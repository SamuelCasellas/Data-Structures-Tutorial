from os import path, getcwd, chdir, listdir
from platform import system
from csv import reader, writer
from typing import Tuple
from random import randint
from time import perf_counter

def file_sample_exists(file_name) -> bool:
    switch_to_parent_dir_of_file()
    return path.exists(file_name)

def switch_to_parent_dir_of_file() -> None:
    current_path = getcwd()

    # Confirm which OS
    if system() == "Windows":
        curr_dir = current_path.split("\\")[-1]
    else:
        curr_dir = current_path.split("/")[-1]

    # cd out to correct dir if needed.
    backtrack = 0
    if curr_dir == "Python_Files":
        backtrack = 1
    elif curr_dir == "Linked_List":
        backtrack = 2

    for _ in range(backtrack):
        chdir("..")

    chdir("Other_Files")