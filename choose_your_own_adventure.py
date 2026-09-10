

user_choice = None

print("You are a courier for a trading post next to a big forest")
print("You need to deliver a letter to a village before night")
print("You come to a fork in the path")
print("A: take the short path through the forest")
print("B: take the long path by the river")

user_choice = input()
user_choice = user_choice.lower()

if user_choice == "a":
    print("You go into the forest, It is quiet")
    print("Then you hear something crying for help.")
    print("A: go check it out")
    print("B: keep walking")

    user_choice = input()
    user_choice = user_choice.lower()

    if user_choice == "a":
        print("You find a fox with its paw stuck in a trap")
        print("A: free the fox")
        print("B: go back and get help")

        user_choice = input()
        user_choice = user_choice.lower()

        if user_choice == "a":
            print("You free the fox. It leads you to a shortcut")
            print("You get to the village early, THE END - Ending 1")
        else:
            print("By the time you get back the fox is already gone")
            print("You are late but you still deliver the letter, THE END - Ending 2")
    else:
        print("You keep walking but the path starts to look different")
        print("A: keep going forward")
        print("B: climb a tree to look around")

        user_choice = input()
        user_choice = user_choice.lower()

        if user_choice == "a":
            print("You push through and find the path again.")
            print("You make it to the village right before dark, THE END - Ending 3")
        else:
            print("From the tree you can see the village lights.")
            print("You get down and walk right to the village, THE END - Ending 4")
else:
    print("You walk along the river. It is a longer way")
    print("You find an old boat tied up by the water")
    print("A: take the boat")
    print("B: keep walking on foot")

    user_choice = input()
    user_choice = user_choice.lower()

    if user_choice == "a":
        print("You get in the boat and the water starts moving faster")
        print("A: row fast to the other side")
        print("B: stop at a calm spot and wait")

        user_choice = input()
        user_choice = user_choice.lower()

        if user_choice == "a":
            print("You row as fast as you can and just make it across")
            print("You get to the village with time to spare, THE END - Ending 5")
        else:
            print("You wait until the water calms down then keep going.")
            print("You are a little late but you made it safe, THE END - Ending 6")
    else:
        print("You keep walking. You hear thunder far away")
        print("A: find shelter and wait out the storm")
        print("B: keep walking fast to beat the rain")

        user_choice = input()
        user_choice = user_choice.lower()

        if user_choice == "a":
            print("You wait under a rock until the storm passes")
            print("You get to the village late but dry. THE END - Ending 7")
        else:
            print("You walk fast and just barely beat the rain.")
            print("You deliver the letter right on time, THE END - Ending 8")



