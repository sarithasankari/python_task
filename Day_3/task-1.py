'''Task 1: Product Search System products = [ {"id": 1, "name": "Laptop"}, {"id": 2, "name": "Mobile"}, {"id": 3, "name": "Keyboard"} ] Requirements: Ask user to enter product name.
Search product from list. If found display product details. Otherwise display "Product Not Found".'''


products = [ {"id": 1, "name": "Laptop"},
             {"id": 2, "name": "Mobile"},
             {"id": 3, "name": "Keyboard"} ]
product_name=input("enter the product name : " )
d=False
for product in products:
    if product["name"].lower()==product_name.lower():
        print("ID :",product["id"])
        print("name :",product["name"])
        d=True
        break
if not d:
    print("Product Not Found")










