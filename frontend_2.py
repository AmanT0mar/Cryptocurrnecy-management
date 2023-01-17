from decimal import Decimal
import requests
import json
import pandas as pd
import tkinter as tk
import backend as bef
import mysql.connector
import customtkinter as CTk

mydb = mysql.connector.connect(host = "localhost", user="Aman", database = "myproj")
mycursor = mydb.cursor()

general_font=('Times New Roman', 18)
small_font=('Times New Roman', 15)
large_font = ('Times New Roman', 30)
current_theme='dark'
class MainWin:
    def __init__(self):
        self.win = CTk.CTk()
        self.win.state("zoomed")
        self.win.title("CRYPTOCURRENCY PORTFOLIO MANAGEMENT")
        self.frame = CTk.CTkFrame(self.win,
                                  width=1100,height=860)
        self.frame.place(x=370,y=0)
        # self.bg = CTk.CTkImage(Image.open("back_1.jpg"),size=(1100,860))                          
        # self.bgframe = CTk.CTkLabel(self.frame,text="",image=self.bg)
        # self.bgframe.place(x=0,y=0)
        self.user_ = CTk.CTkLabel(self.frame,
                                  text="CRYPTOCURRENCY PORTFOLIO MANAGEMENT",
                                  justify='center',
                                  text_color='#308849',
                                  font=large_font)
        self.user_.place(x=120,y=150)

    def login(self):
        self.label0 = CTk.CTkLabel(self.win,text="WELCOME",font =large_font)
        self.label0.place(x=120,y=30)
        self.login_frame = CTk.CTkFrame(self.win,
                                        width=350,height=400)
        self.login_frame.place(x=10,y=150)
        self.title = CTk.CTkLabel(self.login_frame,
                                  text="LOGIN",
                                  font=('Times New Roman',28))
        self.title.place(x=130,y=20)
        
        self.name_varl = tk.StringVar()
        self.passwd_varl = tk.StringVar()
    
        self.login_label1 = CTk.CTkLabel(self.login_frame,
                                        text="USERNAME",
                                        font=small_font).place(x=20,y=100)
        self.login_entry1 = CTk.CTkEntry(self.login_frame,
                                        textvariable=self.name_varl,
                                        width=200,
                                        height=30).place(x=130,y=100)
        
        self.login_label2 = CTk.CTkLabel(self.login_frame,  
                                        text="PASSWORD",
                                        font=small_font).place(x=20,y=160)
        self.login_entry2 = CTk.CTkEntry(self.login_frame,
                                        textvariable=self.passwd_varl,
                                        show="*",
                                        width=200,
                                        height=30).place(x=130,y=160)

        self.login_but = CTk.CTkButton(self.login_frame,
                                       text="LOG IN",
                                       command=self.check_login,
                                       height=40,
                                       width=150,
                                       corner_radius=18,
                                       hover_color= "#009A1F",
                                       fg_color = "#00AF23").place(x=100,y=250)
                                       
        self.signup_but = CTk.CTkButton(self.login_frame,
                                       text="SIGN UP",
                                       command=self.signup,
                                       height=40,
                                       width=150,
                                       corner_radius=18,
                                       hover_color= "#009A1F",
                                       fg_color = "#00AF23").place(x=100,y=310)
    def signup(self):
        
        self.signup_win = CTk.CTkToplevel(self.win)
        self.signup_win.geometry("580x500")
        
        self.fullname_var = tk.StringVar()
        self.name_var = tk.StringVar()
        self.phno_var = tk.StringVar()
        self.passwd_var = tk.StringVar()
        self.passwd2_var = tk.StringVar()
    
        self.signup_win.title("CRYPTOCURRENCY PORTFOLIO MANAGEMENT")

        self.signup_win_label1 = CTk.CTkLabel(self.signup_win,
                                              text="SIGN UP",
                                              justify='center',
                                              font=large_font).place(x=200,y=70)
    
        self.signup_win_label2 = CTk.CTkLabel(self.signup_win,
                                              text="FULLNAME",
                                              font=small_font).place(x=80,y=130)
        self.signup_win_entry2 = CTk.CTkEntry(self.signup_win,
                                              textvariable=self.fullname_var,
                                              width=200).place(x=220,y=130)
        
        self.signup_win_label3 = CTk.CTkLabel(self.signup_win,
                                              text="USERNAME",
                                              font=small_font).place(x=80,y=170)

        self.signup_win_entry3 = CTk.CTkEntry(self.signup_win,
                                              textvariable=self.name_var,
                                              width=200).place(x=220,y=170)
        
        self.signup_win_label4 = CTk.CTkLabel(self.signup_win,
                                              text="PHONE NO.",
                                              font=small_font).place(x=80,y=210)
        self.signup_win_entry4 = CTk.CTkEntry(self.signup_win,
                                              textvariable=self.phno_var,
                                              width=200).place(x=220,y=210)
        
        self.signup_win_label5 = CTk.CTkLabel(self.signup_win,
                                              text="PASSWORD",
                                              font=small_font).place(x=80,y=250)
        self.signup_win_entry5 = CTk.CTkEntry(self.signup_win, 
                                              textvariable=self.passwd_var,
                                              show="*",
                                              width=200).place(x=220,y=250)
        
        self.signup_win_label6 = CTk.CTkLabel(self.signup_win,
                                              text="RE-ENTER\nPASSWORD",
                                              font=small_font).place(x=80,y=290)
        self.signup_win_entry6 = CTk.CTkEntry(self.signup_win,  
                                              textvariable=self.passwd2_var,
                                              show="*",
                                              width=200).place(x=220,y=290)

    
        self.signup_win_button1 = CTk.CTkButton(self.signup_win,text="SIGN UP",
                                                height=50,width=150,
                                                font=small_font,
                                                corner_radius=18,
                                                hover_color= "#009A1F",
                                                fg_color = "#00AF23",
                                                command=self.signing).place(x=200,y=380)
                            
    def signing(self):

        self.fullname = self.fullname_var.get()
        self.username = self.name_var.get()
        self.phno = self.phno_var.get()
        self.passwd = self.passwd_var.get()
        self.passwd2 = self.passwd2_var.get()

        if self.fullname == "" or self.username == "" or self.phno == "" or self.passwd == "" :
            self.non = CTk.CTkLabel(self.signup_win,
                                    text="*FIELD IS EMPTY*",
                                    text_color='#f00',
                                    font=small_font).place(x=190,y=340)
        else:
            if bef.selectfromusers(self.username) != None:
                self.ue = CTk.CTkLabel(self.signup_win,
                                    text="*USERNAME ALREADY EXIST*",
                                    text_color='#f00',
                                    font=small_font).place(x=430,y=170)
                self.name_var.set("")
        
            elif len(self.phno) != 10:
                self.wpn = CTk.CTkLabel(self.signup_win,
                                        text="*INVALID PHONE NUMBER*",
                                        text_color='#f00',
                                        font=small_font).place(x=430,y=210)
                
            elif self.passwd != self.passwd2 :
                self.wp = CTk.CTkLabel(self.signup_win,
                                    text="*PASSWORD DOESN'T MATCH*",
                                    text_color='#f00',
                                    font=small_font).place(x=430,y=290)
                self.passwd_var.set("")
                self.passwd2_var.set("")
                
            else:
                bef.insertintousers(self.fullname,self.username,self.phno,self.passwd)

                self.fullname_var.set("")
                self.name_var.set("")
                self.phno_var.set("")
                self.passwd_var.set("")
                self.passwd2_var.set("")
        
    def check_login(self):
        self.name = self.name_varl.get()
        self.passwdl = self.passwd_varl.get()
        
        if bef.logindatabase(self.name,self.passwdl) == True:
            print("successfully logged in")
            # self.login_frame.destroy()
            # self.win.destroy()
            #MainFrame(self.name)   
        else:
            self.ue2 = CTk.CTkLabel(self.login_frame,text="USERNAME AND PASSWORD DOESN'T MATCH",text_color='#f00',font=small_font)
            self.ue2.place(x=10,y=200)
            self.name_varl.set("")
            self.passwd_varl.set("")
            
if __name__=='__main__':
    app=MainWin()
    app.login()
    app.win.mainloop()
