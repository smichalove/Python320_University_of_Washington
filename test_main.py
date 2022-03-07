
   
''''
Assignment 5 smichalove
https://github.com/uw-continuum/python-320-assignment-05-smichalove
Test the main.py with Unit Tests
https://kapeli.com/cheat_sheets/Python_unittest_Assertions.docset/Contents/Resources/Documents/index
unit test class Test[udf](unittest.TestCase):
main.py functions:
def init_user_collection():
def init_status_collection():
def load_users(filename, user_collection):
def save_users(filename, user_collection):
def load_status_updates(filename, status_collection):
def save_status_updates(filename, status_collection):
def add_user(user_id, email, user_name, user_last_name, user_collection):
def update_user(user_id, email, user_name, user_last_name, user_collection):
def delete_user(user_id, user_collection):
def search_user(user_id, user_collection):
def add_status(user_id, status_id, status_text, status_collection):
def update_status(status_id, user_id, status_text, status_collection):
def delete_status(status_id, status_collection):
def search_status(status_id, status_collection):
'''
# pylint: disable=R0903
# pylint: disable=C0116,C0103,W1514,C0303,W0105,R1705,C0413,W0611,C0413,W0621,W0612,C0411,R1703,W0613
import os
try:
    os.remove("socialnetwork.db")
except PermissionError as err:
    print(f"Cannot delete socialnetwork.db {err} ")
except FileNotFoundError as err:
    print(f"Cannot delete socialnetwork.db {err} ")
import pathlib
import unittest

from playhouse.dataset import DataSet



from unittest import TestCase
from pathlib import Path
from unittest import result
# import users
# import user_status
import main
import pytest
import random
import string



dir_here = Path(__file__).parent
db = DataSet('sqlite:///socialnetwork.db')
# db = main.bind_database('sqlite:///:memory:')


class TestUserCollection(TestCase):
    '''
    tests of the UserCollection class
    this should test all UserCollection functionality
    '''

    def test_init_user_collection(self):
        '''
        checks that a collection is initialized and empty
        '''
        # db = main.bind_database('sqlite:///:memory:')
        # main.load_users("accounts.csv", main.init_user_collection())
        coll = main.init_user_collection()
        print(len(coll))
        
        if coll is not None:
            assert True
        else: 
            assert False
        # self.assertTrue(coll)

class TestUserStatusCollections(TestCase):
    """ Test init of
    def init_status_collection()
    """

    def test_init_status_collection(self):
        '''
        checks that a collection is initialized and empty
        init_status_collection()

        '''

        # db = DataSet('sqlite:///:memory:')
        # db = main.bind_database('sqlite:///:memory:')
        # self.status_collection = db["StatusTable"]
        # main.load_status_updates("status_updates_test.csv", db["StatusTable"])
        coll = main.init_status_collection()
        print(len(coll))
        if len(coll) > 0:
            assert False
        else: 
            assert True 


