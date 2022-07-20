"""
Linked List Example: Auto mobile accidents
Author: Samuel Casellas
"""

from linked_list import LinkedList
from linked_list_dependencies import *

AUTO_FILE_NAME = "auto_accidents.csv"

def main() -> None:
    """Linked lists are good when you need to pull from a long list of data one line at a time.
    Used perf_counter to compare the run times for list and linked list.
    """
    make_auto_accidents_sample(AUTO_FILE_NAME)
    car_data_linked_list, car_data_list = read_auto_accidents(AUTO_FILE_NAME)
    while True:
        input("Hit enter for next car accident LINKED...")
        start_timer = perf_counter()
        print(car_data_linked_list.remove_and_return_head())
        stop_timer = perf_counter()
        print(f"Linked list took {(stop_timer - start_timer) * 1000:.6f} second(s)")
        input("Hit enter for next car accident LIST...")
        start_timer = perf_counter()
        print(car_data_list.pop(0))
        stop_timer = perf_counter()
        print(f"Normal list took {(stop_timer - start_timer) * 1000:.6f} second(s)")

def read_auto_accidents(file_name, link_list_class=LinkedList) -> Tuple[LinkedList, list]:
    """Read each accident into a list, sort them by date,
    then add each to a linked list to return (as well as a list for time comparing)
    """
    linked_list = link_list_class()
    list_of_accidents = list()
    with open(file_name, mode="r") as read_file:
        csv_reader = reader(read_file, delimiter=",")
        for i, row in enumerate(csv_reader):
            # Do not add the header
            if i != 0:
                list_of_accidents.append(row)
    
        # Sort the accidents from earliest to latest.
        list_of_accidents = sorted(
        list_of_accidents, key=lambda data: 
                               data[0].replace("/", ""))
        for data in list_of_accidents:
            linked_list.add_tail(data)

        return (linked_list, list_of_accidents)
    
def make_auto_accidents_sample(file_name) -> None:
    """Checks to see if the file sample already exists,
    create it if not.
    """
    if not file_sample_exists(file_name):
        with open(path.join(getcwd(), file_name), mode="w", newline="") as write_file:
            csv_writer = writer(write_file)
            header = ["accident date", "# of fatalities"]
            csv_writer.writerow(header)
            for _ in range(100000):
                line = [
                    "{}/{}/{}".format(
                                randint(2000, 2022),
                                str(randint(1,12)).rjust(2, '0'),
                                str(randint(1,28)).rjust(2, '0'),
                                ),
                    "{}".format(randint(1, 5))
                ]
                csv_writer.writerow(line)

if __name__ == "__main__":
    main()
