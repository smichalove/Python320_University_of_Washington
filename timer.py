

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
import multiprocessing
from multiprocessing import Process
import main

def import_users():
    jobs = []
    for i in range(1):
        p = multiprocessing.Process(target=main.import_csv_in_chunks(),args=10)
        p.start()
        p.join()
        jobs.append(p)
        p.close()
       
        
        

def import_status():
    jobs = []
    for i in range(1):
        p = multiprocessing.Process(target=main.status_import_csv_in_chunks(1000))
        p.start()
        p.join()       
        jobs.append(p)
        p.close()
        
        

# main.import_csv_in_chunks(100)


# if __name__ == '__main__':
    print(multiprocessing.cpu_count())
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
    socialnetwork_model.User()
    
    socialnetwork_model.UserStatus()

    user_collection = main.init_user_collection()
    status_collection = main.init_status_collection()
    load =  "main.load_users('accounts.csv',user_collection)"
    usercol.drop()
    loaddu = timer(stmt=load,globals=globals(),number=1)
    print(f"time to add all users with OUT multi processsing, {loaddu}")
    statusrcol.drop()
  
    load_status = "main.load_status_updates('status_updates.csv',status_collection)"
    load_stutus_time = timer(stmt=load_status,globals=globals(),number=1)
    print(f"load status without multiprocessing: , {load_stutus_time}")
    usercol.drop()
    statusrcol.drop()


    # THREADING
    start = time.time()
    main.import_csv_in_chunks(500)
    end = time.time()
    total = end - start
    print(f"Total to load all users  -- THREADING timer.py, {total}")
    start = time.time()
    main.status_import_csv_in_chunks(10000)
    end = time.time()
    total = end - start
    print(f"Total to load all status --THREADINGt timer.py , {total}")
    usercol.drop()
    statusrcol.drop()
    start = time.time()
    main.m_import_csv_in_chunks(500)
    end = time.time()
    total = end - start
    print(f"Total to load all users  -- MULTI timer.py, {total}")
    start = time.time()
    main.m_status_import_csv_in_chunks(10000)
    end = time.time()
    total = end - start
    print(f"Total to load all status --MULTI timer.py, {total}")