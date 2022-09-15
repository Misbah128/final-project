# Syed Hussain
# 09/12/2022
# The scene of the level 2 is Player comes across a building.
# This module will ask user if he want to start the game if he say yes it will start otherwise it will exit.
# Ronny now has to distract guards from the building so he can enter.
# This module will ask user to enter the right weapon to distract the guards.
# If user choose the right weapon than he will win this level otherwise the user has to play again!

import globalvars
# import main
# import functions
def main():
    print("Welcome to chapter 2!")
    game = input("Do you want to start level 2[Yes/No]: ")
    if game.casefold() == "yes":
        print("Starting Level 2!")
    else:
        exit("Thank you & Goodbye!")
    globalvars.gvariables()
    print("In chapter 2", globalvars.protagonist, "reaches", globalvars.antagonist, "building but now", globalvars.protagonist, "has to make a plan and execute it.")
    print(globalvars.protagonist,"needs one of the weapon from the weapon list to distract guards")
    print("Weapon list:",globalvars.weapons_list)
    weapon = input("Which weapon do you think is the best to distract guards from the weapon list?")
    if weapon.casefold() == "rocks":
        print("Yup! you choose the right weapon!\nYou were successful to distract guards")
        globalvars.Chapter2_success = True
        return
    else:
        globalvars.Chapter2_success = False
        print("We are just looking to distract guards!\nPlease check the weapon list and try again!")

if __name__ == "__main__":
    main()
