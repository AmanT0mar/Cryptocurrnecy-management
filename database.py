import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user="Aman", database = "mydb")
mycursor = mydb.cursor()

mycursor.execute("""CREATE TABLE IF NOT EXISTS SELL_OUT
                (USERNAME VARCHAR(30),
                SYMBOL VARCHAR(7),
                CURNAME VARCHAR(15),
                PRICE DECIMAL(22,16),
                QUANTITY DECIMAL(8,3),
                TOTAL_RETURNS DECIMAL(15,8),
                SELL_TIME TIMESTAMP,
                CONSTRAINT PK_S PRIMARY KEY(USERNAME,CURNAME,QUANTITY,SELL_TIME),
                CONSTRAINT FK_S FOREIGN KEY(USERNAME) REFERENCES USER_INFO(USERNAME) ON DELETE CASCADE)""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS BOUGHT
                 (USERNAME VARCHAR(30),
                 SYMBOL VARCHAR(7),
                 CURNAME VARCHAR(15),
                 PRICE DECIMAL(22,16),
                 QUANTITY DECIMAL(8,3),
                 TOTAL_PRICE DECIMAL(15,8),
                 BUY_TIME TIMESTAMP,
                 CONSTRAINT PK_B PRIMARY KEY(USERNAME,CURNAME,BUY_TIME),
                 CONSTRAINT FK_B FOREIGN KEY(USERNAME) REFERENCES USER_INFO (USERNAME) ON DELETE CASCADE)""")

mycursor.execute("""CREATE TABLE IF NOT EXISTS WATCHLIST
                 (USERNAME VARCHAR(30),
                 SYMBOL VARCHAR(7),
                 CURNAME VARCHAR(15),
                 PRICE DECIMAL(22,16),
                 SUPPLY DECIMAL(26,16),
                 MARKETCAP DECIMAL(35,16),
                 VOLUME DECIMAL(35,16),
                 CONSTRAINT PK_B PRIMARY KEY(USERNAME,CURNAME),
                 CONSTRAINT FK_B FOREIGN KEY(USERNAME) REFERENCES USER_INFO (USERNAME) ON DELETE CASCADE)""")
mycursor.execute(""" CREATE TABLE IF NOT EXISTS HOLDING
                 (USERNAME VARCHAR(30),
                 SYMBOL VARCHAR(7),
                 CURNAME VARCHAR(15),
                 CUR_PRICE DECIMAL(22,16),
                 QUANTITY DECIMAL(8,3),
                 INVESTED DECIMAL(30,16),
                 RETURNS DECIMAL(30,16),
                 CONSTRAINT PK_H PRIMARY KEY(USERNAME,CURNAME,QUANTITY),
                 CONSTRAINT FK_H FOREIGN KEY(USERNAME) REFERENCES USER_INFO(USERNAME) ON DELETE CASCADE)""")

mydb.commit()  
