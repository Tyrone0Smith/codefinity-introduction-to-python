# The item's discount and stock status have been defined
discounted = False
lowStock = True

# Defining a boolean variable
movingProduct = (discounted or lowStock)

# Creating a boolean variable
promotion = (not discounted and not lowStock)

print(f"Is the item eligible for promotion? {promotion}")

