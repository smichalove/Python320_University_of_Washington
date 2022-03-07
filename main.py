#!/usr/bin/env python3
"""
main driver for a simple social network project
https://github.com/uw-continuum/python-320-assignment-05-smichalove

user.py functions:
    def __init__(self, user_id, email, user_name, user_last_name):
    def __init__(self):
    def add_user(self, user_id, email, user_name, user_last_name):
    def modify_user(self, user_id, email, user_name, user_last_name):
    def delete_user(self, user_id):
    def search_user(self, user_id):

user_status.py functions

    def __init__(self, status_id, user_id, status_text):
    def __init__(self):
    def add_status(self, status_id, user_id, status_text):
    def modify_status(self, status_id, user_id, status_text):
    def delete_status(self, status_id):
    def search_status(self, status_id):



"""
# pylint: disable=R0903
# pylint: disable=C0116,C0103,W1514,C0303,W0105,R1705,C0413,W0611,C0413,W0621,W0612,C0411,R1703,W0613

from pathlib import Path
import csv
import pathlib
import user_status
import users
user_header =[]
import pymongo
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import pandas as pd


def init_user_collection():
    '''
    Creates and returns a new instance of UserCollection
    '''
    return users.UserCollection()
    


def init_status_collection():
    """

    Creates and returns a new instance of UserStatusCollection
    UserStatusCollection()
    """


    return user_status.UserStatusCollection()
    


def load_users(filename, user_collection):
    """
    Opens a CSV file with user data and
    adds it to an existing instance of
    UserCollection

    Requirements:
    - If a user_id already exists, it
    will ignore it and continue to the
    next.
    - Returns False if there are any errors
    (such as empty fields in the source CSV file)
    - Otherwise, it returns True.
    USER_ID,EMAIL,NAME,LASTNAME
    """

    user_header = ["USER_ID", "EMAIL", "NAME", "LASTNAME"]
    cdw = pathlib.Path.cwd()
    print(f"Reading {filename}\npath is {cdw}")
   
    count = 0
    try:
        with open(filename, mode='r', newline='\n') as accountsfile:
            # print(accountsfile)
            reader = csv.reader(accountsfile, delimiter=',')
            user_header = next(reader)
            print("header", user_header)
           

            for row in reader:
                count += 1
                # USER_ID,NAME,LASTNAME,EMAIL (self, user_id, email, user_name, user_last_name)
                # print("row",row[0], row[1], row[2], row[3])
                
                    # print("line",row)
                load = add_user(row[0], row[3], row[1], row[2], user_collection)

            print(f"lines counted {count}")
        accountsfile.close()
        return True


    except FileNotFoundError:
        print(f"ERROR: Couldn't find {filename}")
        print(f"Current path is: {cdw} ")
        return False





def save_users(filename, user_collection):
    """
    Saves all users in user_collection into
    a CSV file

    Requirements:
    - If there is an existing file, it will
    overwrite it.
    - Returns False if there are any errors
    (such as an invalid filename).
    - Otherwise, it returns True.
    """
    cdw = pathlib.Path.cwd()
    print(f"SAVING {filename}\npath is {cdw}")
    
    
    try:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["UserAccounts"]
        # mongo_docs = mydb["Users"]
        usercol = mydb["UserAccounts"]
        mongo_docs = usercol.find({},{"_id":0})
        
        df =  pd.DataFrame(list(mongo_docs))
        df.to_csv(filename, index=False)
        
        return True

    except FileNotFoundError:

        print(f"ERROR: Couldn't find {filename}")
        print(f"Current path is: {cdw} ")
        path = Path(filename)
        print(path)
        return False

    except OSError: 
        return False

def load_status_updates(filename, status_collection):
    """
    Opens a CSV file with status data and adds it to an existing
    instance of UserStatusCollection

    Requirements:
    - If a status_id already exists, it will ignore it and continue to
      the next.
    - Returns False if there are any errors(such as empty fields in the
      source CSV file)
    - Otherwise, it returns True.
    STATUS_ID,USER_ID,STATUS_TEXT
   """
    cdw = pathlib.Path.cwd()
    print(f"Reading {filename}\npath is {cdw}")
    status_header = ["STATUS_ID","USER_ID","STATUS_TEXT"]
    #global tatus_header
    try:
       
        with open(filename, mode='r') as statusfile:
            reader = csv.reader(statusfile, delimiter=',')
            status_header = next(reader)
            count = 0
            print(status_header)
            for line in reader:
                #defadd_status(self, status_id, user_id, status_text):
                
                add_status(line[0], line[1], line[2],status_collection)
                count += 1
                # print("added:",line[0], line[1], line[2])
        statusfile.close()
        print(f'lines counted for Status: {count}')
        return True
    except FileNotFoundError:
        print(f"ERROR: Couldn't find {filename}")
        print(f"Current path is: {cdw} ")

        return False

