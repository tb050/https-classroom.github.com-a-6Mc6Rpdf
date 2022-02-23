#!/usr/bin/env python3

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2 or door #3?""")

door = input("-> ")

# == Door Numbwe 1 logic =====================
if door == "1":
    
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?\n")

    print("1. Take the cake.")
    print("2. Scream at the bear.")

    # == Bear logic ===================
    bear = input("-> ")

    if bear == "1":
        print("1) The bear eats your face off. Good job!")
    elif bear == "2":
        print("2) The bear eats your legs off. Good job!")
    else:
        print(f"N)Well, doing {bear} is probably better.")
        print("Bear runs away.")

# == Door Number 2 Logic ======================
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.\n")

    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    # == Insanity Logic ========================
    insanity =input("-> ")

    if insanity == "1" or insanity == "2":
        print("1) Your body survives powered by a mind of jello.")
        print("1) Good job!")
    else:
        print("N) The insanity rots your eyes into a pool of muck.")
        print("N) Good job!")

    # == Door Number 3 Logic =====================
elif door == "3":
    print("Famous Fortnite streamer Ninja is behind the door and invites you onto the Battles Bus.")
    print("What do you do?\n")

    print("1. Board the Battle Bus")
    print("2. Ignore invitation")
    print("3. Try to down Ninja immediately")

        # == Fortnite Logic =======================
    fortnite = input("-> ")
    if fortnite == "1":
        print("1) You and Ninja wipe out Tomato Town and secure an epic victory royale")
        print("1) Victory Royale")
    elif fortnite == "2":
        print("2) Ninja calls you cringe and you are downed immediately after dropping in Wailing Woods")
        print("2) You took the L")
    elif fortnite == "3":
        print("3) Ninja quickscopes you and you are kicked for hacking")
        print("3) You didn't stick the landing")
    else:
        print("N) You didn't acknowledge Ninja and were kicked for being AFK")
        print("N) Good end. you didn't play Fortnite")

else:
    print("You did not select a door??? Good Call :)")