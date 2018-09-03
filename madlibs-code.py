blank = "___"

def display_story():
    print(str("On my first day in " + blank +  ", of course the first thing I"))
    print(str("wanted to " + blank +  " was " + blank + ". But how? I know I packed"))
    print(str("enough " + blank + " to make the trek, but I wasn't not sure I trusted"))
    print(str("my " + blank + "to allow me to do so without getting " + blank + "."))
    print(str(""))
    print(str("So instead, I settled on" + blank + " " + blank + ", something I could"))
    print(str("do closer to home. Maybe I'm not an exemplary in that regard, but I"))
    print(str("sure am" + blank + ". Plus, that was some good " + blank + "!!!"))

class style:
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# def display_story_with_input_type():
#     print(str("On my first day in " + blank +  ", of course the first thing I"))
#     print(str("wanted to " + blank +  " was " + blank + ". But how? I know I packed"))
#     print(str("enough " + blank + " to make the trek, but I wasn't not sure I trusted"))
#     print(str("my " + blank + "to allow me to do so without getting " + blank + "."))
#     print(str(""))
#     print(str("So instead, I settled on" + blank + " " + blank + ", something I could"))
#     print(str("do closer to home. Maybe I'm not an exemplary in that regard, but I"))
#     print(str("sure am" + blank + ". Plus, that was some good " + blank + "!!!"))

def test():
    print(blank)
    print(style.UNDERLINE + "underline text" + style.END)

test()
display_story()
