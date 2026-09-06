# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

# Count how many times "apples" appears in a tuple
apple_count = shelf.count("apples")
print(f"Number of Apples: {apple_count}")

# Find the index of the first occurrence of "banana"
banana_index = shelf.index("bananas")
print(f"First Banana Index: {banana_index}")

# Checking for a < of an Item
if apple_count < 5:
    print(f"Apples need to be restocked.")
else:
    print(f"Apples are sufficiently stocked.")

# Count how many times "grapes" is in a tuple
grapes_count = shelf.count("grapes")
if grapes_count == 1:
    print(f"Grapes need to be restocked.")
else:
    print(f"Grapes are sufficiently stocked.")

# Checking how many times oranges is in a tuple
if "oranges" in shelf:
    oranges_index = shelf.index("oranges")
    print(f"Oranges are at index: {oranges_index}")
else:
    print("Oranges are out of stock.")
    