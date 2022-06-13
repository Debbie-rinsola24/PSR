from ast import If
import random

CHOICES = ["rock", "paper", "scissors"]

print("make your throw")

user_choices = input("   Type rock, paper, or scissors:  ")

If  user_choices in CHOICES:
    computer_choice = random.choices(CHOICES)

    print(
        f"\nYou threw '{user_choice}' ,  the computer threw  '{computer_choice}'  "
    )

    else:
        print(f"\nYou typed  '{user_choice}'  which isn't a valid throw")

        again = input("\nWant some more? (y/n):  ")
        If again.lower() == "n" :
            break

        print("\nGoodbye")
