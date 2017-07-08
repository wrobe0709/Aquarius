"""Aquarius docstring"""
import Room.Room

def main():
    """Execution of Aquarius Game"""
    current_room = Room.Room.CurrentRoom()
    current_room.set_name('Start Room')
    current_room.set_description('This is the starting room.')

    usr_input = ''
    
    while usr_input != '/quit':
        usr_input = raw_input('Enter room to look into (N,S,E,W) > ')
        if usr_input == 'N':
            north_room = Room.Room.Neighbor()
            north_room.set_name('North Room')
            north_room.set_far_off_description('cannot see anything through the gaseous haze...')
            current_room.set_north(north_room)
            print "From", current_room.get_name(), "Looking into", north_room.get_name(), "the player", current_room.north.get_far_off_description()
        elif usr_input == 'S':
            south_room = Room.Room.Neighbor()
            south_room.set_name('South Room')
            south_room.set_far_off_description('is able to see a wooden chest at the far end of the room...')
            current_room.set_south(south_room)
            print "From", current_room.get_name(), "Looking into", south_room.get_name(), "the player", current_room.south.get_far_off_description()
        elif usr_input == 'E':
            east_room = Room.Room.Neighbor()
            east_room.set_name('East Room')
            east_room.set_far_off_description('can see a sword hanging on the wall...')
            current_room.set_east(east_room)
            print "From", current_room.get_name(), "Looking into", east_room.get_name(), "the player", current_room.east.get_far_off_description()
        elif usr_input == 'W':
            west_room = Room.Room.Neighbor()
            west_room.set_name('West Room')
            west_room.set_far_off_description('sees a bow hanging on a closet door...')
            current_room.set_west(west_room)
            print "From", current_room.get_name(), "Looking into", west_room.get_name(), "the player", current_room.west.get_far_off_description()

if __name__ == '__main__':
    main()
