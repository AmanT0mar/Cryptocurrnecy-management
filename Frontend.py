from decimal import Decimal
import requests
import json
import pandas as pd
import tkinter as tk
import re
import backend as bef
import mysql.connector
import customtkinter as CTk
from tkinter import ttk
from PIL import ImageTk,Image 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
mydb = mysql.connector.connect(host = "localhost", user="Aman", database = "myproj")
mycursor = mydb.cursor()

general_font=('Times New Roman', 18)
small_font=('Times New Roman', 15)
large_font = ('Times New Roman', 30)
current_theme='dark'
#WINDOW FOR LOGIN/SIGNUP
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
            self.login_frame.destroy()
            self.win.destroy()
            MainWindow(self.name)   
        else:
            self.ue2 = CTk.CTkLabel(self.login_frame,text="USERNAME AND PASSWORD DOESN'T MATCH",text_color='#f00',font=small_font)
            self.ue2.place(x=10,y=200)
            self.name_varl.set("")
            self.passwd_varl.set("")
#WINDOW FOR TABLES
class MainWindow:
    def __init__(self,username):
        self.username = username
        self.window = CTk.CTk()
        self.frame = CTk.CTkFrame(master=self.window,
                                  width=1250,height=850)
        self.frame.place(x=220,y=0)
        #Window will be at maximum windowed size
        self.window.state('zoomed')
        #Window Title
        self.window.title("Crypto")

        self.user_label = CTk.CTkLabel(master=self.window,text=f"{self.username}",
                          font=large_font)
        self.user_label.place(x=30,y=20)
        dis=90
        #Wishlist Button
        self.wishlist_Button = CTk.CTkButton(master=self.window,
                                             text="Wishlist",
                                             command=self.wishlist_func,
                                             height=50,width=125,
                                             font=general_font)
        self.wishlist_Button.place(x=40,y=100+(dis*0))
        
        #BuyIN Button
        self.buyin_Button = CTk.CTkButton(master=self.window,
                            text="BuyIN",
                            command=self.buyin_func,
                            height=50,width=125,
                            font=general_font)
        self.buyin_Button.place(x=40,y=100+(dis*1))
        
        #Sellout Button
        self.sellout_Button = CTk.CTkButton(master=self.window,
                              text="Sellout",
                              command=self.sellout_func,
                              height=50,width=125,
                              font=general_font)
        self.sellout_Button.place(x=40,y=100+(dis*2))
        
        #Wishlist Button
        self.holdlist_Button = CTk.CTkButton(master=self.window,
                               text="Holdlist",
                               command=self.holdlist_func,
                               height=50,width=125,
                               font=general_font)
        self.holdlist_Button.place(x=40,y=100+(dis*3))
        #Exit button
        self.exit_Button = CTk.CTkButton(master=self.window,
                                        text="Exit",
                                        command=self.exit_func,
                                        height=50,width=70,
                                        font=general_font)
        self.exit_Button.place(x=40,y=100+(dis*4))
        
        
        self.window.mainloop()
    #Methods
    
    #wishlist button function
    def wishlist_func(self):
        self.frame.destroy()
        self.new_frame = wishlist_frame(self.window,self.username)
        
    #BuyIN button function
    def buyin_func(self):
        self.frame.destroy()
        self.new_frame = boughtlist_frame(self.window,self.username)
    #Sellout button function
    def sellout_func(self):
        self.frame.destroy()
        self.new_frame = soldlist_frame(self.window,self.username)   
    #Holdlist button function
    def holdlist_func(self):
        self.frame.destroy()
        self.new_frame = holdlist_frame(self.window,self.username)
    #Exit function
    def exit_func(self):
        self.window.destroy()
        exit()


