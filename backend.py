import mysql.connector
import requests
import json
import pandas as pd
import threading
import time

mydb = mysql.connector.connect(host = "localhost", user="Aman", database = "mydb")
mycursor = mydb.cursor()

#FOR SIGNUP
def selectfromusers(username):
    sql = "SELECT * FROM USER_INFO WHERE USERNAME = %s "
    val = (username,)
    mycursor.execute(sql,val)
    userdata = mycursor.fetchall()
    for i in userdata:
        return i
#FOR SIGNUP    
def insertintousers(fullname,username,phno,passwd):
    sql = "INSERT INTO USER_INFO VALUES(%s,%s,%s,%s)"
    val = (fullname,username,phno,passwd,)
    mycursor.execute(sql,val)
    mydb.commit()
#FOR LOGIN    
def logindatabase(username,passwd):
    sql = "SELECT * FROM USER_INFO WHERE USERNAME = %s"
    val = (username,)
    mycursor.execute(sql,val)
    logindata = mycursor.fetchall()
    for i in logindata:
        if passwd == i[3]:
            return True
#FOR HISTORICAL DATA    
def get_his(curname,interval):#interval = 1d,1week,1month,1year 
    #if want more data points use start and end in .get()
    if interval == '1d':
        data = requests.get("http://api.coincap.io/v2/assets/"+f'{curname}'+"/history?interval=m1")
        data = data.json()
        for i in data['data']:
            print(i['priceUsd'],i['time'])
    elif interval == '1w':
        data = requests.get("http://api.coincap.io/v2/assets/"+f'{curname}'+"/history?interval=m15")
        data = data.json()
        for i in data['data']:
            print(i['priceUsd'],i['time'])
    elif interval == '1m':
        data = requests.get("http://api.coincap.io/v2/assets/"+f'{curname}'+"/history?interval=h1")
        data = data.json()
        for i in data['data']:
            print(i['priceUsd'],i['time'])
    elif interval == '1y':
        data = requests.get("http://api.coincap.io/v2/assets/"+f'{curname}'+"/history?interval=h12")
        data = data.json()
        for i in data['data']:
            print(i['priceUsd'],i['time'])
#adding cur to watchlist
def addtowatchlist(username,curname):
    data = requests.get("http://api.coincap.io/v2/assets/"+f'{curname}')
    data = data.json()
    a = data['data']
    sql = f"INSERT INTO WATCHLIST VALUES('{username}','{a['symbol']}','{a['name']}',{Decimal(a['priceUsd'])},{Decimal(a['supply'])},{Decimal(a['marketCapUsd'])},{Decimal(a['volumeUsd24Hr'])})"
    mycursor.execute(sql)
    mydb.commit()
