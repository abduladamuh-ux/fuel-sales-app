from sales import calculate_fuel_sales

sales = [
    {"product": "Petrol", "price": 1410, "quantity": 1500},
    {"product": "Diesel", "price": 1200, "quantity": 800},
    {"product": "CNG", "price": 800, "quantity": 500}
]

total_station_sales = 0

for sale in sales:
    product = sale["product"]
    price = sale["price"]
    quantity = sale["quantity"]

    total_sales = calculate_fuel_sales(product, price, quantity)
    total_station_sales += total_sales
    
    print(f"Product: {product}")
    print(f"Price: ₦{price:,.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total Sales: ₦{total_sales:,.2f}\n")

print(f"Total Station sales: ₦{total_station_sales:,.2f}")