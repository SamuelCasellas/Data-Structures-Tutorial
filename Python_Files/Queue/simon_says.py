"""
Queue Example: "Simon Says"
Author: Samuel Casellas
"""


from time import sleep
from random import randint
from queue_class import Queue

def main():

    DIRECTION_SYMBOL = "\x1b"

    direction_decoder = {
        "[D": "LEFT",
        "[C": "RIGHT",
        "[A": "UP",
        "[B": "DOWN"
    }

    options = ("LEFT", "RIGHT", "UP", "DOWN")

    print("\n"*50)
    print("Welcome to Simon Says!\n")
    play_again = "y"
    num_steps = 3
    while play_again == "y":
        print("Follow my lead.")

        # Countdown
        for i in range(5, 0, -1):
            print(i)
            sleep(1)

        # Print the steps to follow while marking them down
        stepping_queue = Queue()
        print("\n"*50)
        tab_count = 0
        for _ in range(num_steps):
            next_step = options[randint(0,3)]
            stepping_queue.enqueue(next_step)
            print("\t"*tab_count,end="")
            print(next_step)
            tab_count += 1
            sleep(0.5)
            print("\n"*50)

        # Get user input
        users_turn = input("Your turn! Use your arrow keys and hit enter...\n")

        # Convert the [LETTER symbols to direction words
        for code, direction in direction_decoder.items():
            users_turn = users_turn.replace(code, direction)
        
        # Create ordered list for each user step 
        users_steps = users_turn.split(DIRECTION_SYMBOL)[1:]

        # Compare the input to the correct order
        miss_count = 0
        for user_step in users_steps:
            # Queue is used here
            correct_step = stepping_queue.deque()
            if correct_step != user_step:
                miss_count += 1

        # Determine any missing steps and account for them
        # Using a for loop ensures to only increment misses 
        # for missing user steps compared to solution
        # (Additional Steps were already accounted for)
        difference = num_steps - len(users_steps)
        for _ in range(difference):
            miss_count += 1

        # Feedback and ask for retry
        if miss_count == 0:
            play_again = input("\nYou got it!\n\nPlay again? (y/n) ").lower()
            num_steps += 1
        else:
            play_again = input(f"\nNot quite! You got {miss_count} wrong.\n\nPlay again? (y/n) ").lower()
    
    # End game
    print("\nGood game!\n")

if __name__ == "__main__":
    main()