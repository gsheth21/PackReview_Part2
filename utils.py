import os
import sys
from pymongo import MongoClient

def get_DB():
    with open(os.path.join(sys.path[0], "app/config.py"), "r") as f:
        content=f.readlines()
    client = MongoClient("mongodb+srv://anishd1910:VEfj1VPH9foeE3NT@cluster0.oagwk.mongodb.net/")

    
    return client.SEProj2
