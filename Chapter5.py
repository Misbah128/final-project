# Syed Hussain
# 09/12/2022
# This is the final fight of the game where Ronny fights against Raghav.
# This module will ask user if he want to start the game if he say yes it will start otherwise it will exit.
# Ronny now has to kill Raghav but he only have 3 weapon left from his weapon list (Knief, Sword, or Dagger).
# This module will ask user to enter the right weapon to he has so he can use to kill Raghav.
# If user choose the right weapon than he will win the final round otherwise the user has to play again!
# After winning this game he gets his partner back and will win the whole game.
# User will also have option to play the game again!

import globalvars
import functions
import random
def main():
    print("Welcome to chapter 5!")
    game = input("Do you want to start level 5[Yes/No]: ")
    if game.casefold() == "yes":
        print("Starting Level 5!")
    else:
        exit("Thank you & Goodbye!")
    globalvars.gvariables()
    print("Chapter 5 is the final chapter of the game", globalvars.protagonist, "now get to meet his main opponent",globalvars.antagonist,",this is when he gets his partner", globalvars.lover, "once he wins!")
    print(globalvars.protagonist,"interact with main opponent",globalvars.antagonist)
    print(globalvars.antagonist,"angrily running to attack",globalvars.protagonist)
    print("Choose a right weapon to fight back from weapon list",globalvars.weapons_list)
    print("Since you have already used 2 weapons out of 5, You only have 3 left!\nChoose you weapons from Knief, Sword, or Dagger!")
    weapon_choice = input("What weapon would you like to choose? ")
    if weapon_choice.casefold() == 'knief' or weapon_choice.casefold() == 'sword' or weapon_choice.casefold() == 'dagger':
        print("You have selected", weapon_choice, "to fight!")
        attack = input("Press 'K + ENTER' to attack: ")
        if attack.casefold() == 'k':
            print("You killed him")
            print("You have successfully completed the game:), You won", globalvars.lover,"back!" )
        else:
            globalvars.chapter5_success = False
    else:
        print("You failed to choose the right weapon\nPlease check your weapon availability and try again!")



if __name__ == "__main__":
    main()
