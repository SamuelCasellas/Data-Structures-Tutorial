import time
import random
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
            time.sleep(1)
        stepping_queue = Queue()
        for _ in range(num_steps):
            next_step = options[random.randint(0,3)]
            stepping_queue.queue(next_step)
        print("\n"*50)
        tab_count = 0
        for step in stepping_queue:
            print("\t"*tab_count,end="")
            print(step)
            tab_count += 1
            time.sleep(0.25)
            print("\n"*50)
        users_turn = input("Your turn! Use your arrow keys and hit enter...\n")
        # Convert the [LETTER symbols to direction words
        for code, direction in direction_decoder.items():
            users_turn = users_turn.replace(code, direction)
            
        users_steps = users_turn.split(DIRECTION_SYMBOL)[1:]

        miss_count = 0

        for user_step in users_steps:
            # Queue is used here
            correct_step = stepping_queue.deque()
            if correct_step != user_step:
                miss_count += 1

        difference = num_steps - len(users_steps)
        for _ in range(difference):
            miss_count += 1

        if miss_count == 0:
            play_again = input("\nYou got it!\n\nPlay again? (y/n) ").lower()
            num_steps += 1
        else:
            play_again = input(f"\nNot quite! You got {miss_count} wrong.\n\nPlay again? (y/n) ").lower()
    
    print("\nGood game!")

if __name__ == "__main__":
    main()