def save_status_updates(filename, status_collection):
    """
    Saves all statuses in status_collection into a CSV file

    Requirements:
    - If there is an existing file, it will overwrite it.
    - Returns False if there are any errors(such an invalid filename).
    - Otherwise, it returns True.
    """
    try:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["StatusUpdates"]
        # mongo_docs = mydb["Users"]
        usercol = mydb["StatusUpdates"]
        mongo_docs = usercol.find({},{"_id":0})
        
        df =  pd.DataFrame(list(mongo_docs))
        df.to_csv(filename, index=False)
        
        return True

    except OSError: 
        return False





def add_user(user_id, email, user_name, user_last_name, user_collection):
    """add users with users: def add_user(self, user_id, email, user_name, user_last_name):
        Creates a new instance of User and stores it in user_collection
        (which is an instance of UserCollection)
    """
    result = user_collection.add_user(user_id, email, user_name, user_last_name)
    #print(user_id, email, user_name, user_last_name)
    if result:
        
        return True
    else:

        return False


def update_user(user_id, email, user_name, user_last_name, user_collection):
    """
    Updates the values of an existing user

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    def modify_user(self, user_id, email, user_name, user_last_name):
    """
    
    try:
        # user_collection = init_user_collection()
        #user_collection.modify_user(user_id, email, user_name, user_last_name)
        results = user_collection.modify_user(user_id, email, user_name, user_last_name)
        if results:
            print(f"User Found in UPDATE{user_id} ")

            return True
        else:
            print("User UPDATE NOT Found")      
            return False

    except DuplicateKeyError:
        return False


  
    


def delete_user(user_id, user_collection):
    """
    Deletes a user from user_collection.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    """
    print(f"user to delete {user_id}")
    return user_collection.delete_user(user_id)

    # if user_collection.delete_user(user_id):
    #     return True
    # else:
    #     print(f"{user_id} USer did not delete",)
    #     return False





def search_user(user_id, user_collection):
    """
    Searches for a user in user_collection(which is an instance of
    UserCollection).

    Requirements:
    - If the user is found, returns the corresponding User instance.
    - Otherwise, it returns None.
     def search_user(self, user_id):
    """

    result = user_collection.search_user(user_id)
    if result is None:
        print(f"Search ERROR: User does not exist, user: {user_id}")
        return None
    else:
        return user_collection.search_user(user_id)
        







def add_status(status_id, user_id, status_text, status_collection):
    """
    Creates a new instance of UserStatus and stores it in
    user_collection(which is an instance of UserStatusCollection)

    Requirements:
    - status_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_status() returns False).
    - Otherwise, it returns True.
    """
    status_collection = status_collection.add_status(status_id, user_id, status_text)
    return status_collection
    


def update_status(status_id, user_id, status_text, status_collection):
    """
    Updates the values of an existing status_id

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    """
    status_collection = status_collection.modify_status(status_id, user_id, status_text)
    return status_collection
    


def delete_status(status_id, status_collection):
    """
    Deletes a status_id from user_collection.

    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    """
    print(f"{status_id=}")
    result = status_collection.delete_status(status_id)
    print(RuntimeError, TypeError, NameError)

    return result


def search_status(status_id, status_collection):
    """
    Requirements:
    - If the status is found, returns the corresponding
    UserStatus instance.
    - Otherwise, it returns None.
    """
    result = status_collection.search_status(status_id)
    if result is None:
        return None 
    else:
        return result

    



# if __name__ == '__main__':
#     init_user_collection()
#     status_collection = init_status_collection()
#     user_collection = init_user_collection()
#     load_users("accounts.csv", user_collection)
#     save_users("accounts2.csv", user_collection)
#     load_status_updates("status_updates.csv", status_collection)
#     # results = search_status("evmiles97_00001", status_collection)
#     # print(results)
#     save_status_updates("status_updates2.csv", status_collection)
    
#     user_collection = init_user_collection()
#     status_collection = init_status_collection()
 
   