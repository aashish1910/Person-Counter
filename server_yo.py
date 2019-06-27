#this is a server client socket connection from person counter to a server from which the data will be further send to webapp and database
import pickle
import socket #Mysql needed
import json

from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
#from database import Base,Iot_Counter #giving error
import random
import string
import time
import pymongo
import datetime

from pymongo import MongoClient
# IMPORTS FOR AUTHENTICATION


import json
from flask import make_response
import requests

#import for flask admin
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
admin=Admin(app)
#app = Flask(__name__)

import MySQLdb# For database

db=MySQLdb.connect("localhost","root","root","firstdb")
cursor=db.cursor()

cursor.execute("drop table if exists ak")

query="""create table ak( \
               upcount integer(5), \
               downcount integer(5), \
               totalcount integer(6))"""
cursor.execute(query)

class foo(object):
    pass

TCP_IP = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print ("conn info: ", conn)
upcount=0
downcount=0
while True:
    objrcv = pickle.loads ( conn.recv ( 1024 ) )
    #print ("conn recv: ", objrcv)
   #print ("conn from: ", addr)
    if objrcv.Y == 0:
        print ("down count")
        print (objrcv.X)
        downcount = objrcv.X
    elif objrcv.Y == -1:
        print ("upcount")
        print  (objrcv.X)
        upcount=objrcv.X
    totalcount=upcount-downcount
    print("Total count : ",totalcount)
    query= "insert into ak values('%d', '%d', '%d')" % (upcount, downcount, totalcount)
    cursor.execute(query)
    db.commit()

    












'''


'''
