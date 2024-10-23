# Build a Dynamic Inventory System Using Nested Dictionaries

## Objective:

You will create a dynamic inventory management system where each item in the inventory is represented by a nested dictionary. The inventory will allow for real-time updates, including adding new items, updating existing items, and retrieving information based on complex queries.

## Requirements:

- The outer dictionary represents categories (e.g., electronics, groceries).
- Each category contains a nested dictionary representing individual items, with keys such as "name", "price", "quantity", etc.

## Key Tasks:

1. **Create Inventory:** Populate the inventory using different dictionary creation methods, including dictionary comprehensions and dict() constructor.
2. **Update & Merge:** Allow users to update item information (e.g., increasing stock, updating price) and merge two inventory systems.
3. **Querying:** Write functions to:
   - Retrieve all items in a category.
   - Find the most expensive item in the inventory.
   - Check if an item is in stock and return its details.
4. **Dictionary Views:** Implement functionality to view available categories (keys), all items (values), and category-item pairs (items view).
5. **Serialization:** Implement functionality to copy the entire inventory structure, modify a copy independently, and use deep and shallow copying techniques.

## Challenges:

- Handling the complex nested dictionary structure dynamically.
- Merging multiple inventories while ensuring no data is lost.
- Managing deep copying versus shallow copying efficiently.
