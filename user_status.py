'''
classes to manage the user status messages
Assignment 5 Steven Michalove
'''
# pylint: disable=R0903

# pylint: disable=C0116,C0103,W1514,C0303,W0105,R1705,C0413,W0611,C0413,W0621,W0612,C0411,R1703,W0613
import pymongo
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
import pytest
import datetime
from time import time
from hashlib import new
from msilib.schema import Error
from dataclasses import dataclass



from datetime import datetime
import sys


class MongoDBConnection():
    '''
    MongoDB Connection context manager
    '''

    def __init__(self, host='127.0.0.1', port=27017):
        """ be sure to use the ip address not name for local windows"""
        self.host = host
        self.port = port
        self.connection = MongoClient(self.host, self.port)

class Status():
    '''
    Contains status information
    '''
    @dataclass
    class status:
        '''define status'''
        status_id: str
        user_id:str
        status_text: str
  
class UserStatus():
    '''
    class to hold status message data
    '''

class UserStatusCollection():
    '''
    Collection of UserStatus messages
    '''

    def __init__(self):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["StatusUpdates"]
        self.statuscol = mydb["StatusUpdates"]        
        # mongo = MongoDBConnection
        # print(MongoDBConnection)
        # database = mongo.connection
        # self.userstatus = database['StatusUpdates']
        # mongo = MongoDBConnection

        
        # self.statuscol = database['StatusUpdates']
        return None
  
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

 
    def __enter__(self):
        self.host='127.0.0.1'
        self.port=27017
        self.connection = MongoClient(self.host, self.port)
        return self

    def add_status(self, status_id, user_id, status_text):
        '''
        add a new status message to the collection
        '''
        # logger.debug(f"add status {status_id} :: ")
        # if status_id in self.database:
        #     # Rejects new status if status_id already exists
        #     return False
        # new_status = UserStatus(status_id, user_id, status_text)
        # self.database[status_id] = new_status
        # return True
        # a_status = {'status_id' : status_id}
        new_status = {'_id' : status_id,
                    'status_id' : status_id,
                    'user_id'  : user_id,
                    'status_text' : status_text,
                    }
        try:
            
            self.statuscol.insert_one(new_status)
            return True

                
        except DuplicateKeyError:
            return False
        
    def modify_status(self, status_id, user_id, status_text):
        '''
        Modifies a status message

        The new user_id and status_text are assigned to the existing message
        '''
        # if status_id not in self.database:
        #     # Rejects update is the status_id does not exist
        #     return False
        # self.database[status_id].user_id = user_id
        # self.database[status_id].status_text = status_text
        # return True
        statusdict = {
                      '_id' : status_id,
                      "status_id ": status_id,
                      "user_id" : user_id,
                      "status_text" : status_text}
        sfilter = {"status_id": status_id}
        try:
            result = self.statuscol.find_one({"status_id": status_id})
            if result is None:
                print(f"User not found {status_id} and {result}")
                return None
            self.statuscol.update_one(sfilter,{"$set":statusdict})
            return True
        except AttributeError as err:
            print(f"{err}")

        return False


    def delete_status(self, status_id):
        '''
        deletes the status message with id, status_id
        '''
        # if status_id not in self.database:
        #     # Fails if status does not exist
        #     logger.debug(f"{status_id }delete_status status_id not in")

        #     return False
        # del self.database[status_id]
        # logger.debug(f"{status_id}delete_status FOUND")
        # return True
        try:
            
            a_status = {"_id": status_id }
            
            result = self.statuscol.find_one(a_status)
            if result is None:
                return False
            self.statuscol.delete_one(a_status)

            return True
        except AttributeError as err:
            print(f"{err}")
            return False
        


    def search_status(self, status_id):
        '''
        Find and return a status message by its status_id

        Returns an empty UserStatus object if status_id does not exist
        '''
        # logger.debug(f"{status_id} ::   users_status.py search_status")
        # if status_id not in self.database:
        #     # Fails if the status does not exist
        #     logger.error(f"{status_id} NOT IN {UserStatus}::")
        #     return UserStatus(None, None, None)
        # logger.debug(f"{status_id} ::  {self.database[status_id]} found")
        # return self.database[status_id]
        a_status = {'_id' : status_id}
        result = self.statuscol.find_one(a_status,{"_id":0})
        try:
            if result is None:
                return None
            
            return result
        except TypeError as err:
            print(f"...............{err}")
            return False