"""Constants docstring"""
ROOMS = {
    'Dungeon Entrance': {
        'long_description': 'There is not much too this room. To the east there is a wooden door without a lock. To the west there is another wooden door, however, this door is locked. The lock on the western door is silver. On the north wall there is a closet.',
        'short_description': 'There is an unlocked door the to the east, a locked door to the west, and a closet on the north wall.',
        'north':None,
        'south':None,
        'east':'Southeast Corridor',
        'west':'Southwest Corridor'
    },
    'Southeast Corridor': {
        'long_description': 'a very long description',
        'short_description': 'a shorter one',
        'north':None,
        'south':None,
        'east':None,
        'west':'Dungeon Entrance'
    },
    'Southwest Corridor': {
        'long_description': 'a very long description',
        'short_description': 'a shorter one',
        'north':None,
        'south':None,
        'east':'Dungeon Entrance',
        'west':None
    },
}