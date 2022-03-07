'''
Classes for user information for the social network project
Assignment 5 Steven Michalove
'''
# pylint: disable=R0903
from dataclasses  import dataclass, asdict

# from msilib.schema import Error
import pymongo
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
# pylint: disable=R0903
# pylint: disable=C0116,C0103,W1514,C0303,W0105,R1705,C0413,W0611,C0413,W0621,W0612,C0411,R1703,W0613





class MongoDBConnection():
    '''
    MongoDB Connection context manager
    '''

    def __init__(self, host='127.0.0.1', port=27017):
        """ be sure to use the ip address not name for local windows"""
        self.host = host
        self.port = port
        self.connection = MongoClient(self.host, self.port)

    # def __enter__(self):
    #     self.connection = MongoClient(self.host, self.port)
    #     return self
        

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.connection.close()


class Users():
    '''
    Contains user information
    '''
    @dataclass
    class User:
        '''define user'''
        user_id: str
        email:str
        user_name: str
        user_last_name: str
    # def __init__(self, user_id, email, user_name, user_last_name):
    #     ''' initialize mongodb'''
    #     # self.user_id = user_id
    #     # self.email = email
    #     # self.user_name = user_name
    #     # self.user_last_name = user_last_name
    #     self.mongodb = mongodb  # just in case we need it
    #     self.userscol = mongodb.users


class UserCollection():
    '''
    Contains a collection of Users objects
    '''
    def __init__(self, ):
        """ be sure to use the ip address not name for local windows"""

        #self.connection = MongoDBConnection
        # mongo = MongoDBConnection
        # print(MongoDBConnection)
        # database = mongo.connection

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["UserAccounts"]
        self.usercol = mydb["UserAccounts"]
        # self, host='127.0.0.1', port=27017
        self.host='127.0.0.1'
        self.port=27017
            
 


        

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

 
    def __enter__(self):
        self.connection = MongoClient(self.host, self.port)
        return self
    # def __init__(self,mongodb):
    #     """
    #     Initialize a DirectorsCollection with the provided database
    #     """
    #     self.mongodb = mongodb  # just in case we need it
    #     self.usercol = mongodb.users
    # def __init__(self):
    #     self.database = {}
    def __len__(self):
        """ number of Directors in the collection """
        return self.usercol.count_documents({})

    def add_user(self, user_id, email, user_name, user_last_name):
        '''
        Adds a new user to the collection
        '''
        a_user = {'user_id' : user_id}
        new_user = {'_id' : user_id,
                    'user_id' : user_id,
                    'email'  : email,
                    'user_name' : user_name,
                    'user_last_name' : user_last_name
                    }
        try:
            found = self.usercol.find_one(a_user)
            if found is None:
                self.usercol.insert_one(new_user)
                return True
            else:
                return False
                
        except DuplicateKeyError:
            return False
        return True
        # if user_id in self.database:
        #     # Rejects new status if status_id already exists
        #     return False
        # new_user = Users(user_id, email, user_name, user_last_name)
        # self.database[user_id] = new_user


    def modify_user(self, user_id, email, user_name, user_last_name):
        '''
        Modifies an existing user
        '''

        userdic = {'_id' : user_id,
                    'userid' : user_id,
                    'email'  : email,
                    'user_name' : user_name,
                    'user_last_name' : user_last_name
                }
        ufilter ={"user_id": user_id}
        try:
            result = self.usercol.find_one({"user_id": user_id})
            if result is None:
                
                return False
            self.usercol.update_one(ufilter,{"$set":userdic})
            return True
        except DuplicateKeyError as err:
            print(f"{err}")
            return False
        # if user_id not in self.database:
        #     return False
        # self.database[user_id].email = email
        # self.database[user_id].user_name = user_name
        # self.database[user_id].user_last_name = user_last_name
        # return True

    def delete_user(self, user_id):
        '''
        Deletes an existing user
        '''
        # if user_id not in self.database:
        #     return False
        # del self.database[user_id]
        # return True
        try:
            a_user = {'user_id' : user_id}
            result = self.usercol.find_one({"user_id": user_id})
            if result is None:
                return False
            self.usercol.delete_one(a_user)
            return True
        except AttributeError as err:
            print(f"{err}")
            return False



    def search_user(self, user_id):
        '''
        Searches for user data
        '''
        a_user = {'user_id' : user_id,}
        result = self.usercol.find_one(a_user,{"_id":0})


        if result is None:
            return None
        return result


