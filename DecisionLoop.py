

def start():
    print("you are inside a dark room")
    print("there are only two doors, one on the left and one on the right")
    print("which one will you choose? left or right?")
    choice = input(">")
    if(choice == "left"):
        bear_room()
    elif (choice == "right"):
        gold_room()
    else:
        print("khattam julaka kei ni bhayena !!!")


def bear_room():
    print("you are inside a room with a bear")
    print("bear is looking at you and you have to sneak into the room")
    print("will you disattract the bear or simply open another door?")
    door = input(">")
    if(door == "open"):
        print("fuck, you are dead piece of meat now!!!")
    elif(door == "closed"):
        print("bear has give you the way now move on")
        gold_room()
    else:
        print("I think the bear is dead !!!")


def gold_room():
    print("fucker you earned the gold!! get lost now you bastard")


start()