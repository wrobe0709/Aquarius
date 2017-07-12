"""Constants docstring"""
ROOMS = {
    'Dungeon Entrance': {
        'long_description': 'long description of the dungeon entrance',
        'short_description': 'short description of the dungeon entrance',
        'north':None,
        'south':None,
        'east':'Southeast Corridor',
        'west':'Southwest Corridor',
        'features':{
            'Chair':{
                'name':'Chair',
                'description':'the description of a chair'
            },
            'Mirror':{
                'name':'Mirror',
                'description':'the description of a mirror'
            },
        },
        'items':{
            'Torch':{
                'name':'Torch',
                'description':'Illuminates Areas'
            }
        }
    },
    'Southeast Corridor': {
        'long_description': 'long description of the southeast corridor',
        'short_description': 'short description of the southeast corridor',
        'north':'Great Hall',
        'south':None,
        'east':'Alcove',
        'west':'Dungeon Entrance',
        'features':{
            'Chair':{
                'name':'Chair',
                'description':'the description of a chair'
            },
            'Mirror':{
                'name':'Mirror',
                'description':'the description of a mirror'
            },
        },
        'items':{}
    },
    'Southwest Corridor': {
        'long_description': 'long description of the southwest corridor',
        'short_description': 'short description of the southwest corridor',
        'north':'Barrel Room',
        'south':None,
        'east':'Dungeon Entrance',
        'west':None,
        'features':{
            'Chair':{
                'name':'Chair',
                'description':'the description of a chair'
            },
            'Mirror':{
                'name':'Mirror',
                'description':'the description of a mirror'
            },
        },
        'items':{}
    },
    'Alcove': {
        'long_description': 'long description of the alcove',
        'short_description': 'short description of the alcove',
        'north':None,
        'south':None,
        'east':None,
        'west':'Southeast Corridor',
        'features':{
            'Chair':{
                'name':'Chair',
                'description':'the description of a chair'
            },
            'Mirror':{
                'name':'Mirror',
                'description':'the description of a mirror'
            },
        },
        'items':{
            'Sword':{
                'name':'Sword',
                'description':'Used for fighting'
            }
        }
    },
    'Great Hall': {
        'long_description': 'long description of the great hall',
        'short_description': 'short description of the great hall',
        'north':'Torch Corridor',
        'south':'Southwest Corridor',
        'east':None,
        'west':None,
        'features':{
            'Chair':{
                'name':'Chair',
                'description':'the description of a chair'
            },
            'Mirror':{
                'name':'Mirror',
                'description':'the description of a mirror'
            },
        },
        'items':{}
    },
    'Torch Corridor': {
        'long_description': 'long description of the torch corridor',
        'short_description': 'short description of the torch corridor',
        'north':'Northeast Corridor',
        'south':'Great Hall',
        'east':'Gaseous Room',
        'west':None,
        'features':{
            'Chair':{
                'name':'Chair',
                'description':'the description of a chair'
            },
            'Mirror':{
                'name':'Mirror',
                'description':'the description of a mirror'
            },
        },
        'items':{}
    },
    'Gaseous Room': {
        'long_description': 'long description of the gaseous room',
        'short_description': 'short description of the gaseous room',
        'north':None,
        'south':None,
        'east':None,
        'west':'Torch Corridor',
        'features':{
            'Chair':{
                'name':'Chair',
                'description':'the description of a chair'
            },
            'Mirror':{
                'name':'Mirror',
                'description':'the description of a mirror'
            },
        },
        'items':{
            'End Room Key':{
                'name':'End Room Key',
                'description':'Unlocks End Room from Armory'
            }
        }
    },
    'Northeast Corridor': {
        'long_description': 'long description of the northeast corridor',
        'short_description': 'short description of the northeast corridor',
        'north':None,
        'south':'Torch Corridor',
        'east':None,
        'west':'Shadow Corridor',
        'features':{
            'Chair':{
                'name':'Chair',
                'description':'the description of a chair'
            },
            'Mirror':{
                'name':'Mirror',
                'description':'the description of a mirror'
            },
        },
        'items':{
            'Helmet':{
                'name':'Helmet',
                'description':'Protects the character'
            }
        }
    },
    'Shadow Corridor': {
        'long_description': 'long description of the shadow corridor',
        'short_description': 'short description of the shadow corridor',
        'north':None,
        'south':'Gear Room',
        'east':'Northeast Corridor',
        'west':'Northwest Corridor',
        'features':{
            'Chair':{
                'name':'Chair',
                'description':'the description of a chair'
            },
            'Mirror':{
                'name':'Mirror',
                'description':'the description of a mirror'
            },
        },
        'items':{}
    },
    'Gear Room': {
        'long_description': 'long description of the gear room',
        'short_description': 'short description of the gear room',
        'north':'Shadow Corridor',
        'south':'Bow Room',
        'east':None,
        'west':'Diamond Room',
        'features':{
            'Chair':{
                'name':'Chair',
                'description':'the description of a chair'
            },
            'Mirror':{
                'name':'Mirror',
                'description':'the description of a mirror'
            },
        },
        'items':{}
    },
    'Northwest Corridor': {
        'long_description': 'long description of the northwest corridor',
        'short_description': 'short description of the northwest corridor',
        'north':None,
        'south':'Diamond Room',
        'east':'Shadow Corridor',
        'west':None,
        'features':{
            'Chair':{
                'name':'Chair',
                'description':'the description of a chair'
            },
            'Mirror':{
                'name':'Mirror',
                'description':'the description of a mirror'
            },
        },
        'items':{
            'Shield':{
                'name':'Shield',
                'description':'Protects the character'
            }
        }
    },
    'Diamond Room': {
        'long_description': 'long description of the diamond room',
        'short_description': 'short description of the diamond room',
        'north':'Northwest Corridor',
        'south':'Barrel Room',
        'east':'Gear Room',
        'west':None,
        'features':{
            'Chair':{
                'name':'Chair',
                'description':'the description of a chair'
            },
            'Mirror':{
                'name':'Mirror',
                'description':'the description of a mirror'
            },
        },
        'items':{}
    },
    'Bow Room': {
        'long_description': 'long description of the bow room',
        'short_description': 'short description of the bow room',
        'north':'Gear Room',
        'south':None,
        'east':None,
        'west':None,
        'features':{
            'Chair':{
                'name':'Chair',
                'description':'the description of a chair'
            },
            'Mirror':{
                'name':'Mirror',
                'description':'the description of a mirror'
            },
        },
        'items':{
            'Bow':{
                'name':'Bow',
                'description':'Shoots an arrow'
            }
        }
    },
    'Armory': {
        'long_description': 'long description of the armory',
        'short_description': 'short description of the armory',
        'north':None,
        'south':'End Room',
        'east':None,
        'west':'Barrel Room',
        'features':{
            'Chair':{
                'name':'Chair',
                'description':'the description of a chair'
            },
            'Mirror':{
                'name':'Mirror',
                'description':'the description of a mirror'
            },
        },
        'items':{
            'Armor Suit':{
                'name':'Armor Suit',
                'description':'Protects the character'
            }
        }
    },
    'Barrel Room': {
        'long_description': 'long description of the barrel room',
        'short_description': 'short description of the barrel room',
        'north':'Diamond Room',
        'south':'Southwest Corridor',
        'east':'Armory',
        'west':None,
        'features':{
            'Chair':{
                'name':'Chair',
                'description':'the description of a chair'
            },
            'Mirror':{
                'name':'Mirror',
                'description':'the description of a mirror'
            },
        },
        'items':{
            'Rune':{
                'name':'Rune',
                'description':'Upgrades the hero\'s sword'
            }
        }
    },
    'End Room': {
        'long_description': 'long description of the end room',
        'short_description': 'short description of the end room',
        'north':'Armory',
        'south':None,
        'east':None,
        'west':None,
        'features':{
            'Chair':{
                'name':'Chair',
                'description':'the description of a chair'
            },
            'Mirror':{
                'name':'Mirror',
                'description':'the description of a mirror'
            },
        },
        'items':{}
    },
}
