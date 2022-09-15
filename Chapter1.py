# Syed Hussain
# 09/12/2022
# The scene of level 1 is Ronny comes across a town (Bangkok); local tell him a direction towards Raghav building.
# This module will ask user if he want to start the game if he say yes it will start otherwise it will exit.
# Ronny interacts with the locals and find out the direction.
# This module will ask user to enter what direction he wants to head, if he inserted the right directions from locals
# User will win this level otherwise the user has to play again!

import globalvars
import random
import functions
# import main
# import functions
def main():
    game = input("Do you want to start the game[Yes/No]: ")
    if game.casefold() == "yes":
        print("Starting Level 1!")
    else:
        exit("Thank you & Goodbye!")
    globalvars.gvariables()
    print("In chapter 1", globalvars.protagonist, "out in Bangkok streets to find", globalvars.lover, "form where he could able to find her location from locals.")
    print(globalvars.protagonist,"interact with locals")
    print("where is the building located..")
    direction = 'East', 'South', 'North', 'West'
    location = random.choice(direction)
    print("Locals tell him a direction towards", location,",it's where the", globalvars.antagonist, "building is located.")
    print("Choose the right path from",direction, "to go towards the building.")
    choice = input("where do you want to go?")
    if choice.casefold() == location.casefold():
        print("Yup! you choose the right direction!")
        globalvars.Chapter1_success = True
        return
    else:
        globalvars.Chapter1_success = False
if __name__ == '__main__':
    main()