class wishlist_frame:
    def __init__(self,window,username):
        self.main = window
        self.username = username
        self.frame = CTk.CTkFrame (master=self.main,
                                   width=1300,height=850)
        self.frame.place(x=170,y=0)
        self.title = CTk.CTkLabel(self.frame,
                                  text="Wish List",
                                  font=general_font)
        self.title.place(x=0,y=0)
        #-----------Search Bar--------------
        
        
        #-------------TABLE-----------------
        self.table_frame = CTk.CTkFrame(self.frame,width=1000,height=300)
        self.table_frame.place(x=100,y=100)
        # Create the Treeview
        self.table = ttk.Treeview(self.table_frame, columns=("col1", "col2", "col3", "col4"),height=10)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Times',22))
        style.configure("Treeview", font=general_font,rowheight=70)
        self.table.column("#0",width=70)
        self.table.heading("#0", text="SNO")
        self.table.column("#1",width=180)
        self.table.heading("#1", text="SYMBOL")
        self.table.column("#2",width=200)
        self.table.heading("#2", text="CURRENCY")
        self.table.column("#3",width=500) 
        self.table.heading("#3", text="PRICE")
        self.table.column("#4",width=200)
        self.table.heading("#4", text="QUANTITY")
        self.table_scrollbar = tk.Scrollbar(self.table_frame, orient="vertical", command=self.table.yview)
        self.table_scrollbar.pack(side="right", fill="y")
        self.table.configure(yscrollcommand=self.table_scrollbar.set)
        self.table.bind("<Double-1>", self.OnDoubleClick)
        # Pack the Treeview
        self.table.pack(expand=True, fill="both")
        curs_data = bef.get_curs(self.username,"holding")
        for i in range(len(curs_data)):
            entry=curs_data[i]
            self.table.insert("", "end",iid=i+1, text=i+1, values=entry[1:5])
        # self.new_data=bef.get_his('bitcoin','1d')
        # self.table_frame.after(1000,self.update_values,curs_data)
    def OnDoubleClick(self,event):
        sel_item = self.table.identify('item',event.x,event.y)
        curname = self.table.item(sel_item)['values'][1]
        self.main.withdraw()
        cur_id = bef.get_cur_id(curname)
        self.win = CurrencyDetails(self.main,self.username,cur_id)


class boughtlist_frame:
    def __init__(self,window,username):
        self.window = window
        self.username = username
        self.frame = CTk.CTkFrame (master=self.window,
                                   width=1300,height=850)
        self.frame.place(x=170,y=0)
        self.title = CTk.CTkLabel(self.frame,
                                  text="Bought",
                                  font=general_font)
        self.title.place(x=0,y=0)
        # self.plot_graph = CTk.CTkButton(self.frame,
        #                                 text='Plot',
        #                                 command=self.plot,
        #                                 font=general_font)
        # self.new_data=bef.get_his("bitcoin","1d")
        # self.plot_graph.place(x=300,y=10)
        #-------------TABLE-----------------
        self.table_frame = CTk.CTkFrame(self.frame,width=1000,height=300)
        self.table_frame.place(x=70,y=100)
        # Create the Treeview
        self.table = ttk.Treeview(self.table_frame, columns=("col1", "col2", "col3", "col4","col5"),height=10)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Times',22))
        style.configure("Treeview", font=general_font,rowheight=50)
        self.table.column("#0",width=70)
        self.table.heading("#0", text="SNO")
        self.table.column("#1",width=180)
        self.table.heading("#1", text="SYMBOL")
        self.table.column("#2",width=200)
        self.table.heading("#2", text="CURRENCY")
        self.table.column("#3",width=500)
        self.table.heading("#3", text="PRICE")
        self.table.column("#4",width=200)
        self.table.heading("#4", text="QUANTITY")
        self.table.column("#5",width=200)
        self.table.heading("#5", text="TOTAL PRICE")
        self.table_scrollbar = tk.Scrollbar(self.table_frame, orient="vertical", command=self.table.yview)
        self.table_scrollbar.pack(side="right", fill="y")
        self.table.configure(yscrollcommand=self.table_scrollbar.set)
        self.table.bind("<Double-1>", self.OnDoubleClick)
        # Pack the Treeview
        self.table.pack(expand=True, fill="both")
        curs_data = bef.get_curs("thejabh","bought")
        for i in range(len(curs_data)):
            entry=curs_data[i]
            self.table.insert("", "end",iid=i+1, text=i+1, values=entry[1:6])
    
    # def OnDoubleClick(self,event):
    #     sel_item = self.table.identify('item',event.x,event.y)
    #     cur = self.table.item(sel_item)['values'][1]
    #     self.plot_window(cur)

