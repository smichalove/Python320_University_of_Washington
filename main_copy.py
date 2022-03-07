#!/usr/bin/env python3
'''
main driver for a simple social network project
'''

import csv
import pathlib
import shutil
import user_status
import users


def init_user_collection():
    '''
    Creates and returns a new instance of UserCollection
    add_user(self, user_id, email, user_name, user_last_name)
    '''
    user_collection = users.UserCollection()
    return user_collection
    pass


def init_status_collection():
    '''

    Creates and returns a new instance of UserStatusCollection
    UserStatusCollection()
    '''
    status_collection = user_status.UserStatusCollection()
    return status_collection
    pass


def load_users(filename, user_collection):
    '''
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
    '''
    cdw = pathlib.Path.cwd()
    print(f"Reading {filename}\npath is {cdw}")
    try:
        with open(filename, mode='r') as accountsfile:
            print(accountsfile)
            global user_header
            reader = csv.reader(accountsfile,delimiter=',')
            user_header = next(reader)
            print(user_header)

            for line in reader:
                user_collection.add_user(line[0], line[1], line[2], line[3])
                #users.UserCollection.add_user(line[0],line[1],line[2],line[3])




    except FileNotFoundError:
        print(f"ERROR: Couldn't find {filename}")
        print(f"Current path is: {cdw} ")

    pass


def save_users(filename, user_collection):
    '''
    Saves all users in user_collection into
    a CSV file

    Requirements:
    - If there is an existing file, it will
    overwrite it.
    - Returns False if there are any errors
    (such as an invalid filename).
    - Otherwise, it returns True.
    '''
    #backup the file

    newfile = r'accounts.csv'
    shutil.copyfile(filename, newfile)

    for key in user_collections.database:
        print(key)
        print(user_collections.database[key].user_id, user_collections.database[key].email,
              user_collections.database[key].user_name, user_collections.database[key].user_last_name)
        records = (user_collections.database[key].user_id, user_collections.database[key].email,
              user_collections.database[key].user_name, user_collections.database[key].user_last_name)

    with open("accounts.tmp", 'w', newline='') as tmp:
        write = csv.writer(tmp)
        write.writerow(user_header)
        write.writerows(records)  # new shipment record
        print("writing file")
    tmp.close()
    shutil.copy(tmp,filename)






    pass


def load_status_updates(filename, status_collection):
    '''
    Opens a CSV file with status data and adds it to an existing
    instance of UserStatusCollection

    Requirements:
    - If a status_id already exists, it will ignore it and continue to
      the next.
    - Returns False if there are any errors(such as empty fields in the
      source CSV file)
    - Otherwise, it returns True.
    STATUS_ID,USER_ID,STATUS_TEXT
    '''
    cdw = pathlib.Path.cwd()
    print(f"Reading {filename}\npath is {cdw}")
    try:
        with open(filename, mode='r') as statusfile:
            reader = csv.reader(statusfile, delimiter=',')
            global status_header
            status_header = next(reader, None)

            for line in reader:
                add_status(line[0], line[1], line[2],status_collection)
    except FileNotFoundError:
        print(f"ERROR: Couldn't find {filename}")
        print(f"Current path is: {cdw} ")
    statusfile.close()
    pass


def save_status_updates(filename, status_collection):
    '''
    Saves all statuses in status_collection into a CSV file

    Requirements:
    - If there is an existing file, it will overwrite it.
    - Returns False if there are any errors(such an invalid filename).
    - Otherwise, it returns True.
    '''
    pass
    newfile = r'status_updates.bak'
    shutil.copyfile(filename, newfile) #backup filename



    for key in status_collection.database:
        print(key)
        print(status_collection.database[key].status_id, status_collections.database[key].user_id,
              status_collection.database[key].status_text)
        records = (status_collection.database[key].status_id, status_collections.database[key].user_id,
              status_collection.database[key].status_text)

    with open("accounts.tmp", 'w', newline='') as tmp:
        write = csv.writer(tmp)
        write.writerow(status_header)
        write.writerows(records)  # new shipment record
        print("writing file")
    tmp.close()
    shutil.copy(tmp,filename)

def add_user(user_id, email, user_name, user_last_name):
    '''
    Creates a new instance of User and stores it in user_collection
    (which is an instance of UserCollection)

    Requirements:
    - user_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_user() returns False).
    - Otherwise, it returns True.
    '''
    users.UserCollection.add_user(user_id, email, user_name, user_last_name)

    pass


def update_user(user_id, email, user_name, user_last_name, user_collection):
    '''
    Updates the values of an existing user

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    '''
    user_collection = users.UserCollection.add_user( user_id, email, user_name, user_last_name)
    return user_collection
    pass


def delete_user(user_id, user_collection):
    '''
    Deletes a user from user_collection.

    Requirements:
    - Returns False if there are any errors (such as user_id not found)
    - Otherwise, it returns True.
    '''

    user_collection = users.UserCollection.delete_user(user_id)
    return user_collection
    pass


def search_user(user_id, user_collection):
    '''
    Searches for a user in user_collection(which is an instance of
    UserCollection).

    Requirements:
    - If the user is found, returns the corresponding User instance.
    - Otherwise, it returns None.
    '''
    user_collection = users.UserCollection.search_user(user_id)
    return user_collection
    pass


def add_status(user_id, status_id, status_text, status_collection):
    '''
    Creates a new instance of UserStatus and stores it in
    user_collection(which is an instance of UserStatusCollection)

    Requirements:
    - status_id cannot already exist in user_collection.
    - Returns False if there are any errors (for example, if
      user_collection.add_status() returns False).
    - Otherwise, it returns True.
    '''
    status_collection = status_collection.add_status(status_id, user_id, status_text)
    return status_collection
    pass


def update_status(status_id, user_id, status_text, status_collection):
    '''
    Updates the values of an existing status_id

    Requirements:
    - Returns False if there any errors.
    - Otherwise, it returns True.
    '''
    status_collection = status_collection.update_status(status_id, user_id, status_text)
    return status_collection
    pass


def delete_status(status_id, status_collection):
    '''
    Deletes a status_id from user_collection.

    Requirements:
    - Returns False if there are any errors (such as status_id not found)
    - Otherwise, it returns True.
    '''
    pass
    status_collection = status_collection.delete_status(status_id)
    return status_collection


def search_status(status_id, status_collection):
    '''
    Searches for a status in status_collection

    Requirements:
    - If the status is found, returns the corresponding
    UserStatus instance.
    - Otherwise, it returns None.
    '''
    status_collection = status_collection.search_status(status_id)
    return status_collection
    pass


if __name__ == '__main__':
    user_collection = init_user_collection()
    status_collection = init_user_collection()
    load_users("accounts.csv", user_collections)
    load_status_updates("status_updates.csv",status_collections)
    for key in user_collections.database:
         print(key)
         print(user_collections.database[key].user_id,user_collections.database[key].email,user_collections.database[key].user_name,user_collections.database[key].user_last_name)
    for key in status_collections.database:
        print(key)
        print(status_collections.database[key].status_id,status_collections.database[key].user_id,status_collections.database[key].status_text)

    print("\n\n\nusers", dir(users.Users))
    print("collection", dir(user_collections))
    print("sc collection", dir(status_collections))

    print("add", dir(user_collections.add_user))



