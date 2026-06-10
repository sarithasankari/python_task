'''
Task 5: Shopping Cart Total cart = [ {"name": "Laptop", "price": 50000}, {"name": "Mouse", "price": 500}, {"name": "Keyboard", "price": 1500} ] Calculate total bill amount.
'''

cart = [ {"name": "Laptop", "price": 50000},
         {"name": "Mouse", "price": 500},
         {"name": "Keyboard", "price": 1500} ]
total_amount=0
for carts in cart:
    total_amount+=carts["price"]
print("total bill : ",total_amount)
