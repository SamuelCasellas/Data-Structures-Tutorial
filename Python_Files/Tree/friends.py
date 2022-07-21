"""
Friends Solution
Author: Samuel Casellas
"""
from tree_solution import *

def main() -> None:
    
    friends_tree = create_balanced_bst(read_names())

    requested_name = input(
    "\nWhat is the name of the friend you are looking for? ")

    if friends_tree.contains_target(requested_name):
        print()
        print(requested_name, "is in your friends list.")
    else:
        print()
        print(requested_name, "was not found in your friends list.")
        if input("Would you like to see who is in your friend list? (y/n) ") == "y":
            print("\nHere is your friends list")
            for name in friends_tree:
                print(name)

    print(f"\nYou currenly have {len(friends_tree)} friend(s).\n")

def read_names() -> list:
    with open("Other_Files/friends_examples.txt", mode="r") as read_file:
        return [name.strip() for name in read_file.readlines()]

if __name__ == "__main__":
    main()