#!/usr/bin/env python3
"""
main driver for a simple social network project
https://github.com/uw-continuum/python-320-assignment-08-smichalove

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



from playhouse.dataset import DataSet

import peewee
import sqlite3
from pathlib import Path
import csv
import pathlib
# import user_status
# import users
user_header =[]

import pandas as pd
import multiprocessing
import time
import threading
import os
db = DataSet('sqlite:///socialnetwork.db')
# db = DataSet('sqlite:///:memory:')
# db = DataSet('sqlite:///:memory:')


# user_collection = init_user_collection()
# status_collection = init_status_collection()

# def bind_database(destination='sqlite:///socialnetwork.db'):
#   TODO: """couldd not figrueout namespace issues when importing mailn"""
#     global db
#     db = DataSet(destination)
   
#     return db

def init_user_collection():
    '''
    Creates and returns a new instance of UserCollection
    '''

    try:
        
        Users = db["UsersTable"]
        
       

        
        Users.insert(USER_ID ='index_user')
        
        
        if len(Users) == 1 :
            db['UsersTable'].create_index(['USER_ID'], unique=True)
        
        Users.delete(USER_ID ='index_user')
        return db["UsersTable"]
        # return users.UserCollection()
    except peewee.OperationalError as err:
        print(err)

        return False
    except peewee.IntegrityError: 
        print(err)
        return False
    


def init_status_collection():
    """

    Creates and returns a new instance of UserStatusCollection
    UserStatusCollection()
    """
    try:
        Statuses = db["StatusTable"]
        size = len(Statuses)
        
       
        print(f"Statustable has {len(Statuses)}")
        # Statuses.insert(STATUS_ID ='index_status')
        # db["StatusTable"].create_index(['STATUS_ID'], unique=True)
       
        # Statuses.delete(STATUS_ID ='index_status')
        if size == 0:
            Statuses.insert(STATUS_ID ='index_status')
            db["StatusTable"].create_index(['STATUS_ID'], unique=True)
            Statuses.delete(STATUS_ID ='index_status')
        # print(result)
        return Statuses
    except peewee.OperationalError as err:
        print("index error {err}")
        return False
    except peewee.IntegrityError as err: 
        print("index error {err}")
        print(err)
        return False


  

def load_users(filename, user_collection= db["UsersTable"]):
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
 
    cdw = pathlib.Path.cwd()
    print(f"Reading {filename}\npath is {cdw}")
   
    count = 0
    Users = db["UsersTable"]
    try:
        result = Users.thaw(format='csv',filename=filename,encoding='utf8')
        return True

    except peewee.IntegrityError as err: 
        print(f"Duplicate user found\n {err}")
        return False
    except FileNotFoundError:
        print(f"ERROR: Couldn't find {filename}")
        print(f"Current path is: {cdw} ")
        return False



                


def save_users(filename, user_collection= db["UsersTable"]):
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


   
    Users = db["UsersTable"]
    
    try:
        user_collection.freeze(format='csv',filename=filename)     
        return True

    except FileNotFoundError:

        print(f"ERROR: Couldn't find {filename}")
        print(f"Current path is: {cdw} ")
        path = Path(filename)
        print(path)
        return False

    except OSError: 
        return False


    except peewee.IntegrityError:
        return False





def load_status_updates(filename, status_collection = db["StatusTable"]):
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
    status_collection = db["StatusTable"]
    
    try:
        status_collection.thaw(filename=filename, format='csv',encoding='utf8')
        return True
  
    except FileNotFoundError:
        print(f"ERROR: Couldn't find {filename}")
        print(f"Current path is: {cdw} ")

        return False
    
    except peewee.IntegrityError:
        print("ERROR DULICATE STATUS")
        return False
    except OSError: 
        return False

def save_status_updates(filename, status_collection = db["StatusTable"]):
    """
    Saves all statuses in status_collection into a CSV file

    Requirements:
    - If there is an existing file, it will overwrite it.
    - Returns False if there are any errors(such an invalid filename).
    - Otherwise, it returns True.
    """
    cdw = pathlib.Path.cwd()
   
    status_collection = db["StatusTable"]
    
    try:
        status_collection.freeze(format='csv',filename=filename)
        
        return True
  
    except FileNotFoundError:
        print(f"ERROR: Couldn't find {filename}")
        print(f"Current path is: {cdw} ")
        return False
    
    
    except OSError: 
        return False


    





def add_user(user_id, email, user_name, user_last_name, user_collection= db["UsersTable"]):
    """add users with users: def add_user(self, user_id, email, user_name, user_last_name):
        Creates a new instance of User and stores it in user_collection
        (which is an instance of UserCollection)
        The Users table will have the following fields:
            user_id (Primary Key, limited to 30 characters).
            user_name (Limited to 30 characters).
            user_last_name (Limited to 100 characters).
            user_email.
    """
    try:
        if len(user_id) > 30:
            print(f"ERROR {user_id} is {len(user_id)} length >30 ")
            return False
        elif len(user_name) > 30:
            print(f"ERROR {user_name} is {len(user_name)} length >30 ")
            return False
        elif len(user_last_name) > 100:
            print(f"ERROR {user_last_name} length is {len(user_last_name)} >100 ")
            return False
            
        
        Users = db["UsersTable"]
      
        result = Users.insert(USER_ID=user_id, NAME=user_name, LASTNAME=user_last_name,EMAIL=email,)
       
        return result
    except peewee.IntegrityError as err: 
        print(err)
        return False


def update_user(user_id, email, user_name, user_last_name, user_collection= db["UsersTable"]):
    """
    Updates the values of an existing user

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    def modify_user(self, user_id, email, user_name, user_last_name):
    """
    Users = db["UsersTable"]
    try:
    
        results = Users.update(USER_ID=user_id,EMAIL=email, NAME=user_name, LASTNAME=user_last_name, columns=['USER_ID'])
        print(results)
        if results:
            print(f"User Found in UPDATE{user_id} ")

            return True
        else:
            print("User UPDATE NOT Found")  
            raise peewee.IntegrityError    
            

    except peewee.IntegrityError:
        return False


  
    


def delete_user(user_id, user_collection = db["UsersTable"]):
    """
    Deletes a user from user_collection.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    """

    Users = db["UsersTable"]
    Statuses = db["StatusTable"]
    
    
    try:
        result_status = False
        result = Users.delete(USER_ID=user_id) 
        if result:
            result_status = True
            result_status = Statuses.delete(USER_ID=user_id) # delete realated status records
            raise KeyError
            
   
        else:
            result_status = Statuses.delete(USER_ID=user_id) # delete realated status records
            return False
        
    except peewee.IntegrityError as err: 

        print(err) 
        return False        



    except KeyError as err:
        if result_status:
            return True
        elif result:
            print("no statuses to delete")
            return result

    # if user_collection.delete_user(user_id):
    #     return True
    # else:
    #     print(f"{user_id} USer did not delete",)
    #     return False





def search_user(user_id, user_collection= db["UsersTable"]):
    """
    Searches for a user in user_collection(which is an instance of
    UserCollection).

    Requirements:
    - If the user is found, returns the corresponding User instance.
    - Otherwise, it returns None.
     def search_user(self, user_id):
    """
    
    Users = db["UsersTable"]
    result = Users.find_one(USER_ID=user_id)
    if result is None:
        print(f"Search ERROR: User does not exist, user: {user_id}")
        return None
    else:
       
        results = result.values()
        print(results)
        print(list(results)[1:])
        
        return  list(results)[1:]
        







def add_status(status_id, user_id, status_text, status_collection = db["StatusTable"]):
    """
    Creates a new instance of UserStatus and stores it in
    user_collection(which is an instance of UserStatusCollection)

    Requirements:
    - status_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_status() returns False).
    - Otherwise, it returns True.
    """
    try:
        Users = db["UsersTable"]
        Statuses =  db["StatusTable"]
        exists = search_user(user_id,Users)
        if exists is None:
            print("USER ID does not match, not adding status")
            raise peewee.IntegrityError
            
        else:
            Statuses = db["StatusTable"]
            result = Statuses.insert(STATUS_ID=status_id, USER_ID=user_id, STATUS_TEXT=status_text)
            print("USER ID does not match, not adding status")
            return result
        
        return True
    except peewee.IntegrityError as err: 
        print(err)
        return False
    except peewee.OperationalError as err: 
        print(err)
        return False


def update_status(status_id, user_id, status_text, status_collection = db["StatusTable"]):
    """
    Updates the values of an existing status_id

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    """
    try:
        Statuses = db["StatusTable"]
        result = Statuses.update(STATUS_ID=status_id, USER_ID=user_id, STATUS_TEXT=status_text,columns=['STATUS_ID'])
        return result
    except peewee.OperationalError as err:
        print(f"error {err}")    
        return False
    
    


def delete_status(status_id, status_collection = db["StatusTable"]):
    """
    Deletes a status_id from user_collection.

    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    """
    Statuses = db["StatusTable"]
    result = Statuses.delete(STATUS_ID=status_id)
    

    return result


def search_status(status_id, status_collection = db["StatusTable"]):
    """
    Requirements:
    - If the status is found, returns the corresponding
    UserStatus instance.
    - Otherwise, it returns None.
    """
    Statuses = db["StatusTable"]
    result = Statuses.find_one(STATUS_ID=status_id)
    if result is None:
        return None 
    else:      
        results = result.values()
        return  list(results)[1:]
