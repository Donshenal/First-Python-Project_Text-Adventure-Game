
print(""" 
Far, far away, in an hardly accessible landscape, the legendary Dragon Medal lies hidden.
The Dragon Medal grants its bearer the ancient power to transform into a dragon.
You are on a mission to find the Dragon Medal.

The Medal can be found on a lonely clearing, but to access the Medal, you need a magic spell.

This spell is only known to the great mage, which lives in a tower behind the forest.

However, in the forest there is a bear that doesn't let anyone pass.

To get past you must give the bear a pot of delicious honey. 

Fortunately there is a beekeeper in a nearby town called honeytown.


Your quest starts now.
""")

room = "hometown"
honey = False
spell = False

if room == "hometown":

    print(""" You are currently in your home town, this is the town you grew up in, but it is only a very small town and
                     not much is going on here. Other locations nearby are a lonely clearing, a forest and honeytown.
                     However you can only visit three other locations to finish your quest, so the order of your travels to the other locations must be correct.
                    """)

location_change = input('Do you want to go to another location? (yes/no)')

if location_change == "yes":
                   
            location_2 = input('Where do you want to go? Please enter c, f or h. (for [c]learing, [f]orest or [h]oneytown)')

            if location_2 == 'c' and not spell:
                        print("""You arrived at the lonely clearing and you found the location of the legendary Dragon Medal, 
                                             but the Medal is guarded by a magical barrier, you need a magic spell to remove the barrier.
                                             The spell is only known by the great mage, who lives in a tower behind the forest""") 


            if location_2 == 'f' and not honey:
                        print("""You arrived at the forest, however you can't go the tower behind the forest, 
                                               because a bear doesn't let anyone pass.""")

            if location_2 == 'h' and not honey:
                        print("""You arrived at honeytown, one beekeper in town is an old friend of yours.
                                                 You visit him and he gives you a pot of delicious honey.""")
                        honey = True

            location_3 = input('Where do you want to go next? Please enter c, f or h. (for [c]learing, [f]orest or [h]oneytown)')           
                                
            if location_3 == 'c' and not spell:
                       print("""You arrived at the lonely clearing and you found the location of the legendary Dragon Medal, 
                                             but the Medal is guarded by a magical barrier, you need a magic spell to remove the barrier.
                                             The spell is only known by the great mage, who lives in a tower behind the forest""") 
                                   
            if location_3 == 'f' and not honey:
                        print("""You arrived at the forest, however you can't go the tower behind the forest, 
                                               because a bear doesn't let anyone pass.""")                                   

            if location_3 == 'f' and honey:
                        print("""You arrived at the forest and approach the bear. You give him the delicious honey from 
                                               honeytown, which makes the bear really happy and the bear becomes friendly towards you and lets you pass.
                                               You go to the tower behind the forest, where the great mage lives and you learn the spell to break the magical
                                               barrier in the lonely clearing from her""")
                        spell = True
            
            if location_3 == 'h'and honey:
                        print("""You arrived in honeytown again. You have been here recently and there is nothing more to do here.""")


            if location_3 == 'h' and not honey:
                        print("""You arrived at honeytown, one beekeper in town is an old friend of yours.
                                                                   You visit him and he gives you a pot of delicious honey.""")
                        honey = True

            location_4 = input('Where do you want to go next? Please enter c, f or h. (for [c]learing, [f]orest or [h]oneytown)')   

            if location_4 == 'c' and not spell:
                        print("""You arrived at the lonely clearing and you found the location of the legendary Dragon Medal, 
                                               but the Medal is guarded by a magical barrier, you need a magic spell to remove the barrier.
                                               The spell is only known by the great mage, who lives in a tower behind the forest""") 
              
            if location_4 == 'c' and spell:
                        print(""" On a hidden clearing you discover the legendary Dragon Medal. Your quest has been successful!""")


            if location_4 == 'f' and not honey:
                        print("""You arrived at the forest, however you can't go the tower behind the forest, 
                                               because a bear doesn't let anyone pass.""")                                   

            if location_4 == 'f' and honey:
                        print("""You arrived at the forest and approach the bear. You give him the delicious honey from 
                                               honeytown, which makes the bear really happy and the bear becomes friendly towards you and lets you pass.
                                               You go to the tower behind the forest, where the great mage lives and you learn the spell to break the magical
                                               barrier in the lonely clearing from her""")
                        spell = True

            if location_4 == 'h' and not honey:
                        print("""You arrived at honeytown, one beekeper in town is an old friend of yours.
                                                                   You visit him and he gives you a pot of delicious honey.""")
                        honey = True

            if location_4 == 'h'and honey:
                        print("You arrived in honeytown again. You have been here recently and there is nothing more to do here.")
                   