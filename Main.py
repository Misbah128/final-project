# Syed Hussain
# 09/12/2022
# This is the main file for my game, this game is going to use this main file to run all my 5 chapters from it!
# Additionally to all 5 chapters of the game, I have imported globalvars and functions module into it.
# This main file also have introduction of the game, where it introduces what this game is going to about!



import Chapter1
import Chapter2
import Chapter3
import Chapter4
import Chapter5
import globalvars
import functions


def gamestory():
        name = input("what is your name: ")
        print("Hello", name, "I hope you are doing alright")
        print("Welcome to the game!")
        print("There are 3 main characters in this game: Ronny(hero), Siya(partner) and Raghav(villain)")
        print("The character 'Ronny' tries to find his partner 'Siya',\nwho got kidnapped by villain 'Raghav'.")
        print("Raghav took Siya to his building which is 5 floors big located in Bangkok \nIn each floor Raghav put some tasks to guard the building "
              "from anyone coming. \nRonny has to win all those tasks from first floor to the fifth till he reaches Raghav"
              " that is where the final fight occurs. \nOnce he wins the final fight with Raghav than he gets to take Siya with him back home.")


def main():
    continue_playing = "Yes"
    while continue_playing.casefold() == "yes":
        Chapter1.main()
        if globalvars.Chapter1_success:
            Chapter2.main()
            if globalvars.Chapter2_success:
                Chapter3.main()
                if globalvars.Chapter3_success:
                    Chapter4.main()
                    if globalvars.Chapter4_success:
                        Chapter5.main()
                        if globalvars.Chapter5_success:
                            continue_playing = input("Would you like to restart the game again?[Yes/No]")
                            if continue_playing.casefold() == "no":
                                exit("Thank you & Goodbye!")
                            else:
                                continue_playing = "yes"
                        else:
                            continue_playing = functions.fail_mesg(5)
                    else:
                        continue_playing = functions.fail_mesg(4)
                else:
                    continue_playing = functions.fail_mesg(3)
            else:
                continue_playing = functions.fail_mesg(2)
        else:
            continue_playing = functions.fail_mesg(1)



if __name__ == '__main__':
    gamestory()
    main()
