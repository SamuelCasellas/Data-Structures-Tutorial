"""
Bank Transaction Solution
Author: Samuel Casellas
"""

from linked_list_solution import LinkedList
from linked_list_dependencies import *
from auto_accidents import read_auto_accidents as read_bank_transactions

BANK_TRANSACTION_FILE_NAME = "bank_transactions.csv"

def main() -> None:
    make_bank_transactions_sample(BANK_TRANSACTION_FILE_NAME)
    
    # As required, unpack the list as "_", for it will not be used here.
    # Hypothesis of the efficiency of linked lists over lists already confirmed in example.
    bank_transactions_linked_list, _ = read_bank_transactions(BANK_TRANSACTION_FILE_NAME, link_list_class=LinkedList)
    missing_transaction = "y"
    while missing_transaction == "y":
        print("\nCurrent bank transactions sorted by date:")
        total_money_spent = 0
        for transaction in bank_transactions_linked_list:
            print("Date: {}, Money Spent: {}".format(
                transaction[0],
                transaction[1]
            ))

            # Remove the $ sign in order to add the values
            total_money_spent += int(transaction[1][1:])
        print("Total money spent: ${}".format(total_money_spent))
        missing_transaction = input("Missing transaction? (y/n) ").lower()
        if missing_transaction == "y":
            new_transaction = input(
            "Enter date and money (Follow this format: \"2012/04/22 $5\") ").split(" ")
            bank_transactions_linked_list.insert_data_ordered(new_transaction, index=0, replace_seq="/")
            print("Transaction successfully added.")
    

def make_bank_transactions_sample(file_name) -> None:
    """Checks to see if the file sample already exists,
    create it if not.
    """
    if not file_sample_exists(file_name):
        with open(path.join(getcwd(), file_name), mode="w", newline="") as write_file:
            csv_writer = writer(write_file)
            header = ["transaction date", "$ spent"]
            csv_writer.writerow(header)
            for _ in range(3):
                line = [
                    "{}/{}/{}".format(
                                randint(2020, 2022),
                                str(randint(1,12)).rjust(2, "0"),
                                str(randint(1,28)).rjust(2, "0"),
                                ),
                    "${}".format(randint(1, 1000))
                ]
                csv_writer.writerow(line)

if __name__ == "__main__":
    main()