# coding: utf-8
#This file has the game intro, conclusion, and a help guide to beat the game
import Character.Character as Character

def game_intro():
    print """
 You wake up, head throbbing, you reach your hand up to check your
 forehead and a little bit of blood comes off onto your hand. You realize
 that you're lying on a cold stone floor, it's incredibly dark in the room
 except for light coming from a hole in the ceiling. And then you remember
 your walk. You'd been out hiking in the woods when you fell...and now here you
 are in a damp and cold dungeon. Could this be the part of the castle from the
 tales of old? Legend has it that a mage from the old kingdom took it over
 centuries ago and went mad trying to find a spell for eternal life...
 But then again those were just tales to keep kids from wandering too far into
 the woods, surely this is someplace else. You rise, dust yourself off and decide
 to check out your surroundings while looking for a way out.\n"""

def game_conclusion():
    print """
 Your eyesight slowly returns to you and as it does an older man in ragged
 robes stands before you, he's as astonished to see you as you are him. His
 eyes begin to water and he breaks down sobbing. "You see" wheezing he says "I've
 been trapped inside that monstrosity for centuries and I've done unspeakable
 things while it manipulated my will and essence. Until you came along and
 put an end to it. I cannot thank you enough. Please destroy those tomes from
 the shadow corridor, they're what I used to bring about this malignant plague
 upon this castle. I cannot..." and before he finishes the sentence the whole
 of time catches up to him and he crumples into dust. Remembering what he said
 you go back to the shadow corridor and there are the two tomes. You take your
 torch out, light it and then spread the flame to the tomes. As they catch fire
 an unearthly noise pierces the air, and then, silence. The walls around you
 transform from their dreary gray and black to a beatiful light marble and a
 path appears that you hadn't noticed previously. You take it, and as it ascends
 you smell the fresh air, hear birds chirp, and feel a faint breeze. You leave
 and enter the forest again for the first time in what seems like forever..."""

def game_menu():
    print """
    ***************************************************************************
                    Welcome to The Aquarius Adventure Game!
                    To start enter one of the following:
                    newgame - starts a new game
                    loadgame - loads the latest saved game
                    walkthrough - displays Aquarius walkthrough
    ***************************************************************************
    """
    game_start = raw_input('> ')
    return game_start

def game_walkthrough():
    print """
    Dungeon Entrance:
    *First thing you’ll want to do is “grab torch”
    **A note, at any time you can type “inventory” to see what you currently have
    on your character. Also, “help” is a useful command that will indicate viable
    commands the player may use**
    *Next, you’ll want to “use closet”, this reveals arrows in the room, go ahead
    and “grab arrows” -- you’ll need them later
    *You’re done with this room, “go east”

    Southeast Corridor:
    *There are room features here that can be interacted with, but they aren’t necessary
    *For now type “go east’ again, this will lead you to…

    Alcove:
    *The Alcove has another one of the necessary items for game progression,
    the hero’s sword
    *The sword is within the display case, type “use display case”
    *This will initiate a riddle that’s required to open the case,
    type the following phrase exactly “wind wood fire mountain”
    *This phrase unlocks the case and reveals the sword, “grab sword” to pick it
    up and move on
    *Time to leave, “go west”

    Southeast Corridor:
    *Again, nothing crucial to game progression here, this time “go north”

    Great Hall:
    *The Great Hall, this is the first instance you should be facing a monster!
    Luckily for you, you’ve got this handy guide and have been following along
    dutifully. Thus, when a menacing skeleton pops out upon your entrance you’ll
    vanquish it! Otherwise, certain doom would have awaited you.
    *The Great Hall does not contain anything necessary for game progression, it
    just has monsters ready to take down brash adventurers
    *Feel free to use any of the features within the room, otherwise, “go north”

    Torch Corridor:
    *The torch corridor is a very special place but at the moment our hero does
    not have the necessary items to make use of it.
    *Thus, “go north” again

    Northeast Corridor:
    *This corridor, like the other directional corridors, does not have much
    pragmatic use for the adventurer
    *Let’s continue, “go west”

    Shadow Corridor:
    *This place has some cool tomes that might be worth the hero checking out to
    get some of the lore behind the place and a feel for what lies ahead
    *Otherwise, “go south”

    Gear Room:
    *This is one of the more important rooms in the game, on the wall is a gear
    which you will be prompted to interact with, type “yes”
    *This will bring up a maze that the player must type exact directions for to
    get to the x in the middle. It’s a bit hard so I suggest you copy and paste
    the following exactly “up left down right down left up right up left up right
    down right down left up left down right up right down left”
    *Eureka! You’ve gained entry to the Bow Room, let's go there “go south”

    Bow Room:
    *Alright, you’re progressing nicely. In here the key thing is quite obviously
    the bow. Go ahead and “grab bow”
    *A quick check of your inventory and at this point you should have your torch,
    arrows, sword, and bow. If you’ve dropped anything in a different room go back
    and grab it. You’ll need all of them (except the torch), to progress from here on out
    *Ok now time to go back to the Torch corridor. To get there “go north”,
    “go north” again, “go east”, and then “go south”

    Torch Corridor:
    *Back again, but now we have the necessary tools (the bow & arrows), to make
    use of the room
    *The reason we needed them is to clear out the gas from the gaseous room, go
    ahead and “use blue torch”
    *Now “go east”

    Gaseous Room:
    *With the gas cleared it’s safe to enter. Within the gaseous room is another
    case, this time containing a key to the End Room!
    *Time to “use puzzle case”, to reveal a riddle and:
    *The missing word that you need to fill in is “dust”
    *The key should now be revealed “grab end room key”
    *Time to make our way back to the shadow corridor and from there to the northwest
    corridor. Take the following path: “go west”, “go north”, and “go west”
    *“Go west” once more to enter...

    Northwest Corridor:
    *Tricked you, it’s another directional corridor, the cool stuff is just up
    ahead though
    *Now “go south”

    Diamond Room:
    *Here in the diamond room you’ll need to “use chair” in order to position it
    in a place where you can access the switch
    *Go ahead and “flip switch”, this reveals the passageway to the Barrel Room
    *“Go south” to the Barrel Room

    Barrel Room:
    *Another monster fight! Since you have both your bow and sword at this point
    you’ll be able to easily eliminate your foes. Otherwise it’ll be a trip to
    gameover land for you
    *Now what’s good fantasy game without some barrels to smash?! Go ahead and
    “smash barrel 1” and “smash barrel 2”. This will reveal some needed armor
    *Next “grab helmet” and then “grab shield”. You’re going to need those for
    the next monster fight!
    *Now it’s time to enter the second to last room! You’re nearly there! “Go east”

    Armory:
    *Big tough monster fight here! Animated Armor attacks you but with your
    weapons and newly acquired armor in tow it’s no match for you!
    *Once you defeat the Animated Armor go ahead and pick up it’s corpse and put
    it on “grab armor suit”
    *Now, it’s time to face the music, the end is just up ahead “go south”

    End Room:
    *Congratulations, if you’ve followed the guide you’ll be treated to the tale
    of your heroic battle against a Lich and the subsequent end of the game!

    """
