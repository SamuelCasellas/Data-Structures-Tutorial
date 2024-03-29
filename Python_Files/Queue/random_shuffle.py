"""
Random Shuffle Solution
Author: Samuel Casellas
"""

from random import randint
from queue_class_solution import Queue

SONGS_PATH = "Other_Files/queue_example_songs.txt"

def main():
    songs = read_songs_into_list()
    last_song_index = len(songs) - 1
    songs_recently_played = Queue(limit=20,shift_when_full=True)

    # main loop
    while True:
        chosen_unique_song = songs[randint(0, last_song_index)]
        while chosen_unique_song in songs_recently_played:
            # This song has been played recently! Pick another...
            chosen_unique_song = songs[randint(0, last_song_index)]
        # If you look inside enqueue, you can see logic that handles
        # automatically dequeueing when the queue reaches the set limit!
        songs_recently_played.enqueue(chosen_unique_song)
        print(chosen_unique_song)
        input("Hit Enter for next song...")
        

def read_songs_into_list():
    with open(SONGS_PATH, mode="r") as read_file:
        return read_file.readlines()

# Used to create the random song file
# 
# def write_song_names_for_examples():
#     with open(SONGS_PATH, mode="w") as write_file:
#         for i in range (1,51):
#             write_file.write(f"Song #{i}\n")

if __name__ == "__main__":
    main()