# Syed Hussain
# 09/12/2022
# The scene of the level 4 is Player comes across a riddle.
# This module will ask user if he want to start the game if he say yes it will start otherwise it will exit.
# Ronny now has to solve the riddle to unlock the door for level 5.
# This module will ask user to enter the right answer for the riddle (This riddle has possible 3 answers).
# If user answer it right than he will win this level otherwise the user has to play again!

import globalvars
import functions
import random
def main():
    print("Welcome to chapter 4!")
    game = input("Do you want to start level 4[Yes/No]: ")
    if game.casefold() == "yes":
        print("Starting Level 4!")
    else:
        exit("Thank you & Goodbye!")
    globalvars.gvariables()
    print("In chapter 4", globalvars.protagonist, "has to solve a riddle to face the main opponent player", globalvars.antagonist,"!")
    print(globalvars.protagonist,",here is your riddle, if you pass you unlock the door to floor 5!")
    riddle = input("Riddle is: I never ask questions, but always answered. What am I? (hint: all homes has it) ")
    if riddle.casefold() == 'door' or riddle.casefold() == 'doorbell' or riddle.casefold() == 'bell':
        globalvars.chapter4_success = True
        print("Yup! you got the riddle right! Door Unlocked!")
        # print("")
        return
    else:
        globalvars.chapter4_success = False

if __name__ == "__main__":
    main()
