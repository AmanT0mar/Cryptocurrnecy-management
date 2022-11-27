import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user="Aman", database = "mydb")
mycursor = mydb.cursor()

def selectfromusers(username):
    sql = "SELECT * FROM USER_INFO WHERE USERNAME = %s "
    val = (username,)
    mycursor.execute(sql,val)
    userdata = mycursor.fetchall()
    for i in userdata:
        return i
        
def insertintousers(fullname,username,phno,passwd):
    sql = "INSERT INTO USER_INFO VALUES(%s,%s,%s,%s)"
    val = (fullname,username,phno,passwd,)
    mycursor.execute(sql,val)
    mydb.commit()
    
def logindatabase(username,passwd):
    sql = "SELECT * FROM USER_INFO WHERE USERNAME = %s"
    val = (username,)
    mycursor.execute(sql,val)
    logindata = mycursor.fetchall()
    for i in logindata:
        if passwd == i[3]:
            return True

def 
        
