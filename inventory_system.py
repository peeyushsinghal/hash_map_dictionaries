# inventory_system.py
from copy import deepcopy

def create_inventory():
    """
    Create and return an inventory using different dictionary creation methods,
    including dictionary comprehensions and dict() constructor.
    """
    electronics = {
        'Laptop': {'name': 'Laptop', 'price': 1000, 'quantity': 5},
        'Smartphone': {'name': 'Smartphone', 'price': 500, 'quantity': 10}
    }
    
    groceries = dict(
        Apples={'name': 'Apples', 'price': 1.5, 'quantity': 100},
        Bananas={'name': 'Bananas', 'price': 0.5, 'quantity': 150}
    )
    
    inventory = {
        'Electronics': electronics,
        'Groceries': groceries,
        **{'Books': {f'Book{i}': {'name': f'Book{i}', 'price': 10 + i, 'quantity': 20} for i in range(1, 4)}}
    }
    
    return inventory

def update_inventory(inventory, category, item_name, update_info):
    """
    Update item information (e.g., increasing stock, updating price) in the inventory.
    """
    if category in inventory and item_name in inventory[category]:
        inventory[category][item_name].update(update_info)
    else:
        raise KeyError(f"Item '{item_name}' not found in category '{category}'")

def merge_inventories(inv1, inv2):
    """
    Merge two inventory systems without losing any data.
    """
    merged = deepcopy(inv1)
    for category, items in inv2.items():
        if category in merged:
            for item_name, item_info in items.items():
                if item_name in merged[category]:
                    # Sum up the quantities
                    merged[category][item_name]['quantity'] += item_info['quantity']
                    # Take the maximum of other values (like price)
                    for key, value in item_info.items():
                        if key != 'quantity':
                            merged[category][item_name][key] = max(merged[category][item_name].get(key, 0), value)
                else:
                    merged[category][item_name] = item_info
        else:
            merged[category] = items
    return merged

def get_items_in_category(inventory, category):
    """
    Retrieve all items in a specified category.
    """
    return inventory.get(category, {})

def find_most_expensive_item(inventory):
    """
    Find and return the most expensive item in the inventory.
    """
    return max(
        (item for category in inventory.values() for item in category.values()),
        key=lambda x: x['price']
    )

def check_item_in_stock(inventory, item_name):
    """
    Check if an item is in stock and return its details if available.
    """
    for category in inventory.values():
        if item_name in category:
            item = category[item_name]
            return item if item['quantity'] > 0 else None
    return None

def view_categories(inventory):
    """
    View available categories (keys of the outer dictionary).
    """
    return list(inventory.keys())

def view_all_items(inventory):
    """
    View all items (values of the inventory).
    """
    return [item for category in inventory.values() for item in category.values()]

def view_category_item_pairs(inventory):
    """
    View category-item pairs (items view of the inventory).
    """
    return [(category, item) for category, items in inventory.items() for item in items.values()]

def copy_inventory(inventory, deep=True):
    """
    Copy the entire inventory structure. Use deep copy if deep=True, else use shallow copy.
    """
    return deepcopy(inventory) if deep else inventory.copy()
