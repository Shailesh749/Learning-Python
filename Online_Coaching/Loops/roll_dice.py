"""
Write a program to simulate a roll of a die / dice a die has 6 faces with numbers 1 to 6 written an them
The program should randomly prints a number between 1 and 6
"""


import random 
# die = [1, 2, 3, 4, 5, 6]
# print(random.choice(die))

print("Welcome to the game of rolling a dice.")
 
while True:
    choice = input("Press 'Enter' to roll the dice or 'q' to quit. ")
    choice = choice.strip() # space removing
    if choice == 'q':
        print("Thanks for playing the game, bye!")
        break
    elif choice =='':
      number = random.randint(1, 6)
      print(f"Your number is {number}")
    else:
      print("Invalid input!!")  

print("GAME OVER!!!")       