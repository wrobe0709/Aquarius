"""Constants docstring"""
import json

def get_room_json(room):
    """Get json data for a specific room"""
    room_dict = {}
    with open('Constants/' + room + '.json') as json_data:
        room_data = json.load(json_data)
        room_dict['long_description'] = room_data['long_description']
        room_dict['short_description'] = room_data['short_description']
        room_dict['north'] = room_data['north']
        room_dict['south'] = room_data['south']
        room_dict['east'] = room_data['east']
        room_dict['west'] = room_data['west']
        room_dict['locked'] = room_data['locked']
        room_dict['features'] = room_data['features']
        room_dict['items'] = room_data['items']
        return room_dict

ROOMS = {
    'Dungeon Entrance': get_room_json('dungeon_entrance'),
    'Southeast Corridor': get_room_json('southeast_corridor'),
    'Southwest Corridor': get_room_json('southwest_corridor'),
    'Alcove': get_room_json('alcove'),
    'Great Hall': get_room_json('great_hall'),
    'Torch Corridor': get_room_json('torch_corridor'),
    'Gaseous Room': get_room_json('gaseous_room'),
    'Northeast Corridor': get_room_json('northeast_corridor'),
    'Shadow Corridor': get_room_json('shadow_corridor'),
    'Gear Room': get_room_json('gear_room'),
    'Northwest Corridor': get_room_json('northwest_corridor'),
    'Diamond Room': get_room_json('diamond_room'),
    'Bow Room': get_room_json('bow_room'),
    'Armory': get_room_json('armory'),
    'Barrel Room': get_room_json('barrel_room'),
    'End Room': get_room_json('end_room')
}
