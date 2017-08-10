"""This file will handle the battle related functions"""
import helpers
from companionText import *

# Handles battles with monsters
def battle(room, character):
    """Handle battles"""
    # Check if the room has a monster and only attack if the monster has not been defeated
    current_room_monster = room.get_monsters()
    if current_room_monster:
        if 'Armored Skeleton' in current_room_monster:
            if not current_room_monster['Armored Skeleton'].get_defeated_status():
                print " The Armored Skeleton attacks!"
                if 'Sword' and 'Bow' in character.get_inventory():
                    print "You pull out your bow and quickly fire off an arrow at the Armored Skeleton, loosening its armor."
                    print "As it draws near you switch to your sword and cut it down where your arrows loosened the armor."
                    current_room_monster['Armored Skeleton'].set_defeated_status(True)
                else:
                    print "You flail helplessly against the might of the Armored Skeleton. As it closes in on you its"
                    print "large broadsword is swung down and cleaves you in two."
                    print "\n"
                    print "\n"
                    helpers.play_game()
        elif 'Animated Armor' in current_room_monster:
            if not current_room_monster['Animated Armor'].get_defeated_status():
                print "The Animated Armor attacks!"
                if 'Sword' and 'Helmet' and 'Shield' in character.get_inventory():
                    print "You battle relentlessly, pounding away at the Animated Armor. Landing blow after blow with"
                    print "your sword and taking hits, but your helm and sheild hold up against the Armor until you finally vanquish it."
                    current_room_monster['Animated Armor'].set_defeated_status(True)
                else:
                    print "You charge at the Animated Armor and strike it. You immediately realize the mistake you've made"
                    print "by coming unprepared. The Armor reaches down and grabs you with its metal gauntlets, crushing your unprotected skull."
                    print "\n"
                    print "\n"
                    helpers.play_game()
        elif 'Skeleton' in current_room_monster:
            if not current_room_monster['Skeleton'].get_defeated_status():
                print " The Skeleton attacks!"
                if 'Sword' in character.get_inventory():
                    print " As the Skeleton lunges you deftly pull out your sword and decimate its feable undeath."
                    current_room_monster['Skeleton'].set_defeated_status(True)
                else:
                    print "The Skeleton lunges at you and catches you entirely off guard. It sinks its dagger into you"
                    print "while its bones chatter away and its empty sockets look at you, you descend into oblivion."
                    print "\n"
                    print "\n"
                    helpers.play_game()
        elif 'Lich' in current_room_monster:
            if not current_room_monster['Lich'].get_defeated_status():
                print "The Lich attacks!"
                if 'Sword' and 'Armor Suit' in character.get_inventory():
                    print '''The final battle is upon you! With your trusty sword at your side and the powerful armor
                    for protection against the Lich's malignant spells, you boldly draw your sword and charge the Lich.
                    It summons a skeletal minion which you easily crush. Side-stepping its ashy ruins you leap and deliver
                    a devastating blow against the Lich. As your sword penatrates its etheral form it screams in agony!
                    A burst of light fills the room and the darkness of the Lich condenses into an orb and vanishes.
                    You slowly raise yourself off the ground and stand -- VICTORIUS.'''
                    current_room_monster['Lich'].set_defeated_status(True)
                    game_conclusion()
                else:
                    print '''You've gotten so far, but your ambition has gotten the best of you. The Lich summons a ball of magic
                    from its staff, points it at you, and then a stream of dark malignant energy races towards you. It
                    splashes against your frail armor, immediately disintergrating it and then you feel it. The cold
                    expanse of the void. Your eyes grow wide with fear as the Lich's eyes burn with a mix of delight and
                    hate. As your senses begin to fail you just barely see the Lich's skeletal mouth moving, an incantation?
                    You crumple to the ground, your final breath leaves your body and you die...And then you rise up off the
                    ground, as you rise your flesh and innards dissapte into dust as the Lich's newest champion bows to its master!'''
                    print "\n"
                    print "\n"
                    helpers.play_game()
