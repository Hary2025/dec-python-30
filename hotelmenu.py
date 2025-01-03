#Define the menu of restro
menu= {
'Pizza':40,
'Pasta':50,
'Burger':100,
'Salad':50,
'Coffee':100
}
print(menu)

#Greet
print("Welcome to Ayush Restaurant:")
print("Pizza:Rs40\nPasta:50\nBurger:100\nSalad:50\nCofee:100\n")

order_total=0
item_1=input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total +=menu[item_1]#0+40
    print(f"Your item has been added to order")
else:
    print("Please order something else that i can serve you!")
another_order= input("Do you want to add another item?(Yes/No)")
if another_order=="Yes":
    item_2 = input("Enter the name of second item=")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not aavailable!")
print(f"The total amount of items to pay is {order_total}")



