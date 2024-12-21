from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from pathlib import Path

app = FastAPI()

# Path to the data file
DATA_FILE = Path("data/items.json")

# Helper functions to read and write data
def read_data():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

def write_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=2)

# Pydantic model for the item
class Item(BaseModel):
    id: int
    name: str
    description: str = None

# Routes
@app.get("/items")
def get_items():
    """Retrieve all items."""
    return read_data()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    """Retrieve a single item by ID."""
    items = read_data()
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items")
def create_item(item: Item):
    """Create a new item."""
    items = read_data()
    if any(existing_item["id"] == item.id for existing_item in items):
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items.append(item.dict())
    write_data(items)
    return {"message": "Item created successfully"}

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    """Update an item by ID."""
    items = read_data()
    for index, item in enumerate(items):
        if item["id"] == item_id:
            items[index] = updated_item.dict()
            write_data(items)
            return {"message": "Item updated successfully"}
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    """Delete an item by ID."""
    items = read_data()
    for index, item in enumerate(items):
        if item["id"] == item_id:
            items.pop(index)
            write_data(items)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