class soldlist_frame:
    def __init__(self,window,username):
        self.window = window
        self.username = username
        self.frame = CTk.CTkFrame (master=self.window,
                                   width=1300,height=850)
        self.frame.place(x=170,y=0)
        self.title = CTk.CTkLabel(self.frame,
                                  text="Bought",
                                  font=general_font)
        self.title.place(x=0,y=0)
        # self.plot_graph = CTk.CTkButton(self.frame,
        #                                 text='Plot',
        #                                 command=self.plot,
        #                                 font=general_font)
        # self.new_data=bef.get_his("bitcoin","1d")
        # self.plot_graph.place(x=300,y=10)
        #-------------TABLE-----------------
        self.table_frame = CTk.CTkFrame(self.frame,width=1000,height=300)
        self.table_frame.place(x=70,y=100)
        # Create the Treeview
        self.table = ttk.Treeview(self.table_frame, columns=("col1", "col2", "col3", "col4","col5"),height=10)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Times',22))
        style.configure("Treeview", font=general_font,rowheight=50)
        self.table.column("#0",width=70)
        self.table.heading("#0", text="SNO")
        self.table.column("#1",width=180)
        self.table.heading("#1", text="SYMBOL")
        self.table.column("#2",width=200)
        self.table.heading("#2", text="CURRENCY")
        self.table.column("#3",width=500)
        self.table.heading("#3", text="PRICE")
        self.table.column("#4",width=200)
        self.table.heading("#4", text="QUANTITY")
        self.table.column("#5",width=300)
        self.table.heading("#5", text="TOTAL RETURNS")
        self.table_scrollbar = tk.Scrollbar(self.table_frame, orient="vertical", command=self.table.yview)
        self.table_scrollbar.pack(side="right", fill="y")
        self.table.configure(yscrollcommand=self.table_scrollbar.set)
        self.table.bind("<Double-1>", self.OnDoubleClick)
        # Pack the Treeview
        self.table.pack(expand=True, fill="both")
        curs_data = bef.get_curs("thejabh","sell_out")
        for i in range(len(curs_data)):
            entry=curs_data[i]
            self.table.insert("", "end",iid=i+1, text=i+1, values=entry[1:6])
    
    # def OnDoubleClick(self,event):
    #     sel_item = self.table.identify('item',event.x,event.y)
    #     cur = self.table.item(sel_item)['values'][1]
    #     self.plot_window(cur)

class holdlist_frame:
    def __init__(self,main,username):
        
        self.main = main
        self.username = username
        self.frame = CTk.CTkFrame (master=self.window,
                                   width=1300,height=850)
        self.frame.place(x=170,y=0)
        self.title = CTk.CTkLabel(self.frame,
                                  text="Holding",
                                  font=general_font)
        self.title.place(x=0,y=0)
        # self.plot_graph = CTk.CTkButton(self.frame,
        #                                 text='Plot',
        #                                 command=self.plot,
        #                                 font=general_font)
        # self.new_data=bef.get_his("bitcoin","1d")
        # self.plot_graph.place(x=300,y=10)
        #-------------TABLE-----------------
        self.table_frame = CTk.CTkFrame(self.frame,width=1000,height=300)
        self.table_frame.place(x=70,y=100)
        # Create the Treeview
        self.table = ttk.Treeview(self.table_frame, columns=("col1", "col2", "col3", "col4","col5"),height=10)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Times',22))
        style.configure("Treeview", font=general_font,rowheight=50)
        self.table.column("#0",width=70)
        self.table.heading("#0", text="SNO")
        self.table.column("#1",width=180)
        self.table.heading("#1", text="SYMBOL")
        self.table.column("#2",width=200)
        self.table.heading("#2", text="CURRENCY")
        self.table.column("#3",width=500)
        self.table.heading("#3", text="PRICE")
        self.table.column("#4",width=200)
        self.table.heading("#4", text="QUANTITY")
        self.table_scrollbar = tk.Scrollbar(self.table_frame, orient="vertical", command=self.table.yview)
        self.table_scrollbar.pack(side="right", fill="y")
        self.table.configure(yscrollcommand=self.table_scrollbar.set)
        self.table.bind("<Double-1>", self.OnDoubleClick)
        # Pack the Treeview
        self.table.pack(expand=True, fill="both")
        curs_data = bef.get_curs("thejabh","holding")
        for i in range(len(curs_data)):
            entry=curs_data[i]
            self.table.insert("", "end",iid=i+1, text=i+1, values=entry[1:6])
    
    def OnDoubleClick(self,event):
        sel_item = self.table.identify('item',event.x,event.y)
        curname = self.table.item(sel_item)['values'][1]
        self.main.withdraw()
        cur_id = bef.get_cur_id(curname)
        self.win = CurrencyDetails(self.main,self.username,cur_id)

