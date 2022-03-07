'''
Provides a basic frontend
from Assignment 2 modified for Assignment 5

https://github.com/uw-continuum/python-320-assignment-02-smichalove
'''
import sys
import main
import user_status
import users
from datetime import datetime
import logging
import sys
import main
import user_status
import users
import logger
from loguru import logger

date_log = datetime.now().strftime('log_%m_%d-%Y.log')
logger.add(sys.stderr, level="DEBUG")
logger.add(sys.stderr, level="ERROR")
logger.add(date_log, level="DEBUG")
logger.add(date_log, level="ERROR")
logger.add(sys.stderr, level="WARNING")
logger.add(f"{date_log}", encoding="utf8")
logger.debug(f"logging to {date_log}" )
logger.add(sys.stderr, format="{message}",  level="DEBUG")
#logger.add(sys.stdout, colorize=True, format="<green>{time}</green> <level>{message}</level>")
logger.add(sys.stderr, format="{message}",  level="ERROR")
#logger.add(f"{date}",level="DEBUG")
logger.enable("charger")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)  # Add this line
#logger.add(sys.stderr, level="DEBUG")
logger = logging.getLogger()
#logger.add(sys.stderr, format=log_format)



    #
def load_users():
    '''
    Loads user accounts from a file
    '''
    filename = input('Enter filename of user file: ')
    main.load_users(filename, user_collection)
#

def load_status_updates():
    '''
    Loads status updates from a file
    '''
    filename = input('Enter filename for status file: ')

    main.load_status_updates(filename, status_collection)
    results = main.load_status_updates(filename, status_collection)
    logger.debug(f"menu.py load {results} {filename}")

def add_user():
    '''
    Adds a new user into the database
    '''
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    if not main.add_user(user_id,
                         email,
                         user_name,
                         user_last_name,
                         user_collection):
        print("An error occurred while trying to add new user")
    else:
        print("User was successfully added")


def update_user():
    '''
    Updates information for an existing user
    '''
    user_id = input('User ID: ')
    email = input('User email: ')
    user_name = input('User name: ')
    user_last_name = input('User last name: ')
    if not main.update_user(user_id, email, user_name, user_last_name, user_collection):
        print("An error occurred while trying to update user")
    else:
        print("User was successfully updated")


def search_user():
    '''
    Searches a user in the database
    '''
    user_id = input('Enter user ID to search: ')
    logger.debug(f"menu.py search_users {user_id}")
    result = main.search_user(user_id, user_collection)
    logger.debug(f"result::{result}")
    if result is None:
        print("ERROR: User does not exist")
    else:
       
        print(f"User ID: {result['user_id']}")
        print(f"Email: {result['email']}")
        print(f"Name: {result['user_name']}")
        print(f"Last name: {result['user_last_name']}")


def delete_user():
    '''
    Deletes user from the database
    '''
    user_id = input('User ID: ')
    if not main.delete_user(user_id, user_collection):
        print("An error occurred while trying to delete user")
    else:
        print("User was successfully deleted")


def save_users():
    '''
    Saves user database into a file
    '''
    filename = input('Enter filename for users file: ')
    main.save_users(filename, user_collection)


def add_status():
    '''
    Adds a new status into the database
    '''
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')
    if not main.add_status(status_id, user_id, status_text, status_collection):
        print("An error occurred while trying to add new status")
    else:
        print("New status was successfully added")


def update_status():
    '''
    Updates information for an existing status
    '''
    user_id = input('User ID: ')
    status_id = input('Status ID: ')
    status_text = input('Status text: ')
    logger.debug(f"{user_id} --> {status_id} --> {status_text}")
    if not main.update_status(status_id, user_id, status_text, status_collection):
        logger.debug(f"{user_id} --> {status_id} --> {status_text} NOT FOUND")
        print("An error occurred while trying to update status")
    else:
        logger.debug(f"{user_id} --> {status_id} --> {status_text} updated!")
        print("Status was successfully updated")



def search_status():
    '''
    Searches a status in the database
    '''
    try:
        status_id = input('Enter status ID to search: ')
        result = main.search_status(status_id,status_collection)
       
        if result is None:
            print("ERROR: Status does not exist")
 
        else:
            
            print(f"User ID: {result['user_id']}")
            print(f"Status ID: {result['status_id']}")
            print(f"Status text: {result['status_text']}")
           
    except AttributeError:
        logger.error(f"AttributeError:::: {status_id}")
        logger.debug(f"status result result::{result}")
        logger.debug(f"AttributeError:{result}")


def delete_status():
    '''
    Deletes status from the database
    '''
    status_id = input('Status ID: ')
    if not main.delete_status(status_id, status_collection):
        print("An error occurred while trying to delete status")
    else:
        print("Status was successfully deleted")


def save_status():
    '''
    Saves status database into a file
    '''
    filename = input('Enter filename for status file: ')
    main.save_status_updates(filename, status_collection)


def quit_program():
    '''
    Quits program
    '''
    sys.exit()


if __name__ == '__main__':

    user_collection = main.init_user_collection()
    status_collection = main.init_status_collection() # init_status_collection()
    menu_options = {
        'A': load_users,
        'B': load_status_updates,
        'C': add_user,
        'D': update_user,
        'E': search_user,
        'F': delete_user,
        'G': save_users,
        'H': add_status,
        'I': update_status,
        'J': search_status,
        'K': delete_status,
        'L': save_status,
        'Q': quit_program
    }
    while True:
        user_selection = input("""
                            A: Load user database
                            B: Load status database
                            C: Add user
                            D: Update user
                            E: Search user
                            F: Delete user
                            G: Save user database to file
                            H: Add status
                            I: Update status
                            J: Search status
                            K: Delete status
                            L: Save status database to file
                            Q: Quit

                            Please enter your choice: """)
        if user_selection.upper() in menu_options:
            menu_options[user_selection.upper()]()
        else:
            print("Invalid option")
            