"""
BST Example: Hotels
Author: Samuel Casellas
"""
from tree import *
from random import randint

def main() -> None:
    total_num_rooms = 250
    reserved_hotels = set()

    # Generate 50 occupied rooms at random.
    for _ in range(50):
        room_num = randint(1, total_num_rooms)
        while room_num in reserved_hotels:
            room_num = randint(1, total_num_rooms)
        reserved_hotels.add(room_num)

    hotel_rooms_tree = create_balanced_bst(list(reserved_hotels))
    
    # Ask for room requested and see if it's available. 
    requested_room = int(input(f"\nWelcome to our hotel. This hotel has {total_num_rooms} rooms.\n\
Which room would you like to reserve? "))
    while hotel_rooms_tree.contains_target(requested_room):
        requested_room = int(input(f"\nRoom #{requested_room} is taken!\n\
Which room would you like to reserve? "))

    hotel_rooms_tree.insert_data(requested_room)
    print(f"\nRoom #{requested_room} has now been reserved. \n\
Enjoy your stay!")
        

if __name__ == "__main__":
    main()