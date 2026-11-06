def calculate_fuel_sales(product, price, quantity):

    if not product.strip():
        raise ValueError("Product name cannot be empty.")
    if price <= 0:
        raise ValueError("Price must be greater than zero.")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
       
    total_sales = quantity * price
       
    return total_sales