class CurrencyDetails:
    def __init__(self,main_win,username,curname):
        self.main=main_win
        global btnState
        btnState=False# initially navbar is closed
        
        self.username = username
        self.curname = curname
        
        # self.root = CTk.CTk()
        self.root = CTk.CTk()
        self.root.state("zoomed")
        self.mainframe = CTk.CTkFrame(self.root,width=1500,height=1000)
        self.mainframe.place(x=0,y=0)
        self.gLabel1 = CTk.CTkLabel(self.mainframe,text=f'{self.curname}',font=('Courier',30))
        self.gLabel1.place(x=70,y=60)
        self.gLabel2 = CTk.CTkLabel(self.mainframe,text="PRICE",font=('Courier',30))
        self.gLabel2.place(x=70,y=100)
        self.gLabel3 = CTk.CTkLabel(self.mainframe,text="Profit/Loss",font=('Courier',15))
        self.gLabel3.place(x=70,y=130)
        self.gbutton6 = CTk.CTkButton(self.mainframe,text="❤",font=('Times',20),width=40,command = self.pressed)
        self.gbutton6.place(x=600,y=60)
        
        #Button to choose time
        self.tab_view = CTk.CTkTabview(self.mainframe,width=600,height=450,
                                       command=lambda:self.graphing(self.tab_view.get().lower(),
                                                                    self.tab_view.tab(self.tab_view.get())))
        self.tab_view.place(x=100,y=250)
        self.tab_view.add('1D')
        self.tab_view.add('1W')
        self.tab_view.add('1M')
        self.tab_view.add('1Y')
        self.tab_view.set('1D')
        color='grey23'
        #menu frame
        self.menu = CTk.CTkFrame(self.mainframe,fg_color='grey13',width=1500,height=50)
        self.menu.place(x=0,y=0)
        self.exit_but = CTk.CTkButton(self.menu,text="X",width=50,height=50,command = self.exit_)
        self.exit_but.place(x=1370,y=0)
        #--------navigation profile-------------
        self.gButton5 = CTk.CTkButton(self.menu,width=50,height=50,text='=',
                                      font=('Courier',40),
                                      command=self.switch)
        self.gButton5.place(x=1420,y=0)
        self.navRoot= CTk.CTkFrame(self.mainframe,fg_color=color, height=900, width=400)
        self.navRoot.place(x=1600,y=40)
       
        CTk.CTkLabel(self.navRoot,text=self.username,font=general_font,width=300,height=50).place(x=10,y=10)
        
        #option widgets inside navbar  
        
        CTk.CTkButton(self.navRoot,text='PROFILE',width=300,height=50,font=general_font,
                      hover_color='OliveDrab2',text_color='black',fg_color=color,command=lambda: self.pro(self.username)).place(x=-10,y=200)
        CTk.CTkButton(self.navRoot,text='WISHLIST',width=300,height=50,font=general_font,
                      hover_color='RoyalBlue2',text_color='black',fg_color=color,command=lambda: self.back_to_main(self.main.wishlist_func)).place(x=-10,y=249)
        CTk.CTkButton(self.navRoot,text='HOLDING',width=300,height=50,font=general_font,
                      hover_color='yellow',text_color='black',fg_color=color,command=lambda: self.back_to_main(self.holdlist_func)).place(x=-10,y=298)
        CTk.CTkButton(self.navRoot,text='BUYIN',width=300,height=50,font=general_font,
                      hover_color='yellow',text_color='black',fg_color=color,command=lambda: self.back_to_main(self.buyin_func)).place(x=-10,y=298)
        CTk.CTkButton(self.navRoot,text='SELLOUT',width=300,height=50,font=general_font,
                      hover_color='yellow',text_color='black',fg_color=color,command=lambda: self.back_to_main(self.sellout_func)).place(x=-10,y=298)
        CTk.CTkButton(self.navRoot,text='LOG OUT',width=300,height=50,font=general_font,
                      hover_color='white',text_color='black',fg_color=color,command=lambda: self.back_to_main(self.main.wishlist_func)).place(x=-10,y=495)
        
        
        

        #curent data
        self.curquant = bef.coinquant(self.username,self.curname)
        self.cLabel1 = CTk.CTkLabel(self.mainframe,text = f"CURRENT QUANTITY: {self.curquant}",font=('Courier',20))
        self.cLabel1.place(x=900,y=450)

        #selling
        self.sellingc = CTk.CTkButton(self.mainframe,text="SELL",font=('Courier',20),command=self.selling)
        self.sellingc.place(x=800,y=620)

        #buying
        self.buyingc = CTk.CTkButton(self.mainframe,text="BUY",font=('Courier',20),command=self.buying)
        self.buyingc.place(x=1000,y=620)

        #initially 24hrs graph
        self.graphing('1d',self.tab_view.tab('1D'))
        
        # #search bar 
        # self.my_list=['1inch Network', 'Aave', 'Algorand', 'Arweave', 'Avalanche', 'Axie Infinity', 'Balancer', 'Basic Attention Token', 'BNB', 'Binance USD', 'Bitcoin', 'Bitcoin BEP2', 'Bitcoin Cash', 'Bitcoin Gold', 'Bitcoin SV', 'Cardano', 'Casper', 'Celo', 'Chainlink', 'Chiliz', 'Compound', 'Convex Finance', 'Cosmos', 'Crypto.com Coin', 'Curve DAO Token', 'Dash', 'Decentraland', 'Decred', 'Dogecoin', 'eCash', 'MultiversX', 'Enjin Coin', 'EOS', 'Ethereum', 'Ethereum Classic', 'Fantom', 'Fei Protocol', 'Filecoin', 'Flow', 'Frax', 'Frax Share', 'FTX Token', 'Gala', 'GateToken', 'Hedera Hashgraph', 'Helium', 'Holo', 'Huobi Token', 'Internet Computer', 'IOTA', 'Kava', 'Klaytn', 'KuCoin Token', 'Kusama', 'Lido DAO', 'Litecoin', 'Loopring', 'Maker', 'Mina', 'Monero', 'Multi Collateral DAI', 'NEAR Protocol', 'NEM', 'Neo', 'Nexo', 'Oasis Network', 'OKB', 'PancakeSwap', 'Polkadot', 'Polygon', 'Quant', 'Ravencoin', 'Rocket Pool', 'Shiba Inu', 'Solana', 'Stacks', 'Stellar', 'SushiSwap', 'Synthetix', 'Terra', 'Tether', 'Tezos', 'The Graph', 'The Sandbox', 'THETA', 'Theta Fuel', 'THORChain', 'TRON', 'TrueUSD', 'Trust Wallet Token', 'Uniswap', 'UNUS SED LEO', 'USD Coin', 'VeChain', 'WOO Network', 'Wrapped Bitcoin', 'XinFin Network', 'XRP', 'Zcash', 'Zilliqa']

        
        # self.e1_str=tk.StringVar()  # string variable   
        # self.e1=CTk.CTkEntry(self.mainframe,textvariable=self.e1_str,width=250,font=general_font) # entry    
        # self.e1.place(x=300,y=120)
        # self.l1 = tk.Listbox(self.mainframe,height=0,font=general_font,relief='flat',
        # bg='red',highlightcolor= 'SystemButtonFace')
        # self.l1.place(x=300,y=200)
        # self.e1.bind('<Down>', self.my_down) # down arrow key is pressed
        # self.l1.bind('<Right>', self.my_upd) # right arrow key is pressed
        # self.l1.bind('<Return>', self.my_upd)# return key is pressed 
        # self.e1_str.trace('w',self.get_data)

    # def my_upd(self,my_widget): # On selection of option 
    #         my_w = my_widget.widget
    #         index = int(my_w.curselection()[0]) # position of selection
    #         value = my_w.get(index) # selected value 
    #         self.e1_str.set(value) # set value for string variable of Entry 
    #         self.l1.delete(0,tk.END)     # Delete all elements of Listbox
    # def my_down(self,my_widget): # down arrow is clicked 
    #     self.l1.focus()  # move focus to Listbox
    #     self.l1.selection_set(0) # select the first option 
    # def get_data(self,*args): # populate the Listbox with matching options 
    #     search_str=self.e1.get() # user entered string 
    #     self.l1.delete(0,tk.END)     # Delete all elements of Listbox
    #     list_len=0
    #     for i in range(len(self.my_list)):
    #         if(re.match(search_str,self.my_list[i],re.IGNORECASE)):
    #             self.l1.insert(tk.END,self.my_list[i])    #add matching options to Listbox
    #             list_len+=1
    #     self.l1.config(height=list_len)
    def back_to_main(self):
        self.root.withdraw()
        self.main.deiconify()
        self.main.state("zoomed")
    def exit_(self):
            self.root.destroy()
            exit()
    def switch(self):
        global btnState
        if btnState is True:
            # create animated Navbar closing:
            for x in range(1200,1600):
                self.navRoot.place(x=x, y=50)
                self.mainframe.update()
            # turning button OFF:
            btnState = False
        
        else:
            #current balance 
            self.balance = bef.getbalance(f'{self.username}')
            CTk.CTkLabel(self.navRoot,text=f'{self.balance}' + ' USD',font=small_font).place(x=10,y=70)
            # created animated Navbar opening:
            for x in range(1600,1200,-1):
                self.navRoot.place(x=x, y=50)
                self.mainframe.update()

            # turing button ON:
            btnState = True
    
    def selling(self):
        sell_win = CTk.CTkInputDialog(text="Enter the quantity of crypto currency:",title="SELL OUT")
        amt=sell_win.get_input()
        if amt == "":
            self.mes7 = tk.messagebox.showinfo("ERROR","ENTER SOME AMOUNT")
        else:
            self.coinq1 = Decimal(amt)
            self.p1 = bef.current_data(f"{self.curname}")
            self.curp1 = self.p1['price'][0]
            if self.curquant == 0 or self.curquant < 0:
                self.Smes0 = tk.messagebox.showinfo("ERROR MESSAGE","ENTER VALID AMOUNT")
            else:
                if self.coinq1 == 0:
                    self.Smes1 = tk.messagebox.showinfo("INVALID AMOUNT","You Entered 0\nEnter Valid Amount")
                elif self.coinq1 > self.curquant:
                    self.Smes2 = tk.messagebox.showinfo("NOT ENOUGH COINS",f"YOU CURRENT ONLY HOLD {self.curquant}")
                else:
                    self.Smes3 = tk.messagebox.askquestion("SELLING",f"ORDER TO SELL {self.coinq1} AT PRICE {self.curp1}")
                    if self.Smes3 == "yes":
                        bef.selling(self.username,self.curname,self.coinq1)
                        self.curquant = bef.coinquant(self.username,self.curname)
                        self.cLabel1.configure(text=f"CURRENT QUANTITY: {self.curquant}")                

    def buying(self):
        buy_win = CTk.CTkInputDialog(text="Enter the quantity of crypto currency:",title="BUY IN")
        
        self.coinq2 =Decimal(buy_win.get_input())
        self.p2 = bef.current_data(f"{self.curname}")
        self.curp2 = Decimal(self.p2['price'][0])
        if self.coinq2 == 0 or self.coinq2 < 0:
            self.Bmes1 = tk.messagebox.showinfo("INVALID AMOUNT","Enter Valid Amount")
        elif self.balance < self.curp2 * self.coinq2:
            self.maxamt = self.balance/self.curp2
            self.Bmes2 = tk.messagebox.showinfo("NOT ENOUGH FUNDS",f"THE QUANTITY SHOULD BE LESS THAN {self.maxamt}")
        else:
            self.Bmes3 = tk.messagebox.askquestion("BUYING",f"ORDER TO BUY {self.coinq2} AT PRICE {self.curp2}")
            if self.Bmes3 == "yes":
                bef.buying(self.username,self.curname,self.coinq2)
                self.curquant = bef.coinquant(self.username,self.curname)
                self.cLabel1.configure(text=f"CURRENT QUANTITY: {self.curquant}")
       
    def graphing(self,time,tab):
        self.interval = time
        self.curdata = bef.get_his(self.curname,self.interval)

        self.fig = Figure(figsize=(7,5),dpi=100,facecolor='grey')
        self.plot1 = self.fig.add_subplot(111)
        self.plot1.plot(self.curdata['time'],self.curdata['price'])
        self.ax = plt.axes()
        self.ax.set_facecolor("grey")
        self.canvas1 = FigureCanvasTkAgg(self.fig,tab)

        self.canvas1.draw()
        self.canvas1.get_tk_widget().place(x=15,y=10)

    def pro(self,username):
        self.username = username
        a = Profile(self.username)
        a.wallet.mainloop()
        
    def pressed(self):
        if bef.fromwatchlist(self.username,self.curname) == []:
            bef.addtowatchlist(self.username,self.curname)
            self.gbutton6.configure(fg_color ="#00AF23" , hover_color="#00AF23")
        else:
            bef.rmfromwatchlist(self.username,self.curname)
            self.gbutton6.configure(fg_color ="#D10202" , hover_color="#D10202")
        
