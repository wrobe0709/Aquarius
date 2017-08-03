"""This file will handle the battle related functions"""
import json
import Room.Room as Room
import Character.Character as Character
import Feature.Feature as Feature
import Item.Item as Item
import Monster.Monster as Monster


#This function first checks to make sure the room has a monster, then it will
#make sure the monster is not already defeated. Lastly it will compare the items
#in the players inventory to see if they have the requisite ones to defeat the monster
#and will either slay the monster or the player will be defeated
def battle(room):
    current_room_monster = room.get_monsters()
    monster_lvl = getattr(room[current_room_monster].get_lvl())
    print monster_lvl
    if current_room_monster:
        #if room[current_room_monster].get_defeated_status() == False
            print "The monster is attacking!"
            if room[current_room_monster].get_lvl() == '1':
                print "This is a lvl 1 monster"
            elif current_room_monster.get_lvl() == '2':
                print "Now we're talking, lvl 2 monster"
            elif current_room_monster.get_lvl() == '3':
                print "Ok this is serious! Lvl 3 monster!"
            elif current_room_monster.get_lvl() == '4':
                print "O shit, the boss!"
        #else:
            #pass
