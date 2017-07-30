"""This file will handle the battle related functions"""
import json
import Room.Room as Room
import Character.Character as Character
import Feature.Feature as Feature
import Item.Item as Item


#This function first checks to make sure the room has a monster, then it will
#make sure the monster is not already defeated. Lastly it will compare the items
#in the players inventory to see if they have the requisite ones to defeat the monster
#and will either slay the monster or the player will be defeated
#def battle(character, room);
    #if
