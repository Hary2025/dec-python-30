import random
print(" Game Rule\n Type 0 for Rock, Type 1 for Paper, AND Type 2 for Scissor")
user_choice=int(input("Enter your Choice:"))

computer_choice=random.randint(0,2)
print("computer_choice:", computer_choice)
if user_choice not in[0,1,2]:
    print("Invalid Number... Please type  0,1 or 2 to play this game ")
elif computer_choice==user_choice:
    print("Its a draw")
elif user_choice == 0 and computer_choice == 2:
    print("You win")
elif user_choice == 1 and computer_choice == 0:
    print("You won.")
elif user_choice == 2 and computer_choice == 0:
     print("You Loose..Better luck next time.")
elif user_choice>computer_choice:
    print("You won")


elif computer_choice>user_choice:
    print("Computer won...Better luck next time")
else:
    print("Compter Won")

    






