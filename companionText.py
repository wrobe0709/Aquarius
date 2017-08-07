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
    to check out your surroundings while looking for a way out."""

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
    print "Work in progress, check back soon."
