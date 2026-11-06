def calculate_fuel_sales(product, price, quantity):

    if not product.strip():
        raise ValueError("Product name cannot be empty.")
    if price <= 0:
        raise ValueError("Price must be greater than zero.")
    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")
       
    total_sales = quantity * price
       
    return total_sales


def calculate_total_station_sales(sales):
    total_station_sales = 0
    for sale in sales:
        price = sale["price"]
        quantity = sale["quantity"]

        total_sales = price * quantity
        
        total_station_sales += total_sales

    return total_station_sales