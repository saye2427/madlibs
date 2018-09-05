import os
import sys
import time

blank = "___"

def greeting():
    print(str("Hello there! Welcome to fill-in-the-blank Madlibs, a dying art form!"))

def ready_to_play():
    ready = str(input("Are you ready to play? (y/n): "))
    if ready == 'y' or ready == 'Y':
        print("Great, let's go!")
        time.sleep(1)
        os.system('clear')
        display_story()
    elif ready == 'n' or ready == 'N':
        print("Okay, goodbye.")
        time.sleep(1)
        sys.exit()
    else:
        print("Invalid input! Please try again.")
        ready_to_play()

def display_story():
    print(str("Here's a quick glance of the story you'll be helping to create..."))
    print(str(""))
    print(str("On my first day in " + blank +  ", of course the first thing I"))
    print(str("wanted to " + blank +  " was " + blank + ". But how? I know I packed"))
    print(str("enough " + blank + " to make the trek, but I wasn't sure I trusted"))
    print(str("my " + blank + " to allow me to do so without getting " + blank + "."))
    print(str(""))
    print(str("So instead, I settled on " + blank + "ing " + blank + " " + blank + "(s), something I could"))
    print(str("do closer to home. Maybe I'm not an exemplary in that regard, but I"))
    print(str("sure am " + blank + ". Plus, that was some good " + blank + "!!!"))
    time.sleep(5)
    os.system('clear')

class style:
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def display_story_with_input_type():
    print(str("And now, here's the same story with some parameters that you may wanna follow"))
    print(str("so your silly story doesn't end up too silly to understand!!!:"))
    print(str(""))
    print(str("On my first day in " + style.UNDERLINE + " place " + style.END + ", of course the first thing I"))
    print(str("wanted to " + style.UNDERLINE + " verb " + style.END + " was " + style.UNDERLINE + " noun/thing " + style.END + ". But how? I know I packed"))
    print(str("enough " + style.UNDERLINE + " noun " + style.END + " to make the trek, but I wasn't sure I trusted"))
    print(str("my " + style.UNDERLINE + " body part " + style.END + " to allow me to do so without getting " + style.UNDERLINE + " emotion/feeling " + style.END + "."))
    print(str(""))
    print(str("So instead, I settled on" + style.UNDERLINE + " verb " + style.END + "ing " + style.UNDERLINE + " number " + style.END + " " + style.UNDERLINE + " noun " + style.END + "(s), something I could"))
    print(str("do closer to home. Maybe I'm not an exemplary in that regard, but I"))
    print(str("sure am " + style.UNDERLINE + " adjective " + style.END + ". Plus, that was some good " + style.UNDERLINE + " noun " + style.END + "!!!"))
    time.sleep(10)
    os.system('clear')

def start_game():
    print("So let's get to filling in the blanks, shall we?")

# def blank_user_inputs():
def fill_in_blanks():
    user_inputs = []

    blank1 = str(input("Enter the name of a place you've always wanted to go: "))
    user_inputs.append(blank1)

    blank2 = str(input("Enter a verb; what do you want to do today?: "))
    user_inputs.append(blank2)

    blank3 = str(input("Enter a noun, any noun!: "))
    user_inputs.append(blank3)

    blank4 = str(input("Enter another noun; what's in your bag/pocket right now?: "))
    user_inputs.append(blank4)

    blank5 = str(input("Enter a body part--keep it rated-G please (-_-): "))
    user_inputs.append(blank5)

    blank6 = str(input("Enter an emotion or feeling: "))
    user_inputs.append(blank6)

    blank7 = str(input("Enter a verb; what do you like to do?: "))
    user_inputs.append(blank7)

    blank8 = int(input("Enter a number: "))
    user_inputs.append(blank8)


    blank9 = str(input("Enter one more noun--anything you can think of. The world is your oyster!!!: "))
    user_inputs.append(blank9)

    blank10 = str(input("And lastly, enter an adjective: "))
    user_inputs.append(blank10)

    print("")
    print(str("And now, *DRUMROLL PLEASE*...here's your silly story!!!"))
    time.sleep(3)
    os.system('clear')

    print(str("On my first day in " + user_inputs[0] +  ", of course the first thing I"))
    print(str("wanted to " + user_inputs[1] +  " was " + user_inputs[2] + ". But how? I know I packed"))
    print(str("enough " + user_inputs[3] + " to make the trek, but I wasn't sure I trusted"))
    print(str("my " + user_inputs[4] + " to allow me to do so without getting " + user_inputs[5] + "."))
    print(str(""))
    print(str("So instead, I settled on " + user_inputs[6] + "ing " + str(user_inputs[7]) + " " + user_inputs[8] + "(s), something I could"))
    print(str("do closer to home. Maybe I'm not an exemplary in that regard, but I"))
    print(str("sure am " + user_inputs[9] + ". Plus, that was some good " + user_inputs[8] + "!!!"))

# def fill_in_blanks():
#     blank_user_inputs()
#     # print(user_inputs)
#     #
#     # madlibs_story = str(display_story())
#
#     # i = 0
#     # while i < 11:
#     #     i += 1
#     # completed_madlibs_story = madlibs_story.replace('blank', user_inputs[0])
#     # print(completed_madlibs_story)

def test():
    #check blank variable terminal output
    print(blank)
    #check underline class
    print(style.UNDERLINE + "underline text" + style.END)
    # #check script exit
    # sys.exit()
    #check functions
    # blank_user_inputs()
    # fill_in_blanks()
    #test through index out of range error
    # blank_user_inputs()
    # print(user_inputs[0])
    # print(user_inputs[9])
    fill_in_blanks()

# test()
greeting()
ready_to_play()
display_story_with_input_type()
start_game()
fill_in_blanks()
