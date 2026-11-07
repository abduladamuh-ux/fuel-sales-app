from sales import calculate_fuel_sales, calculate_total_station_sales, get_sales_count

sales = [
    {"product":"   petrol", "price": 1410, "quantity": 1500},
    {"product": "Diesel", "price": 1200, "quantity": 800},
    {"product": "CNG", "price": 800, "quantity": 500}
]

sales_count = get_sales_count(sales)
print(f"Number of sales: {sales_count}")

total_station_sales = 0
total_station_sales = calculate_total_station_sales(sales)
    

for sale in sales:
    product = sale["product"]
    price = sale["price"]
    quantity = sale["quantity"]

    product, total_sales = calculate_fuel_sales(product, price, quantity)
   
    print(f"Product: {product}")
    print(f"Price: ₦{price:,.2f}")
    print(f"Quantity: {quantity}")
    print(f"Total Sales: ₦{total_sales:,.2f}\n")

print(f"Total Station sales: ₦{total_station_sales:,.2f}")