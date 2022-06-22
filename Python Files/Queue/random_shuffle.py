"""
Random Shuffle 

"""

import random
from queue_class import Queue

SONGS_PATH = "Other Files/queue_example_songs.txt"

def main():
    songs = read_songs_into_list()
    last_song_index = len(songs) - 1
    songs_recently_played = Queue(limit=20,shift_when_full=True)
    # main loop
    while True:
        chosen_unique_song = songs[random.randint(0, last_song_index)]
        while chosen_unique_song in songs_recently_played:
            chosen_unique_song = songs[random.randint(0, last_song_index)]
        songs_recently_played.queue(chosen_unique_song)
        print(chosen_unique_song)
        if input("Hit Enter for next song...") == "\x1b[C":
            raise Exception
        

def read_songs_into_list():
    with open(SONGS_PATH, mode="r") as read_file:
        return read_file.readlines()

# def write_song_names_for_examples():
#     with open(SONGS_PATH, mode="w") as write_file:
#         for i in range (1,51):
#             write_file.write(f"Song #{i}\n")

if __name__ == "__main__":
    main()