""" Assignment 6 performance of Mango
"""
from ast import stmt
from pathlib import Path
import csv
import pathlib
from timeit import repeat, timeit as timer
import main
import users
import user_status
import pymongo
import pandas as pd
import random
import string
import time
import socialnetwork_model

letters = string.ascii_lowercase
# from pymongo import MongoClient
# from pymongo.errors import DuplicateKeyError

def add_random_users():
    
    for n in range(500):
        new_user_id = ''.join(random.choice(letters) for i in range(10))
        add_user(new_user_id,"email","name","lastname",user_collection)

def add_random_status():

    """
    search a 1000 records
   """
  


    cdw = pathlib.Path.cwd()
    # print(f"Reading {filename}\npath is {cdw}")
    status_header = ["STATUS_ID","USER_ID","STATUS_TEXT"]
    #global tatus_header
    try:
        filename = "status_updates.csv"
        with open(filename, mode='r') as statusfile:
            reader = csv.reader(statusfile, delimiter=',')
            status_header = next(reader)
            count = 0
            # print(status_header)
            for line in reader:
                
                new_status_id = ''.join(random.choice(letters) for i in range(10))
                add = main.add_status(new_status_id,line[1],line[2],status_collection)
                
                count += 1
                if count == 1000:
                    break
                # print("added:",line[0], line[1], line[2])
        statusfile.close()
        
        # print(f'lines counted for Status: {count}')
        return True

    except FileNotFoundError:
        print(f"ERROR: Couldn't find {filename}")
        print(f"Current path is: {cdw} ")

def load_users(filename, user_collection):
    """
    Load 1000 lines
    """

    user_header = ["USER_ID", "EMAIL", "NAME", "LASTNAME"]
    cdw = pathlib.Path.cwd()
    # print(f"Reading{cdw} {filename}\npath is {cdw}")
    try:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["UserAccounts"]
        # mongo_docs = mydb["Users"]
        usercol = mydb["UserAccounts"]
        # mongo_docs =
        # print("drop the database")
        # usercol.drop()
        
        # df =  pd.DataFrame(list(mongo_docs))
        # df.to_csv(filename, index=False)       
    # return True

    except FileNotFoundError:

        print(f"ERROR: Couldn't find {filename}")
        print(f"Current path is: {cdw} ")
        path = Path(filename)
        print(path)
        return False

    except OSError: 
        return False

   
    count = 0
    try:
        with open(filename, mode='r', newline='\n') as accountsfile:
            # print(accountsfile)
            reader = csv.reader(accountsfile, delimiter=',')
            user_header = next(reader)
            # print("header", user_header)
           

            for row in reader:
                count += 1
                # USER_ID,NAME,LASTNAME,EMAIL (self, user_id, email, user_name, user_last_name)
                # print("row",row[0], row[1], row[2], row[3])
                
                    # print("line",row)
                load = add_user(row[0], row[3], row[1], row[2], user_collection)
                if count == 1000:
                    break

            # print(f"lines counted {count}")

        accountsfile.close()
        return True
    except FileNotFoundError:
            print(f"ERROR: Couldn't find {filename}")
            print(f"Current path is: {cdw} ")
            return False

def search_1000_status_updates(filename, status_collection):
    """
    search a 1000 records
   """
  


    cdw = pathlib.Path.cwd()
    # print(f"Reading {filename}\npath is {cdw}")
    status_header = ["STATUS_ID","USER_ID","STATUS_TEXT"]
    #global tatus_header
    try:
       
        with open(filename, mode='r') as statusfile:
            reader = csv.reader(statusfile, delimiter=',')
            status_header = next(reader)
            count = 0
            # print(status_header)
            for line in reader:
                
                
                search = main.search_status(line[0], status_collection)
                
                count += 1
                if count == 1000:
                    break
                # print("added:",line[0], line[1], line[2])
        statusfile.close()
        
        # print(f'lines counted for Status: {count}')
        return True

    except FileNotFoundError:
        print(f"ERROR: Couldn't find {filename}")
        print(f"Current path is: {cdw} ")

        return False

def delete_status_updates(filename, status_collection):
    """
    search a 1000 records
   """
  


    cdw = pathlib.Path.cwd()
    # print(f"Reading {filename}\npath is {cdw}")
    status_header = ["STATUS_ID","USER_ID","STATUS_TEXT"]
   
    #global tatus_header
    try:
       
        with open(filename, mode='r') as statusfile:
            reader = csv.reader(statusfile, delimiter=',')
            status_header = next(reader)
            count = 0
            # print(status_header)
            for line in reader:
                
               
                search = main.delete_status(line[0], status_collection)
                
                
                count += 1
                if count == 1000:
                    break
                # print("added:",line[0], line[1], line[2])
        # tatusfile.close()
        
        # print(f'lines counted for Status: {count}')
        return True

    except FileNotFoundError:
        print(f"ERROR: Couldn't find {filename}")
        print(f"Current path is: {cdw} ")

        return False


