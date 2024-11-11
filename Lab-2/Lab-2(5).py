items = []

n = int(input("Enter the number of items: "))

for i in range(n):
    name = input(f"Enter the name of item {i+1}: ")
    quantity = int(input(f"Enter the quantity of item {i+1}: "))
    price = float(input(f"Enter the price per unit of item {i+1}: "))
    
    items.append({
        'name': name,
        'quantity': quantity,
        'price': price
    })

print("-------------- BILL --------------")
print("{:<15} {:<15} {:<10}".format("Name", "Item Quantity", "Item Price"))
print("-" * 40)

total_amount = 0


for item in items:
    name = item['name']
    quantity = item['quantity']
    price = item['price']
    
    item_total = quantity * price
    total_amount += item_total
    
    print("{:<15} {:<15} {:<10.2f}".format(name, quantity, item_total))

print("-" * 40)
print("Total Amount to be paid: {:.2f}".format(total_amount))
print("-" * 40)
