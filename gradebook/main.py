"""Main application.
"""
__author__ = "Ram Basnet"

import os
import time
from python import db


def setup_database(db_file):
    """TODO: Write all your code to setup database.
    """
    print('seting up database...')
    sql = """CREATE TABLE IF NOT EXISTS Students (
            student_id INTEGER PRIMARY KEY
            )
        """
    db.create_table(db_file, sql)
    time.sleep(2)


def show_menu():
    """Displays menu."""
    text = """
    A+ Grade Book
    =============

    Select one of the following menu options:
    1. Setup Database
    2. Add a new student
    3. Exit the program
    """
    print(text)
    option = input('Enter an option: [1-3]: ')
    while True:
        if option.isdecimal():
            option = int(option)
            if 1 <= option <= 3:
                return int(option)
        os.system('clear')
        option = input("Enter a valid option: ")


def main():
    """Main function.
    """
    db_file = "gradebook.sqlite"
    while True:
        option = show_menu()
        if option == 3:
            exit(0)
        elif option == 1:
            setup_database(db_file)
            os.system('clear')


if __name__ == "__main__":
    main()