class TestUserFunctions(unittest.TestCase):
    """
    test user functions
    """
    def setUp(self):
        # print("------------setUP USER------------")
        # print(dir_here)
        # db = main.bind_database('sqlite:///:memory:')
        # self.db = main.bind_database('sqlite:///:memory:')
        self.letters = string.ascii_lowercase
        self.user_collection = main.init_user_collection()
        self.user_id = "Brittaney.Gentry86"
        self.new_user_id = ''.join(random.choice(self.letters) for i in range(10))
        self.new_user_id_long = ''.join(random.choice(self.letters) for i in range(100))
        self.user_name_long =  ''.join(random.choice(self.letters) for i in range(100))
        self.user_last_name_long =''.join(random.choice(self.letters) for i in range(500))
        
        self.new_user = ''.join(random.choice(self.letters) for i in range(10))
        self.email = "eve.miles@uw.edu"
        self.user_name = "Eve"
        self.user_last_name ="Miles" 
        self.wronguser = ''.join(random.choice(self.letters) for i in range(10))
        self.new_user_name = ''.join(random.choice(self.letters) for i in range(10))
        self.dupefile = "accouts_dupes.csv"
        self.wrongfile = ''.join(random.choice(self.letters) for i in range(10))
        self.filename = "accounts.csv"
        # main.load_users("accounts.csv", main.init_user_collection())

    def test_load_users(self):
        """load the users"""
        result = main.load_users("accounts.csv", main.init_user_collection())
        self.assertTrue(result)

   
    # def test_load_dupe_file(self):
    #     """test duplicate file load USERS"""
    #     print("testing for duplicate file load")
    #     result = main.load_users("accounts.csv", main.init_user_collection())
    #     self.assertFalse(result)
    
    def test_update_user(self):
        """ test
        def update_user(user_id, email, user_name, user_last_name, user_collection):
        """
        print(dir_here)
        # main.load_users("accounts.csv", self.user_collection)

        result = main.add_user("test",self.email, self.new_user,
                                      self.user_last_name,
                                      self.user_collection)
        completed = main.update_user("test", self.email, self.new_user_name, self.user_last_name,
                                     self.user_collection)
        print(completed)
        
        self.assertTrue(completed)

    def test_loaddupes(self):

        results = main.load_users(self.dupefile, self.user_collection)
        self.assertFalse(results)


    def test_loadmissingfile(self):

        results = main.load_users(self.wrongfile,self.user_collection)
        print(self.wrongfile)
        self.assertFalse(results)



    def test_wrong_update_user(self):
        """ test
        def update_user(user_id, email, user_name, user_last_name, user_collection):
        """
      
        completed = main.update_user(self.wronguser, self.email,
                                     self.user_name,
                                     self.user_last_name,
                                     self.user_collection)
        self.assertFalse(completed)

    def test_delete_user(self):
        """ main: def delete_user(user_id, user_collection):
        main.delete_status(status_id, status_collection)
        def delete_user(self, user_id)
        """
        main.add_user("test_user",self.email, self.new_user,
                                      self.user_last_name,
                                      self.user_collection)
        results = main.delete_user("test_user", self.user_collection)
        self.assertTrue(results)
 


    def test_wrongdelete_user(self):
        """ main: def delete_user(user_id, user_collection):
        main.delete_status(status_id, status_collection)
        """



        self.assertFalse(main.delete_user(''.join(random.choice(self.letters) for i in range(10)), self.user_collection))

    def test_search_user(self):

        """ test  search user in main
        def search_user(user_id, user_collection):
           def search_user(self, user_id):
        '''

        """

        result = main.search_user(self.user_id, self.user_collection)

        if result is None:
            print(result)
            assert False

    def test_Wrongsearch_user(self):
        """ test  search user in main
        def search_user(user_id, user_collection):
        """
        #main.load_users("accounts.csv", main.init_user_collection())

        result = main.search_user(self.wronguser, self.user_collection)
        
        self.assertIsNone(result)


    def test_add_user(self):
        """def add_user(user_id, email, user_name, user_last_name, user_collection):
        def add_user(user_id, email, user_name, user_last_name, user_collection):
        """
        result = main.add_user(self.new_user_id,self.email, self.new_user,
                                      self.user_last_name,
                                      self.user_collection)
        self.assertTrue(result)

    def test_add_userlong_uid(self):
        """def add_user(user_id, email, user_name, user_last_name, user_collection):
        def add_user(user_id, email, user_name, user_last_name, user_collection):
        """
        result = main.add_user(self.new_user_id_long,self.email, self.new_user_name,
                                      self.user_last_name,
                                      self.user_collection)
        self.assertFalse(result)

    def test_add_userlong_name(self):
        """def add_user(user_id, email, user_name, user_last_name, user_collection):
        def add_user(user_id, email, user_name, user_last_name, user_collection):
        """
        result = main.add_user(''.join(random.choice(self.letters) for i in range(10)),self.email, self.user_last_name_long,
                                      self.user_last_name,
                                      self.user_collection)
        self.assertFalse(result)

    def test_add_userlong_last_name(self):
        """def add_user(user_id, email, user_name, user_last_name, user_collection):
        def add_user(user_id, email, user_name, user_last_name, user_collection):
        """
        result = main.add_user(''.join(random.choice(self.letters) for i in range(10)),self.email, self.user_name,
                                      self.user_last_name_long,
                                      self.user_collection)
        self.assertFalse(result)


    def test_Sameadd_user(self):
        main.add_user("test", self.email, self.new_user,
                                       self.user_last_name,
                                       self.user_collection)
        


        self.assertFalse(main.add_user("test", self.email, self.new_user,
                                       self.user_last_name,
                                       self.user_collection))


    def Test_wrongFile_load(self):
        """ Test load users return True
        """
        self.assertFalse(main.load_users(self.wrongfile,main.init_user_collection()))
 
