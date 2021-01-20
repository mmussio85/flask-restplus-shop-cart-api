from flask import Flask
import datetime
import pytest
from app.main import db

from app.main.model.item import Item
from app.main.service import item_service
import json

@pytest.fixture
def shoes_one():
    return Item(
        name="Air Force 1",
        supplier="Nike",
        price="100",
        category="basketball"
            
    )
def test_insert_item(app, db, shoes_one):
    item_service.save_changes(shoes_one)
    results = item_service.get_all_items()
    assert results[0].name == "Air Force 1"
    

def test_list_of_items(app, db, client, shoes_one):
    item_service.save_changes(shoes_one)
    response = client.get('/item/')
    assert response.status_code == 200
    assert len(response.json["data"]) == 2
    


if __name__ == '__main__':
    pytest.main()

