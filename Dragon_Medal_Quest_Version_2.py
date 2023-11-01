

print(""" 
Far, far away, in an hardly accessible landscape, the legendary Dragon Medal lies hidden.
The Dragon Medal grants its bearer the ancient power to transform into a dragon.
You are on a mission to find the Dragon Medal.

Your quest starts now.
""")

room_descriptions = {
    'hometown': """You are currently in your home town, this is the town you grew up in, 
but it is only a very small town and not much is going on here. 
Other locations nearby are a lonely clearing and a forest.""",
    'forest': """You arrived at the forest, however, you can't go to the tower behind the forest 
because a bear doesn't let anyone pass. Nearby locations are hometown and honeytown.""",
    'honeytown': """You arrived at honeytown, one beekeeper in town is an old friend of yours. 
You visit him and he gives you a pot of delicious honey. You can only go back to the forest from here.""",
    'clearing':  """You arrived at the lonely clearing, but you can't enter because it is 
guarded by a magical barrier. You need a magic spell to remove the barrier. 
The spell is only known by the great mage. You can go to your hometown or the forest from here."""
}

paths = {
    "hometown": ["clearing","forest","hometown"],
    "clearing": ["hometown","forest"],
    "forest": ["hometown","honeytown"],
    "honeytown": ["forest"]
}
room = "hometown"
honey = False
spell = False
rooms = ['hometown', 'forest', 'honeytown', 'clearing']

if room == "hometown":
    print(room_descriptions[room])

while room != "clearing":

    target = input("""Where would you like to go next? 
    Please enter hometown, forest, honeytown or clearing:""").lower()

    if target in rooms and target in paths[room]:
        if target == "forest" and honey == False:
            print(room_descriptions[target])
            room = target
        elif target =="hometown":
            print(room_descriptions[target])
            room = target
        elif target == "honeytown" and honey == False:
            print(room_descriptions[target])
            honey = True
            room = target
        elif target == "honeytown" and honey == True:
            print("""You arrived in honeytown again. You have been here recently and there is nothing more to do here. 
You can only go to the forest from here.""")
            room = target
        elif target == "forest" and spell == True:
            print("""You already went to the mage in the tower to learn the spell, there is nothing more to do here.
You can go to your hometown and to honeytown from here.""")
            room = target
        elif target == "forest" and honey == True:
            print("""You arrived at the forest and approach the bear. You give him the delicious honey from honeytown, 
which makes the bear really happy and he becomes friendly towards you and lets you pass. 
You go to the tower behind the forest, where the great mage lives and you learn a spell 
to break the magical barriers from her and you go back to the forest. 
From there you can go back to your hometown or honeytown.""")
            spell = True
            room = target
        elif target == "clearing" and spell == False:
            print(room_descriptions[target])
        elif target == "clearing" and spell == True:
            room = target

    else:
        print("Wait! That is not one of the options given.")

print("""
With the magical spell you learned you make the barrier disappear and
on a hidden clearing, you discover the legendary Dragon Medal.
Your quest has been successful!
""")