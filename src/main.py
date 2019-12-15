# Main game file

import zork


def print_list(l):
    for line in l:
        print(line)



functions = {"field":zork.OpenField,
             "lake":zork.Lake,
             "forest":zork.Forest,
             "clearing":zork.Clearing,
             "cave":zork.Cave,
             "end":zork.End,
             "die":zork.Restart,
             "win":zork.Restart,
             "start":zork.Start,
             }

messages = {"field":["---------------------------------------------------------","You are standing in an open field west of a white house.","You can see a small lake to the north.","(A secret path leads southwest into the forest.","There is a Small Mailbox."],
            "lake":["---------------------------------------------------------","You find yourself at the edge of a beautiful lake aside rolling hills.","A small pier juts out into the lake.","A fishing rod rests on the pier.","(You can see a white house in the distance to the south."],
            "forest":["---------------------------------------------------------","This is a forest, with trees in all directions. To the east, there appears to be sunlight."],
            "clearing":["---------------------------------------------------------","You are in a clearing, with a forest surrounding you on all sides. A path leads south.","There is an open grating, descending into darkness."],
            "cave":["---------------------------------------------------------","You are in a tiny cave with a dark, forbidding staircase leading down.","There is a skeleton of a human male in one corner."],
            "end":["---------------------------------------------------------","You have entered a mud-floored room.","Lying half buried in the mud is an old trunk, bulging with jewels."]}

continue_messages = {"win":["---------------------------------------------------------","You have found the Jade Statue and have completed your quest!"],
                    "die":["---------------------------------------------------------","You die.","---------------------------------------------------------"]}

status = "start"
alive = True

while(alive == True):
    inp = ""


    if status in messages:
        message = messages[status]
        print_list(message)

        inp = input("What do you do? ")
    
    elif status == "win":
        message = continue_messages[status]
        print_list(message)
        inp = input("Do you still want to coninue? Y/N ")

    function = functions[status]
    
    #format is (alive, status)
    
    output = function(inp)

    #function outputs a new place / a death
    if(not (output is None)):
        alive = output[0]
        status = output[1]
    
    if (not alive):
        print_list(continue_messages["die"])
        inp = input("Do you still want to coninue? Y/N ")
        output = zork.Restart(inp)
        alive = output[0]
        status = output[1]


def PrintOutput(s):
    print("OUTPUT", s)

