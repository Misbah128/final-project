# Syed Hussain
# 09/12/2022
# The function module has all the fail messages laid out for the game chapters.
# I am going to use this functions module fail messages for my 5 chapters and as well as for the main file!


import globalvars
def fail_mesg(chapter):
    if chapter == 1:
        print("Oops! you fail to get the directions")
        return input("would you like to play again?[yes/no]")
    elif chapter == 2:
        print("Oops! the guards caught you")
        return input("would you like to play again?[yes/no]")
    elif chapter == 3:
        print("Oops! you are injured")
        return input("would you like to play again?[yes/no]")
    elif chapter == 4:
        print("Oops! you failed the riddle")
        return input("would you like to play again?[yes/no]")
    elif chapter == 5:
        print("Oops! you got killed by Raghav")
        return input("would you like to play again?[yes/no]")
# if __name__ == "__main__":
#     globalvars.gvariables()
#     globalvars.protagonist = input("what is your name: ")
#     print("Welcome to my game ", globalvars.protagonist)
#     print(fail_mesg(1))
