import requests
import threading
import mysql.connector
import json
import pandas as pd
import threading
import time
from decimal import Decimal
from datetime import datetime

import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user="Aman", database = "mydb")
mycursor = mydb.cursor()

def up_wl(username):
    mycursor.execute("SELECT * FROM WATCHLIST")
    w_data = mycursor.fetchall()
    for i in range(len(w_data)):
        curname = w_data[i][2]
        data = requests.get("http://api.coincap.io/v2/assets/"+f'{curname.lower()}')
        data = data.json()
        a = data['data']
        mycursor.execute(f"UPDATE WATCHLIST SET PRICE = {Decimal(a['priceUsd'])}, SUPPLY = {Decimal(a['supply'])}, MARKETCAP = {Decimal(a['marketCapUsd'])}, VOLUME = {Decimal(a['volumeUsd24Hr'])} WHERE CURNAME = '{curname}' ")
        mydb.commit() 
def up_hd(username):        
    mycursor.execute("SELECT * FROM HOLDING")
    h_data = mycursor.fetchall()
    for i in range(len(h_data)):
        curname = h_data[i][2]
        inv = h_data[i][5]
        q = h_data[i][4]
        data = requests.get("http://api.coincap.io/v2/assets/"+f'{curname.lower()}')
        data = data.json()
        a = data['data']
        returns = inv - Decimal(a['priceUsd'])*q
        mycursor.execute(f"UPDATE HOLDING SET CUR_PRICE = {Decimal(a['priceUsd'])}, RETURNS ={returns} WHERE CURNAME = '{curname}' ")
        mydb.commit() 
def thr():
    t1 = threading.Thread(target=up_wl('superman'))
    t2 = threading.Thread(target=up_hd('superman'))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

while True:
    thr()
    time.sleep(30)
    