"""
    def tearDown(self):
        pass
"""

class TestUserUserCollection(unittest.TestCase):
    '''
    tests of the UserCollection class
    this should test all UserCollection functionality
    '''
    def test_init_collection(self):
        '''
        checks that a collection is initialized and empty
        '''
        coll = main.init_user_collection()
        
        if len(coll) > 0:
            assert True


        



class TestUser_save_users(unittest.TestCase):
    """ Test save users return True
    """
    def setUp(self):
        print("------------setUP------------save")
        #self.user_collection = main.init_user_collection()
    
    
    def test_save_users(self):
        main.load_users("accounts.csv", main.init_user_collection())
        completed = main.save_users(dir_here / "accounts2.csv", main.init_user_collection())
        self.assertTrue(completed)

    def test_badsaveUsers_status(self):

        baddrive = pathlib.PureWindowsPath('v:/')
        main.save_users(baddrive / "status_updates.temp", main.init_user_collection())
        self.assertRaises(FileNotFoundError)

# class TestUserStatusCollections(TestCase):
#     """ Test init of
#     def init_status_collection()
#     """

#     def test_init_status_collection(self):
#         '''
#         checks that a collection is initialized and empty
#         init_status_collection()

#         '''
#         # db = DataSet('sqlite:///:memory:')
#         db = DataSet('sqlite:///socialnetwork.db')
#         # self.status_collection = db["StatusTable"]
#         # main.load_status_updates("status_updates_test.csv", db["StatusTable"])
#         coll = main.init_status_collection()
#         print(len(coll))
#         if len(coll) > 0:
#             assert True
#         else:
#             assert False 


        
class TestUserStatusFunctions(unittest.TestCase):
    """ test
    def update_status(status_id, user_id, status_text, status_collection):
    def delete_status(status_id, status_collection):
    def search_status(status_id, status_collection):
    def load_status_updates(filename, status_collection):
    """
    def setUp(self):
        print("------------setUP STATUS------------")
        # db = main.bind_database('sqlite:///:memory:')
        self.status_id = "Winna.McKay71_321"
        self.status_id_delete = "Dorolice.Julissa21_763"
        self.search_id ="Keri.Royce8"
        self.user_id = "dave03"
        self.status_text = "Perfect weather for a hike"
        self.letters = string.ascii_lowercase
        self.badstatus = ''.join(random.choice(self.letters) for i in range(10))
        self.badUser_id = ''.join(random.choice(self.letters) for i in range(10))
        self.newStatus_id =''.join(random.choice(self.letters) for i in range(10))
        self.newstatus_text = ''.join(random.choice(self.letters) for i in range(20))
        self.newUser_id = ''.join(random.choice(self.letters) for i in range(20))
        # db = DataSet('sqlite:///:memory:')
        self.status_collection = db["StatusTable"]
        self.user_collection = db["UsersTable"]

       
    def test_save_status(self):
        
        completed = main.save_status_updates("status_updates2.csv",db["StatusTable"])
        self.assertTrue(completed)      

    def test_Load_Status(self):
        result = main.load_status_updates(dir_here/"status_updates_test.csv", self.status_collection)
        print(len(self.status_collection))
        # main.m_status_import_csv_in_chunks(100)
        if len(self.status_collection) > 0:
            assert True
        else:
            assert False


    def test_dupe_status_load(self):
        """ duplicate file load of csv"""
        result = main.load_status_updates("status_updates_test.csv", db["StatusTable"])
        self.assertFalse(result)

    def test_update_status(self):
        """ update_status(status_id, user_id, status_text, status_collection):
        """
        main.add_user("test","test","test","test",self.user_collection)
        main.add_status(self.search_id,"test", 
                                self.newstatus_text,  db["StatusTable"])
        result = main.update_status(self.status_id, "test", self.newstatus_text,  db["StatusTable"])

        self.assertTrue(result)


    def test_bad_update_status(self):
        """ update_status(status_id, user_id, status_text, status_collection):
        """
        result = main.update_status(self.badstatus, self.badUser_id, self.status_text, db["StatusTable"])
        self.assertFalse(result)

    def test_badsaveUsers_status(self):
        baddrive = pathlib.PureWindowsPath('v:/')
        main.load_status_updates(baddrive / "status_updates.temp", self.status_collection)
        self.assertRaises(FileNotFoundError)

    def test_add_status(self):
        """
        Test function
        def add_status(user_id, status_id, status_text, status_collection):
       
        """
        
        main.add_user("test","test","test","test",self.user_collection)
        result = main.add_status(''.join(random.choice(self.letters) for i in range(10)),"test", 
                                self.newstatus_text,  db["StatusTable"])
        print(self.newStatus_id,"test_user", 
                                self.newstatus_text )
        self.assertTrue(result)


    def test_delete_status(self):
        """ test
        def delete_status(self, status_id):
        """
        # main.add_user("test","test","test","test",main.init_user_collection())
        main.add_status("test","test","test",self.status_collection)
        # print(self.status_id_delete,self.status_collection)
        self.assertTrue((main.delete_status( "test",self.status_collection)))

    def test_baddelete_status(self):
        """ test
        def delete_status(self, status_id):
        """

        #main.load_status_updates("status_updates.csv", self.status_collection)
       
        self.assertFalse((main.delete_status(self.badstatus,self.status_collection)))

    def test_search_status(self):
        """ test
        def delete_status(self, status_id):
        """
        # main.load_status_updates(dir_here/"status_updates_test.csv", self.status_collection)
        main.add_user("test","test","test","test",self.user_collection)
        result = main.add_status(self.search_id,"test", 
                                self.newstatus_text,  db["StatusTable"])
        print(self.search_id)
        # main.load_status_updates("status_updates.csv", self.status_collection)
        result = main.search_status(self.search_id, self.status_collection)
        if result is not None:
            assert True
        
    def test_bad_add_status(self):
        """ test
        def delete_status(self, status_id):
        """
        main.load_status_updates(dir_here/"status_updates_test.csv", self.status_collection)
        # main.load_status_updates("status_updates.csv", self.status_collection)
        result = main.add_status(''.join(random.choice(self.letters) for i in range(10)),''.join(random.choice(self.letters) for i in range(10)),self.status_text ,self.status_collection)
        if result is not None:
            assert True
        
    def test_badsearch_status(self):
        """ test
        def delete_status(self, status_id):
        """
        #main.load_status_updates("status_updates.csv", self.status_collection)
        result = main.search_status(''.join(random.choice(self.letters) for i in range(10)), self.status_collection)
        if result is None:
            self.assertIsNone(main.search_status(''.join(random.choice(self.letters) for i in range(10)), self.status_collection))
            assert True
        else:
            print (result)
            assert False
class Test_save_updates_load(unittest.TestCase):
    """test save updates
    """
    # def setUp(self):
        # self.db = main.bind_database('sqlite:///:memory:')
        # db = main.bind_database('sqlite:///:memory:')
    

    def test_save_status(self):
        
        completed = main.save_status_updates("status_updates2.csv",db["StatusTable"])
        self.assertTrue(completed)

    def test_badsave_status(self):

        baddrive = pathlib.PureWindowsPath('v:/')
        main.save_status_updates(baddrive / "status_updates.temp",
                                             main.init_user_collection())
        self.assertRaises(FileNotFoundError)