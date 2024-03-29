import mysql.connector


mydb = mysql.connector.connect(host = "localhost", user="Aman")
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS MYDB")
mydb.commit()  

mydb = mysql.connector.connect(host = "localhost", user="Aman", database = "MYDB")
mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE IF NOT EXISTS USER_INFO
                (FULLNAME VARCHAR(30) NOT NULL,
                USERNAME VARCHAR(30) NOT NULL,
                PHONENO BIGINT(10) NOT NULL,
                PASSWORD VARCHAR(256) NOT NULL,
                BALANCE DECIMAL(45,16) NOT NULL,
                CONSTRAINT PK_U PRIMARY KEY(USERNAME))""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS SELL_OUT
                (USERNAME VARCHAR(30) NOT NULL,
                SYMBOL VARCHAR(7) NOT NULL,
                CURNAME VARCHAR(15) NOT NULL,
                PRICE DECIMAL(32,16) NOT NULL,
                QUANTITY DECIMAL(12,3) NOT NULL,
                TOTAL_RETURNS DECIMAL(32,16) NOT NULL,
                SELL_TIME TIMESTAMP NOT NULL,
                CONSTRAINT PK_S PRIMARY KEY(USERNAME,CURNAME,QUANTITY,SELL_TIME),
                CONSTRAINT FK_S FOREIGN KEY(USERNAME) REFERENCES USER_INFO(USERNAME) ON DELETE CASCADE)""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS BOUGHT
                 (USERNAME VARCHAR(30) NOT NULL,
                 SYMBOL VARCHAR(7) NOT NULL,
                 CURNAME VARCHAR(15) NOT NULL,
                 PRICE DECIMAL(32,16) NOT NULL,
                 QUANTITY DECIMAL(12,3) NOT NULL,
                 TOTAL_PRICE DECIMAL(32,16) NOT NULL,
                 BUY_TIME TIMESTAMP NOT NULL,
                 CONSTRAINT PK_B PRIMARY KEY(USERNAME,CURNAME,BUY_TIME),
                 CONSTRAINT FK_B FOREIGN KEY(USERNAME) REFERENCES USER_INFO (USERNAME) ON DELETE CASCADE)""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS WATCHLIST
                 (USERNAME VARCHAR(30) NOT NULL,
                 SYMBOL VARCHAR(7) NOT NULL,
                 CURNAME VARCHAR(15) NOT NULL,
                 PRICE DECIMAL(32,16) NOT NULL,
                 SUPPLY DECIMAL(32,16) NOT NULL,
                 MARKETCAP DECIMAL(32,16) NOT NULL,
                 VOLUME DECIMAL(32,16) NOT NULL,
                 CONSTRAINT PK_W PRIMARY KEY(USERNAME,CURNAME),
                 CONSTRAINT FK_W FOREIGN KEY(USERNAME) REFERENCES USER_INFO (USERNAME) ON DELETE CASCADE)""")
mycursor.execute(""" CREATE TABLE IF NOT EXISTS HOLDING
                 (USERNAME VARCHAR(30) NOT NULL,
                 SYMBOL VARCHAR(7) NOT NULL,
                 CURNAME VARCHAR(15) NOT NULL,
                 CUR_PRICE DECIMAL(32,16) NOT NULL,
                 QUANTITY DECIMAL(12,3) NOT NULL,
                 INVESTED DECIMAL(32,16) NOT NULL,
                 PER_COIN DECIMAL(32,16) NOT NULL,
                 RETURNS DECIMAL(32,16),
                 CONSTRAINT PK_H PRIMARY KEY(USERNAME,CURNAME,QUANTITY),
                 CONSTRAINT FK_H FOREIGN KEY(USERNAME) REFERENCES USER_INFO(USERNAME) ON DELETE CASCADE)""")
mycursor.execute("""CREATE TABLE IF NOT EXISTS COINS
                (CNAME VARCHAR(25) NOT NULL,
                CID VARCHAR(25) NOT NULL,
                CSYMBOL VARCHAR(25) NOT NULL,
                CIMAGE VARCHAR(10),
                CONSTRAINT PK_I PRIMARY KEY(CID))""")
mycursor.execute("""CREATE TABLE IF NOT EXISTS BALANCE
                 (USERNAME VARCHAR(30) NOT NULL,
                  ACTION VARCHAR(30) NOT NULL,
                  AMOUNT DECIMAL(45,16) NOT NULL,
                  TIME TIMESTAMP NOT NULL,
                  CONSTRAINT PK_B PRIMARY KEY(USERNAME,TIME),
                  CONSTRAINT FK_Bl FOREIGN KEY(USERNAME) REFERENCES USER_INFO(USERNAME) ON DELETE CASCADE)""")
mydb.commit()  