def search_1000_users(filename, user_collection):
    """
    Load 1000 lines
    """
    user_header = ["USER_ID", "EMAIL", "NAME", "LASTNAME"]
    cdw = pathlib.Path.cwd()
    count = 0
    try:
        with open(filename, mode='r', newline='\n') as accountsfile:
            # print(accountsfile)
            reader = csv.reader(accountsfile, delimiter=',')
            user_header = next(reader)
            # print("header", user_header)
           

            for row in reader:
                count += 1
                # USER_ID,NAME,LASTNAME,EMAIL (self, user_id, email, user_name, user_last_name)
                # print("row",row[0], row[1], row[2], row[3])
                
                    # print("line",row)
                load = main.search_user(row[0], user_collection)
                
                if count == 1000:
                    break
        accountsfile.close()
            # print(f"lines counted {count}")
    except FileNotFoundError:
            print(f"ERROR: Couldn't find {filename}")
            print(f"Current path is: {cdw} ")
            return False

def delete_1000_users(filename, user_collection):
    """
    delete 1000 lines
    """
    user_header = ["USER_ID", "EMAIL", "NAME", "LASTNAME"]
    cdw = pathlib.Path.cwd()
    count = 0
    try:
        with open(filename, mode='r', newline='\n') as accountsfile:
            # print(accountsfile)
            reader = csv.reader(accountsfile, delimiter=',')
            user_header = next(reader)
            # print("header", user_header)
           

            for row in reader:
                count += 1
                # USER_ID,NAME,LASTNAME,EMAIL (self, user_id, email, user_name, user_last_name)
                # print("row",row[0], row[1], row[2], row[3])     
                
                load = main.delete_user(row[0], user_collection)
                
                if count == 1000:
                    break
        accountsfile.close()
            # print(f"lines counted {count}")
        
        return True
    except FileNotFoundError:
            print(f"ERROR: Couldn't find {filename}")
            print(f"Current path is: {cdw} ")
            return False


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
    status_collection = main.add_status(status_id, user_id, status_text,status_collection)
    return status_collection

def load_status_updates(filename, status_collection):
    """
    Asd a 1000 records
   """
    try:
        # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        # mydb = myclient["StatusUpdates"]
        # # mongo_docs = mydb["Users"]
        # statuscol = mydb["StatusUpdates"]
        # mongo_docs = statuscol.find({},{"_id":0})

        with open(filename, mode='r') as statusfile:
            reader = csv.reader(statusfile, delimiter=',')
            status_header = next(reader)
            count = 0
            # print(status_header)
            for line in reader:
                #defadd_status(self, status_id, user_id, status_text):
                # print(f"load {line}")
                main.add_status(line[0], line[1], line[2],status_collection)
                count += 1
                if count == 1000:
                    break
                # print("added:",line[0], line[1], line[2])
           
        statusfile.close()
        
        

    except FileNotFoundError:

        print(f"ERROR: Couldn't find {filename}")

        path = Path(filename)
        print(path)
        return False

    except OSError: 
        return False

   


if __name__ == '__main__':
    socialnetwork_model.User()
    socialnetwork_model.UserStatus()
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    mydbs = myclient["StatusUpdates"]
    # mongo_docs = mydb["Users"]
    statusrcol = mydbs["StatusUpdates"]
    statusrcol.drop()

    mydb = myclient["UserAccounts"]
    usercol = mydb["UserAccounts"]
    usercol.drop()
    socialnetwork_model.UserStatus()


    status_collection = main.init_status_collection()
    user_collection = main.init_user_collection()

    reps = 2
    luser = 'load=load_users("accounts.csv", user_collection)'
    lstatus = 'load=load_status_updates("status_updates.csv",status_collection)'

    time.sleep(1)

    load_1000_users = timer(stmt=luser,globals=globals(),number=reps)
    time.sleep(2)
    load_1000_status = timer(stmt=lstatus,globals=globals(),number=reps)
    # print(f"user mango load  {load_1000_users}")
    # print(f"Status MANGO load {load_1000_status}")
    time.sleep(2)
    susers = 'search_1000_users("accounts.csv", user_collection)'
    sstatus = 'search_1000_status_updates("status_updates.csv",status_collection)'
    search_1k_users = timer(stmt=susers,globals=globals(),number=reps)
    time.sleep(1)
    print(f"time to search mNGO 1000 users: , {search_1k_users}")
    search_1k_updates = timer(stmt=sstatus,globals=globals(),number=reps)
    print(f"time to search mango 1000 users: , {search_1k_users}")
    time.sleep(1)
    print(f"time to search mango 1000 updates , {search_1k_updates}")
    time.sleep(1)
    print(f"user mango load , {load_1000_users}")
    print(f"Status mango load , {load_1000_status}")
    add="add_random_users()"
    add5kusers =  timer(stmt=add,globals=globals(),number=reps)
    adds = "add_random_status()"
    add5kstatus =  timer(stmt=adds,globals=globals(),number=reps)
    
    dels = 'delete_status_updates("status_updates.csv",status_collection)'
    #deletestatus = timer(stmt=dels,globals=globals(),number=1)
  
    print(f"time to add 5k random user mango:,  {add5kusers}")
    print(f'tile to add random status mango: , {add5kstatus}')
    delu = 'delete_1000_users("accounts.csv", user_collection)'
    deletusers =  timer(stmt=delu,globals=globals(),number=reps)
    print(f"time to delete status mango: , {timer(stmt=dels,globals=globals(),number=1)}")
    print(f"time to delete user mango: , {deletusers}")
  