class Profile:
    def __init__(self,username):
        self.username = username

        self.wallet = CTk.CTkToplevel()
        self.wallet.state("zoomed")

        #user info
        self.ud,self.tinv = bef.userd(self.username)
        self.tinv = (self.tinv*10000000)//1
        self.tot_r = bef.porl(self.username)
        self.tot_r = (self.tot_r*10000000)//1
        self.wlabel0 = CTk.CTkLabel(self.wallet,text=f'HELLO, {self.ud[0][0]}',font=('Courier',30))
        self.wlabel0.place(x=100,y=60)
        self.userd0 = CTk.CTkLabel(self.wallet,text=f"UserID: {self.ud[0][1]}",font=('Courier',20))
        self.userd0.place(x=140,y=140)
        self.userd1 = CTk.CTkLabel(self.wallet,text=f"Phone No: {self.ud[0][2]}",font=('Courier',20))
        self.userd1.place(x=140,y=180)
        self.userd2 = CTk.CTkLabel(self.wallet,text=f"Investment: {self.tinv/10000000}  USD",font=('Courier',20))
        self.userd2.place(x=140,y=220)
        self.userd4 = CTk.CTkLabel(self.wallet,text="Total Returns:",font=('Courier',20))
        self.userd4.place(x=140,y=260)
        if self.tot_r >= 0:
            self.userd3 = CTk.CTkLabel(self.wallet,text=f"{self.tot_r/10000000} USD",font=('Courier',20),text_color="green")
            self.userd3.place(x=320,y=260)
        else:
            self.userd3 = CTk.CTkLabel(self.wallet,text=f"{self.tot_r/10000000} USD",font=('Courier',20),text_color="red")
            self.userd3.place(x=320 ,y=260)
        # self.userpic = ImageTk.PhotoImage(Image.open("profilepic1.png"))
        # self.userlabel = tk.Label(self.wallet,image=self.userpic)
        # self.userlabel.place(x=0,y=0)


        #balance info
        self.wlabel9 = CTk.CTkLabel(self.wallet,text="ACCOUNT HISTORY",font=('Courier',25))
        self.wlabel9.place(x=850,y=50)
        self.table_frame = CTk.CTkFrame(self.wallet,width=200,height=200)
        self.table_frame.place(x=850,y=100)
        self.table = ttk.Treeview(self.table_frame, columns=("col1", "col2","col3"),height=10)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('Times',20))
        style.configure("Treeview", font=general_font,rowheight=30)
        self.table.column("#0", width = 0, stretch = "no")
        self.table.heading("#1", text="ACTION")
        self.table.column("#1",width=180)
        self.table.heading("#2", text="AMOUNT")
        self.table.column("#2",width=250)
        self.table.heading("#3", text="TIME")
        self.table.column("#3", width=250)
        self.table_scrollbar = tk.Scrollbar(self.table_frame, orient="vertical", command=self.table.yview)
        self.table_scrollbar.pack(side="right", fill="y")
        self.table.configure(yscrollcommand=self.table_scrollbar.set)
        self.table.pack(expand=True, fill="both")
        self.userb = bef.balinfo(self.username)
        for i in range(len(self.userb)):
            entry = self.userb[i]
            self.table.insert("","end",values=entry[1:4])
        

        #balance
        self.Pframe0 = CTk.CTkFrame(self.wallet,width=550,height=380)
        self.Pframe0.place(x=850,y=420)
        self.wlabel3 = CTk.CTkLabel(self.Pframe0,text="FUND YOUR WALLET ",font=('Courier',30))
        self.wlabel3.place(x=20,y=30)
        self.balance = bef.getbalance(f'{self.username}')
        self.wlabel1 = CTk.CTkLabel(self.Pframe0,text="BALANCE AVAILABLE",font=('Courier',27))
        self.wlabel1.place(x=40,y=100)
        self.wlabel2 = CTk.CTkLabel(self.Pframe0,text=f'{self.balance} USD',font=('Courier',20))
        self.wlabel2.place(x=60,y=160)

        self.amt = tk.StringVar()
        self.wlabel3 = CTk.CTkLabel(self.Pframe0,text="ENTER THE AMOUNT",font=('Courier',20))
        self.wlabel3.place(x=40,y=230)
        self.wentry0 = CTk.CTkEntry(self.Pframe0,textvariable = self.amt)
        self.wentry0.place(x=280,y=230)
        self.addbut = CTk.CTkButton(self.Pframe0,text="DEPOSIT MONEY",font=('Courier',20),command =self.add)
        self.addbut.place(x=40,y=300)
        self.withdrawbut = CTk.CTkButton(self.Pframe0,text="WITHDRAW MONEY",font=('Courier',20),command = self.withdraw)
        self.withdrawbut.place(x=300,y=300)

        #edit profile
        self.Pframe1 = CTk.CTkFrame(self.wallet,width=700,height=440)
        self.Pframe1.place(x=60,y=360)
        self.curpwd = tk.StringVar()
        self.newpwd = tk.StringVar()
        self.newpwd1 = tk.StringVar()
        self.wlabel5 = CTk.CTkLabel(self.Pframe1,text="CHANGE YOUR PASSWORD",font=('Courier',30))
        self.wlabel5.place(x=20,y=40)
        self.wlabel6 = CTk.CTkLabel(self.Pframe1,text="Enter Your Current Password",font=('Courier',25))
        self.wlabel6.place(x=40,y=90)
        self.wentry1 = CTk.CTkEntry(self.Pframe1,textvariable=self.curpwd,show="*",width=600,height=30)
        self.wentry1.place(x=40,y=130)
        self.wlabel7 = CTk.CTkLabel(self.Pframe1,text="Enter Your New Password",font=('Courier',25))
        self.wlabel7.place(x=40,y=190)
        self.wentry2 = CTk.CTkEntry(self.Pframe1,textvariable=self.newpwd,show="*",width=600,height=30)
        self.wentry2.place(x=40,y=230)
        self.wlabel8 = CTk.CTkLabel(self.Pframe1,text="Re-Enter Your New Password",font=('Courier',25))
        self.wlabel8.place(x=40,y=280)
        self.wentry3 = CTk.CTkEntry(self.Pframe1,textvariable=self.newpwd1,show="*",width=600,height=30)
        self.wentry3.place(x=40,y=320)
        self.wbutton0 = CTk.CTkButton(self.Pframe1,text="Change Password",font=('Courier',20),command=self.chgpwd)
        self.wbutton0.place(x=450,y=380)


    def chgpwd(self):
        self.curpwd1 = self.curpwd.get()
        self.newpwd00 = self.newpwd.get()
        self.newpwd01 = self.newpwd1.get()

        if self.curpwd1=="" or self.newpwd00=="" or self.newpwd01=="":
            self.cp0 = tk.messagebox.showinfo("ERROR","FIELD IS EMPTY")
        
        elif bef.logindatabase(self.username,self.curpwd1) != True:
            self.cp2 = tk.messagebox.showinfo("ERROR","CURRENT PASSWORD IS INCORRECT")
        
        elif self.newpwd00 != self.newpwd01:
            self.cp1 = tk.messagebox.showinfo("ERROR","PASSWORD DON'T MATCH")

        else:
            bef.chgpassword(self.username,self.newpwd00)
            self.curpwd.set("")
            self.newpwd.set("")
            self.newpwd1.set("")


    def add(self):
        if self.amt.get()=="":
            self.ames0 = tk.messagebox.showinfo("ERROR","ENTER SOME AMOUNT")
        else:
            self.addamt = Decimal(self.amt.get())
            if self.addamt == 0 or self.addamt < 0:
                self.ames1 = tk.messagebox.showinfo("ERROR","ENTER SOME AMOUNT")
            elif self.addamt > 0:
                self.ames2 = tk.messagebox.askquestion("DEPOSIT MONEY",f"ADDING {self.addamt}USD TO ACCOUNT")
                if self.ames2 == "yes":
                    bef.addbalance(self.username,self.addamt)
                    self.amt.set("")
                else:
                    self.amt.set("")

    def withdraw(self):
        self.balance = bef.getbalance(f'{self.username}')
        if self.balance == None:
            self.wmes3 = tk.messagebox.showinfo("ERROR","NO BALANCE")
        elif self.amt.get()=="":
            self.wmes0 = tk.messagebox.showinfo("ERROR","ENTER SOME AMOUNT")
        else:
            self.withamt = Decimal(self.amt.get())
            if self.withamt == 0 or self.withamt < 0:
                self.wmes1 = tk.messagebox.showinfo("INVALID AMOUNT","ENTER SOME AMOUNT")
            elif self.balance < self.withamt:
                self.wmes1 = tk.messagebox.showinfo("INVALID AMOUNT",f"INSUFFICIENT BALANCE\nCURRENT BALANCE: {self.balance}")
            elif self.withamt > 0:
                self.wmes2 = tk.messagebox.askquestion("WITHDRAW MONEY",f"WITHDRAWING {self.withamt}USD FROM ACCOUNT")
                if self.wmes2 == "yes":
                    bef.withdrawwallet(self.username,self.withamt)
                    self.amt.set("")
                else:
                    self.amt.set("")

if __name__=='__main__':
    app=MainWin()
    app.login()
    app.win.mainloop()
