"""
Test script for Todo API
Run this after starting the server to test all endpoints
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def print_response(endpoint, response):
    """Pretty print API response"""
    print(f"\n{'='*60}")
    print(f"Endpoint: {endpoint}")
    print(f"Status Code: {response.status_code}")
    print(f"Response: {json.dumps(response.json(), indent=2)}")
    print(f"{'='*60}")

def test_api():
    """Test all API endpoints"""
    
    print("\n🚀 Starting API Tests...\n")
    
    # 1. Test root endpoint
    print("1. Testing root endpoint...")
    response = requests.get(f"{BASE_URL}/")
    print_response("GET /", response)
    
    # 2. Test health check
    print("\n2. Testing health check...")
    response = requests.get(f"{BASE_URL}/health")
    print_response("GET /health", response)
    
    # 3. Create a todo
    print("\n3. Creating a new todo...")
    todo_data = {
        "title": "Complete hackathon project",
        "completed": False
    }
    response = requests.post(f"{BASE_URL}/todos", json=todo_data)
    print_response("POST /todos", response)
    todo_id = response.json()["id"]
    
    # 4. Create another todo
    print("\n4. Creating another todo...")
    todo_data2 = {
        "title": "Test the API endpoints",
        "completed": False
    }
    response = requests.post(f"{BASE_URL}/todos", json=todo_data2)
    print_response("POST /todos", response)
    
    # 5. Get all todos
    print("\n5. Getting all todos...")
    response = requests.get(f"{BASE_URL}/todos")
    print_response("GET /todos", response)
    
    # 6. Get specific todo
    print(f"\n6. Getting todo with ID {todo_id}...")
    response = requests.get(f"{BASE_URL}/todos/{todo_id}")
    print_response(f"GET /todos/{todo_id}", response)
    
    # 7. Update todo
    print(f"\n7. Updating todo {todo_id}...")
    update_data = {
        "title": "Complete hackathon project - UPDATED",
        "completed": False
    }
    response = requests.put(f"{BASE_URL}/todos/{todo_id}", json=update_data)
    print_response(f"PUT /todos/{todo_id}", response)
    
    # 8. Mark as complete
    print(f"\n8. Marking todo {todo_id} as complete...")
    response = requests.patch(f"{BASE_URL}/todos/{todo_id}/complete")
    print_response(f"PATCH /todos/{todo_id}/complete", response)
    
    # 9. Get completed todos
    print("\n9. Getting completed todos...")
    response = requests.get(f"{BASE_URL}/todos?completed=true")
    print_response("GET /todos?completed=true", response)
    
    # 10. Get statistics
    print("\n10. Getting todo statistics...")
    response = requests.get(f"{BASE_URL}/todos/stats/summary")
    print_response("GET /todos/stats/summary", response)
    
    # 11. Delete todo
    print(f"\n11. Deleting todo {todo_id}...")
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    print(f"\n{'='*60}")
    print(f"Endpoint: DELETE /todos/{todo_id}")
    print(f"Status Code: {response.status_code}")
    print(f"Response: Todo deleted successfully")
    print(f"{'='*60}")
    
    # 12. Verify deletion
    print("\n12. Verifying deletion - getting all todos...")
    response = requests.get(f"{BASE_URL}/todos")
    print_response("GET /todos", response)
    
    print("\n✅ All tests completed!\n")

if __name__ == "__main__":
    try:
        test_api()
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to the API server.")
        print("Make sure the server is running on http://localhost:8000")
        print("\nStart the server with:")
        print("  python main.py")
        print("or")
        print("  uvicorn main:app --reload")
    except Exception as e:
        print(f"\n❌ Error during testing: {e}")
