import requests
import threading
import mysql.connector
import json
import pandas as pd
import threading
import time
from decimal import Decimal
from datetime import datetime

mydb = mysql.connector.connect(host = "localhost", user="Aman", database = "MYDB")
mycursor = mydb.cursor()

def up_wl(username):
    mycursor.execute(f"SELECT CURNAME FROM WATCHLIST WHERE USERNAME = '{username}'")
    c_names = mycursor.fetchall()
    for i in range(len(c_names)):
        mycursor.execute(f"SELECT CID FROM COINS WHERE CNAME = '{c_names[i][0]}'")
        c_id = mycursor.fetchall()
        for j in c_id:
            data = requests.get("http://api.coincap.io/v2/assets/"+f'{j[0]}')
            data = data.json()
            a = data['data']
            mycursor.execute(f"UPDATE WATCHLIST SET PRICE = {Decimal(a['priceUsd'])}, SUPPLY = {Decimal(a['supply'])}, MARKETCAP = {Decimal(a['marketCapUsd'])}, VOLUME = {Decimal(a['volumeUsd24Hr'])} WHERE CURNAME = '{c_names[i][0]}' AND USERNAME = '{username}'")
            mydb.commit()
            print("updated watchlist")
def up_hd(username):        
    mycursor.execute(f"SELECT * FROM HOLDING WHERE USERNAME = '{username}'")
    h_data = mycursor.fetchall()
    for i in range(len(h_data)):
        mycursor.execute(f"SELECT CID FROM COINS WHERE CNAME = '{h_data[i][2]}'")
        c_id = mycursor.fetchall()
        for j in c_id:
            inv = h_data[i][5]
            q = h_data[i][4]
            data = requests.get("http://api.coincap.io/v2/assets/"+f'{j[0]}')
            data = data.json()
            a = data['data']
            returns = Decimal(a['priceUsd'])*q - inv
            mycursor.execute(f"UPDATE HOLDING SET CUR_PRICE = {Decimal(a['priceUsd'])}, RETURNS ={returns} WHERE USERNAME = '{username}' AND CURNAME = '{h_data[i][2]}'")
            mydb.commit()
            print("update holding")
def thr():
    t1 = threading.Thread(target=up_wl('aman1234'))
    t2 = threading.Thread(target=up_hd('aman1234'))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
while True:
    thr()
    time.sleep(15)
    
