import tkinter as tk
import backendfunction as bef
import mysql.connector

mydb = mysql.connector.connect(host = "localhost", user="Aman", database = "mydb")
mycursor = mydb.cursor()


class MainWin:
    def __init__(self):
        self.win = tk.Tk()
        self.win.geometry("900x600")

        self.win.title("CRYPTOCURRENCY PORTFOLIO MANAGEMENT")
        self.user_ = tk.Label(self.win,text="CRYPTOCURRENCY PORTFOLIO MANAGEMENT",justify='center',fg='#308849',font=('Times 20')).place(x=180,y=150)

        self.login_button = tk.Button(self.win,text="LOG IN",height=2,width=10,command=self.login)
        self.login_button.place(x=300,y=400)

        self.signup_button = tk.Button(self.win,text="SIGN UP",height=2,width=10,command=self.signup)
        self.signup_button.place(x=500,y=400)

        self.win.mainloop()
        
    def signup(self):
        
        self.signup_win = tk.Toplevel()
        self.signup_win.geometry("700x700")
        
        self.fullname_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.phno_var = tk.StringVar()
        self.passwd_var = tk.StringVar()
        self.passwd2_var = tk.StringVar()
    
        self.signup_win.title("CRYPTOCURRENCY PORTFOLIO MANAGEMENT")
        self.signup_win_label1 = tk.Label(self.signup_win,text="SIGN UP",justify='center',font=('Times 18')).place(x=150,y=80)
    
        self.signup_win_label2 = tk.Label(self.signup_win,text="FULLNAME").place(x=100,y=130)
        self.signup_win_entry2 = tk.Entry(self.signup_win,textvariable=self.fullname_var,width=20).place(x=230,y=130)
        
        self.signup_win_label3 = tk.Label(self.signup_win,text="USERNAME").place(x=100,y=160)
        self.signup_win_entry3 = tk.Entry(self.signup_win,textvariable=self.name_var,width=20).place(x=230,y=160)
        
        self.signup_win_label4 = tk.Label(self.signup_win,text="PHONE NO.").place(x=100,y=190)
        self.signup_win_entry4 = tk.Entry(self.signup_win,textvariable=self.phno_var,width=20).place(x=230,y=190)
        
        self.signup_win_label5 = tk.Label(self.signup_win,text="PASSWORD").place(x=100,y=220)
        self.signup_win_entry5 = tk.Entry(self.signup_win,textvariable=self.passwd_var,show="*",width=20).place(x=230,y=220)
        
        self.signup_win_label6 = tk.Label(self.signup_win,text="RE-ENTER PASSWORD").place(x=100,y=250)
        self.signup_win_entry6 = tk.Entry(self.signup_win,textvariable=self.passwd2_var,show="*",width=20).place(x=230,y=250)

    
        self.signup_win_button1 = tk.Button(self.signup_win,text="SIGN UP",height=2,width=8,command=self.signing).place(x=150,y=350)
        
    def signing(self):
        self.fullname = self.fullname_var.get()
        self.username = self.name_var.get()
        self.phno = self.phno_var.get()
        self.passwd = self.passwd_var.get()
        self.passwd2 = self.passwd2_var.get()
        
        if bef.selectfromusers(self.username) != None:
            self.ue = tk.Label(self.signup_win,text="*USERNAME ALREADY EXIST*",fg='#f00',font=('Times 10')).place(x=360,y=160)
      
        if len(self.phno)>10 or len(self.phno)<10:
            self.wpn = tk.Label(self.signup_win,text="*INVALID PHONE NUMBER*",fg='#f00',font=('Times 10')).place(x=360,y=190)
            
        if self.passwd != self.passwd2:
            self.wp = tk.Label(self.signup_win,text="*PASSWORD DOESN'T MATCH*",fg='#f00',font=('Times 10')).place(x=360,y=250)
        
        elif self.fullname!=None or self.username!=None or self.phno!=None or self.passwd!=None:
            self.non = tk.Label(self.signup_win,text="*FIELD IS EMPTY*",fg='#f00',font=('Times 10')).place(x=150,y=300)
        
        else:
            bef.insertintousers(self.fullname,self.username,self.phno,self.passwd)
            
        self.fullname_var.set("")
        self.name_var.set("")
        self.phno_var.set("")
        self.passwd_var.set("")
        self.passwd2_var.set("")
        
    def login(self):
    
        self.login_win = tk.Toplevel()
        self.login_win.geometry("700x700")
        self.login_win.title("CRYPTOCURRENCY PORTFOLIO MANAGEMENT")
        self.login_label = tk.Label(self.login_win,text="LOG IN",justify='center',font=('Times 18')).place(x=150,y=100)
    
        self.name_var = tk.StringVar()
        self.passwd_var = tk.StringVar()
    
        self.login_label1 = tk.Label(self.login_win,text="USERNAME").place(x=100,y=150)
        self.login_entry1 = tk.Entry(self.login_win,textvariable=self.name_var,width=20).place(x=230,y=150)
        
        self.login_label2 = tk.Label(self.login_win,text="PASSWORD").place(x=100,y=180)
        self.login_entry2 = tk.Entry(self.login_win,textvariable=self.passwd_var,show="*",width=20).place(x=230,y=180)

        self.login_but = tk.Button(self.login_win,text="LOG IN",height=2,width=8,command=self.check_login).place(x=150,y=300)
    
    def check_login(self):
        self.name = self.name_var.get()
        self.passwd = self.passwd_var.get()

        if bef.logindatabase(self.name,self.passwd) == True:
            self.login_win.destroy()
            self.win.destroy()
            MainFrame(self.name)
        else:
            self.ue2 = tk.Label(self.login_win,text="USERNAME AND PASSWORD DOESN'T MATCH",fg='#f00',font=('Times 10'))
            self.ue2.place(x=360,y=150)
        
        self.passwd_var.set("")
        
        
# M A I N F R A M E        
           
if __name__=="__main__":
        abc = MainWin()
        abc.win.mainloop()
