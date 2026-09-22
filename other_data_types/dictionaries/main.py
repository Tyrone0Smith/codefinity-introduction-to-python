grocery_inventory = {
    "Milk": (113, "Dairy"),
    "Eggs": (116, "Dairy"),
    "Bread": (117, "Bakery"),
    "Apples": (141, "Produce")
}

# Retrieve the details of bread
bread_details = grocery_inventory.get("Bread")
print("Details of Bread:", bread_details)

# Add a new item
grocery_inventory["Cookies"] = (143, "Bakery")
print("Inventory after adding Cookies:", grocery_inventory)

# Remove eggs
removed_item = grocery_inventory.pop("Eggs")
print("Inventory after removing Eggs:", grocery_inventory)