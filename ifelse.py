print("Hello,Welcome to Ayush Coffee!!!")
name= input("What is your name? ")

menu="latte,mocha,espresso,cappicino,afredo"
if name == "ayush":
    print("I am sorry " + name + " ,  you cannot make an order... Go to the accounts and clear your credit. ")
    exit()
    
else:
    print("Hello, " + name + " thank you so much comming in today.")
menu="afredo, espresso, black cofee, frappe"

print("Hello " + name + " What would you like to order?.\nHere is what we have today's menu\n " + menu )
order =input("")
price=8
quantity=input("How many coffee do you like ?")
total = price * int(quantity)
print("Your total bill is :",total)
print("Sounds good " + name + " Your drink will be ready in 5 mins\n please hold on" )






