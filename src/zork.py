def Start(inp = ""):
	print("---------------------------------------------------------")
	print("Welcome to Zork - The Unofficial Python Version.")
	return (True, "field")


def OpenField(inp = ""):
	# print("---------------------------------------------------------")
	# print("You are standing in an open field west of a white house, with a boarded front door.")
	# print("You can see a small lake to the north.")
	# print("(A secret path leads southwest into the forest.)")
	# print("There is a Small Mailbox.")
	# inp = input("What do you do? ")

	if inp.lower() == ("take mailbox"):
		print("---------------------------------------------------------")
		print("It is securely anchored.")
	elif inp.lower() == ("open mailbox"):
		print("---------------------------------------------------------")
		print("Opening the small mailbox reveals a leaflet.")
	elif inp.lower() == ("go north"):
		return (True, "lake")
	elif inp.lower() == ("open door"):
		print("---------------------------------------------------------")
		print("The door cannot be opened.")
	elif inp.lower() == ("take boards"):
		print("---------------------------------------------------------")
		print("The boards are securely fastened.")
	elif inp.lower() == ("look at house"):
		print("---------------------------------------------------------")
		print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
	elif inp.lower() == ("go southwest"):
		return (True, "forest")
	elif inp.lower() == ("read leaflet"):
		print("---------------------------------------------------------")
		print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
	elif inp.lower() == ("kick the bucket"):
		return (False, "die")
	else:
		print("---------------------------------------------------------")


def Lake(inp = ""):
	# print("---------------------------------------------------------")
	# print("You find yourself at the edge of a beautiful lake aside rolling hills.")
	# print("A small pier juts out into the lake.")
	# print("A fishing rod rests on the pier.")
	# print("(You can see a white house in the distance to the south.)")
	# inp = input("What do you do? ")

	if inp.lower() == ("go south"):
		return (True, "field")
	elif inp.lower() == ("swim"):
		print("---------------------------------------------------------")
		print("You don't have a change of clothes and you aren't here on vacation.")
	elif inp.lower() == ("fish"):
		print("---------------------------------------------------------")
		print("You spend some time fishing but nothing seems to bite.")
	elif inp.lower() == ("kick the bucket"):
		return (False, "die")
	else:
		print("---------------------------------------------------------")


def Forest(inp = ""):
	# print("---------------------------------------------------------")
	# print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
	# inp = input("What do you do? ")

	if inp.lower() == ("go west"):
		print("---------------------------------------------------------")
		print("You would need a machete to go further west.")
	elif inp.lower() == ("go north"):
		print("---------------------------------------------------------")
		print("The forest becomes impenetrable to the North.")
	elif inp.lower() == ("go south"):
		print("---------------------------------------------------------")
		print("Storm-tossed trees block your way.")
	elif inp.lower() == ("go east"):
		return (True, "clearing")
	elif inp.lower() == ("kick the bucket"):
		return (False, "die")
	else:
		print("---------------------------------------------------------")


def Clearing(inp = ""):
	# print("---------------------------------------------------------")
	# print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
	# print("There is an open grating, descending into darkness.")
	# inp = input("What do you do? ")

	if inp.lower() == ("go south"):
		print("---------------------------------------------------------")
		print("You see a large ogre and turn around.")
	elif inp.lower() == ("descend grating"):
		return (True, "cave")
	elif inp.lower() == ("kick the bucket"):
		return (False, "die")
	else:
		print("---------------------------------------------------------")	


def Cave(inp = ""):

	# print("---------------------------------------------------------")
	# print("You are in a tiny cave with a dark, forbidding staircase leading down.")
	# print("There is a skeleton of a human male in one corner.")
	# inp = input("What do you do? ")

	if inp.lower() == ("descend staircase"):
		return (True, "end")
	elif inp.lower() == ("take skeleton"):
		print("---------------------------------------------------------")
		print("Why would you do that? Are you some sort of sicko?")
	elif inp.lower() == ("smash skeleton"):
		print("---------------------------------------------------------")
		print("Sick person. Have some respect mate.")
	elif inp.lower() == ("light up room"):
		print("---------------------------------------------------------")
		print("You would need a torch or lamp to do that.")
	elif inp.lower() == ("break skeleton"):
		print("---------------------------------------------------------")
		print("I have two questions: Why and With What?")
	elif inp.lower() == ("go down staircase"):
		return (True, "end")
	elif inp.lower() == ("scale staircase"):
		return (True, "end")
	elif inp.lower() == ("kick the bucket"):
		return (False, "die")
	elif inp.lower() == ("scale staircase"):
		return (True, "end")
	else:
		print("---------------------------------------------------------")


def End(inp = ""):
	# print("---------------------------------------------------------")
	# print("You have entered a mud-floored room.")
	# print("Lying half buried in the mud is an old trunk, bulging with jewels.")
	# inp = input("What do you do? ")

	if inp.lower() == ("open trunk"):
		return (True, "win")
	elif inp.lower() == ("kick the bucket"):
		return (False, "die")
	else:
		print("---------------------------------------------------------")


def Restart(inp = ""):
	if inp.lower() == ("n"):
		return (False, "end")
	if inp.lower() == ("y"):
		return (True, "start")

