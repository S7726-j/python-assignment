inventory = {}

def add_inventory(item , price , quantity):
    inventory[item] = ( "₹" + str(price), quantity )

def update(item_update , sale_quantity, quantity):
    inventory[item_update] = ( "₹" + str(price), quantity - sale_quantity )
    
    

n = int(input("Enter no. of items : "))

for i in range(n):
    item = input(" Enter item : ")
    price = int(input(" Enter price : "))
    quant = int(input(" Enter quantity : "))
    print()
    add_inventory(item, price, quant)
    print(f"Inventory : {inventory1}")
    print()
    
item_update = input("Enter item to update quantity : ")
sale_quant = int(input(" Enter sale quantity : "))
update(item_update, sale_quant, quant)
print(inventory)

