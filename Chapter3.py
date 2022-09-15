# Syed Hussain
# 09/12/2022
# The scene of the level 3 is Player comes across martial arts experts.
# This module will ask user if he want to start the game if he say yes it will start otherwise it will exit.
# Ronny now has to kill guards but he only have 1 chance to kill (all at once).
# This module will ask user to enter the right weapon to distract the guards.
# If user choose the right weapon than he will win this level otherwise the user has to play again!

import globalvars
import functions
import random
def main():
    print("Welcome to chapter 3!")
    game = input("Do you want to start level 3[Yes/No]: ")
    if game.casefold() == "yes":
        print("Starting Level 3!")
    else:
        exit("Thank you & Goodbye!")
    globalvars.gvariables()
    print("In chapter 3", globalvars.protagonist, "has to face martial arts experts, \nthey can fight very well and it will be tough for",globalvars.protagonist, "to beat them")
    print("Since",globalvars.protagonist,"is now tired and can't fight this many guys\nBut he has 1 chance to kill all guys at once by using one weapon from his weapon list!")
    print("Weapon list:", globalvars.weapons_list)
    weapon = input("Which weapon do you think is the best to kill all guards at once? ")
    if weapon.casefold() == "bomb":
        print("Yup! you choose the right weapon! \nMission accomplished, you are now in clear")
        globalvars.Chapter3_success = True
        return
    else:
        globalvars.Chapter3_success = False
        print("We are looking to kill all at once! You choose the wrong weapon")
        print(globalvars.protagonist,"got tired and killed by oppenets:/ \nPlease check the weapon list and try again!")


if __name__ == "__main__":
    main()
