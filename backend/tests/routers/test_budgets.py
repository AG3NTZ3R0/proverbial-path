from fastapi.testclient import TestClient
from main import app
import mongomock
import pymongo

client = TestClient(app)


# Path: /budgets
@mongomock.patch(servers=(("localhost", 27017),))
def test_get_budgets():
    response = client.get("/budgets")
    assert response.status_code == 200
    assert response.json() == []


# Path: /budgets/{budget_id}
@mongomock.patch(servers=(("localhost", 27017),))
def test_get_budget():
    # Create a budget
    pymongo.MongoClient("mongodb://localhost:27017/")["proverbial-path"]["budgets"].insert_one({"_id": "new_budget"})

    response = client.get("/budgets/new_budget")
    assert response.status_code == 200
    assert response.json() == {"_id": "new_budget"}


# Path: /budgets/{budget_id}
@mongomock.patch(servers=(("localhost", 27017),))
def test_put_budget():
    response = client.put("/budgets/new_budget")
    assert response.status_code == 200
    assert response.json() == {"message": "Budget created", "id": "new_budget"}
