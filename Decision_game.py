
"""
|-----------------------------------------------------------------------|
|    o   \ o /  _ o         __|    \ /     |__        o _  \ o /   o    |
|   /|\    |     /\   ___\o   \o    |    o/    o/__   /\     |    /|\   |
|   / \   / \   | \  /)  |    ( \  /o\  / )    |  (\  / |   / \   / \   |
|-----------------------------------------------------------------------|"""

from curses import nl


print("Welcome to the decision game!!")
print("Your mission is to navigate the forest")
choice1= input("Where would you like to turn? Left or right? ").lower()



if choice1 == 'left':
   choice2= input("\nDo you want to swim or wait?")
   if choice2 == 'wait':
    choice3= input("\nWhat door do you want to go through? Red, yellow or blue?")
    if choice3 == "red":
        print("\nGame over")
    elif choice3 == "yellow":
        print("\nYou win")
    elif choice3 == "blue":
        print("\nGame over!")
    else:
       print("\nGame over")
   else:
       print("\nSwim Game over")
else:
    print("\nGame over")