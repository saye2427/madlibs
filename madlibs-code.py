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
    print(str("enough " + blank + " to make the trek, but I wasn't not sure I trusted"))
    print(str("my " + blank + "to allow me to do so without getting " + blank + "."))
    print(str(""))
    print(str("So instead, I settled on" + blank + " " + blank + ", something I could"))
    print(str("do closer to home. Maybe I'm not an exemplary in that regard, but I"))
    print(str("sure am" + blank + ". Plus, that was some good " + blank + "!!!"))

    # os.system('clear')


class style:
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def display_story_with_input_type():
    print(str("Here are some parameters that you may wanna follow so your silly story doesn't end up too silly to understand O.o"))
    print(str(""))
    print(str("On my first day in " + style.UNDERLINE + " place " + style.END + ", of course the first thing I"))
    print(str("wanted to " + style.UNDERLINE + " verb " + style.END + " was " + style.UNDERLINE + " noun/thing " + style.END + ". But how? I know I packed"))
    print(str("enough " + style.UNDERLINE + " noun " + style.END + " to make the trek, but I wasn't not sure I trusted"))
    print(str("my " + style.UNDERLINE + " body part " + style.END + " to allow me to do so without getting " + style.UNDERLINE + " emotion/feeling " + style.END + "."))
    print(str(""))
    print(str("So instead, I settled on" + style.UNDERLINE + " verb " + style.END + "ing " + style.UNDERLINE + " noun " + style.END + ", something I could"))
    print(str("do closer to home. Maybe I'm not an exemplary in that regard, but I"))
    print(str("sure am " + style.UNDERLINE + " adjective " + style.END + ". Plus, that was some good " + style.UNDERLINE + " noun " + style.END + "!!!"))

    # os.system('clear')

def test():
    #check blank variable terminal output
    print(blank)
    #check underline class
    print(style.UNDERLINE + "underline text" + style.END)
    #check script exit
    sys.exit()

# test()
greeting()
ready_to_play()
# display_story_with_input_type()
