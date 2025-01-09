operation=input("Enter which operation do you want to perform :")
num1=int(input("Enter first number"))
num2=int(input("Enter second number"))

if operation=="+" or "add":
    print("The total is:",num1+num2) 
elif operation=="-" or "sub":
    print(num1-num2)
elif operation=="*" or "multiply":
    print(num1*num2)
elif operation=="/" or "divide":
    print(num1/num2)
else:
    print("Invalid...! I can only perform add,sub,multiple and divide.\n")
