# Importing the tkinter module
import customtkinter as CTk
import tkinter as tk
from tkinter import ttk
import backend as bef
from matplotlib.animation  import FuncAnimation
import pandas as pd
import mplcursors
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import api_graph as graph_win
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from decimal import Decimal

general_font=('Times', 18)
large_font = ('Times', 25)
current_theme='dark'
class MainWindow:
    def __init__(self,username):
        self.window = CTk.CTk()
        self.frame = CTk.CTkFrame(master=self.window,
                                  width=1250,height=850)
        self.frame.place(x=220,y=0)
        #Window will be at maximum windowed size
        self.window.state('zoomed')
        #Window Title
        self.window.title("Crypto")

        self.user_label = CTk.CTkLabel(master=self.window,text=f"{username}",
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
        #Theme Button
        self.theme_Button = CTk.CTkSwitch(master=self.window,
                            text="Light Theme",
                            command=self.change_theme)
        self.theme_Button.place(x=50,y=700)
        
        self.window.mainloop()
    #Methods
    #Configuring window theme
    def change_theme(self):
        global current_theme
        if current_theme == "dark":
            current_theme="light"
        else:
            current_theme="dark"
        CTk.set_appearance_mode(current_theme)
    #wishlist button function
    def wishlist_func(self):
        self.frame.destroy()
        self.new_frame = wishlist_frame(self.window)
        #self.new_frame.display_list()
    #BuyIN button function
    def buyin_func(self):
        self.frame.destroy()
        self.new_frame = boughtlist_frame(self.window)
    #Sellout button function
    def sellout_func(self):
        self.frame.destroy()
        self.new_frame = soldlist_frame(self.window)   
    #Holdlist button function
    def holdlist_func(self):
        self.frame.destroy()
        self.new_frame = holdlist_frame(self.window)
    #Exit function
    def exit_func(self):
        self.window.destroy()
        exit()


class wishlist_frame:
    def __init__(self,window):
        self.main = window
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
            self.table.insert("", "end",iid=i+1, text=i+1, values=entry[1:5])
        self.new_data=bef.get_his('bitcoin','1d')
        self.table_frame.after(1000,self.update_values,curs_data)  
        # self.table_frame.after(2000,self.plot)
    # update values in tables
    def update_values(self,data_rec):
        for i in range(len(data_rec)):
            new_price=bef.get_cur_price(data_rec[i][2].lower())
            self.table.item(i+1, values=(data_rec[i][1],data_rec[i][2],new_price,data_rec[i][4]+1))
        print( "table update was called")
    
    def OnDoubleClick(self,event):
        sel_item = self.table.identify('item',event.x,event.y)
        curname = self.table.item(sel_item)['values'][1]
        self.main.destroy()
        self.win = graph_win.CurrencyDetails('thejabh',curname)
        

        
        
    
    def plot(self):
        
        #initial data
        self.data=bef.current_data('bitcoin')
        print(self.data)
        self.new_data=pd.concat([self.new_data,self.data],ignore_index=True)   
        
        self.fig=Figure()
        self.canvas = FigureCanvasTkAgg(self.fig, self.frame)
        self.canvas.get_tk_widget().place(x=200,y=200)
        self.ax=self.fig.add_subplot(111)
        self.ax.plot(self.new_data['time'][1435:],self.new_data['price'][1435:])
        self.ani = FuncAnimation(self.fig,self.update_line,interval=10000)
    def update_line(self,i):
        
        self.data=bef.current_data('bitcoin')
        print(self.data)
        
        self.new_data=pd.concat([self.new_data,self.data],ignore_index=True)
        print(self.new_data[1435:])

        #return line,
        self.ax.plot(self.new_data['time'][1435:],self.new_data['price'][1435:])
        mplcursors.cursor(hover=False)
        mplcursors.cursor(hover=True)

class boughtlist_frame:
    def __init__(self,window):
        self.window = window
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
    
    def OnDoubleClick(self,event):
        sel_item = self.table.identify('item',event.x,event.y)
        cur = self.table.item(sel_item)['values'][1]
        self.plot_window(cur)
    def plot_window(self,curname):
        self.plot_window=CTk.CTk()
        self.title = CTk.CTkLabel(self.plot_window,text=curname).pack() 
        self.plot_window.mainloop()

class soldlist_frame:
    def __init__(self,window):
        self.window = window
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
    
    def OnDoubleClick(self,event):
        sel_item = self.table.identify('item',event.x,event.y)
        cur = self.table.item(sel_item)['values'][1]
        self.plot_window(cur)
    def plot_window(self,curname):
        self.plot_window=CTk.CTk()
        self.title = CTk.CTkLabel(self.plot_window,text=curname).pack() 
        self.plot_window.mainloop()

class holdlist_frame:
    def __init__(self,window):
        
        self.window = window
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
        cur = self.table.item(sel_item)['values'][1]
        self.plot_window(cur)
    def plot_window(self,curname):
        self.plot_window=CTk.CTk()
        self.title = CTk.CTkLabel(self.plot_window,text=curname).pack() 
        self.plot_window.mainloop()


#---------------GRAPH--------------------

# class CurrencyDetails:
#     def __init__(self,username,curname):
        
#         self.username = username
#         self.curname = curname
        
#         self.root = CTk.CTk()
#         # self.root = CTk.CTkToplevel(master)
#         self.root.state("zoomed")
#         self.gframe = CTk.CTkFrame(self.root,width=2500,height=700).place(x=0,y=0)
#         self.gLabel1 = CTk.CTkLabel(self.gframe,text=f'{self.curname}',font=('Courier',30))
#         self.gLabel1.place(x=50,y=60)
#         self.gLabel2 = CTk.CTkLabel(self.gframe,text="PRICE",font=('Courier',30)).place(x=50,y=100)
#         self.gLabel3 = CTk.CTkLabel(self.gframe,text="Profit/Loss",font=('Courier',15)).place(x=50,y=130)
        
#         self.gButton1 = CTk.CTkButton(self.gframe,width=50,text="1D",font=('Courier',10),command = lambda: self.graphing("1d")).place(x=50,y=620)
#         self.gButton2 = CTk.CTkButton(self.gframe,width=50,text="1W",font=('Courier',10),command = lambda: self.graphing("1w")).place(x=150,y=620)
#         self.gButton3 = CTk.CTkButton(self.gframe,width=50,text="1M",font=('Courier',10),command = lambda: self.graphing("1m")).place(x=250,y=620)
#         self.gButton4 = CTk.CTkButton(self.gframe,width=50,text="1Y",font=('Courier',10),command = lambda: self.graphing("1y")).place(x=350,y=620)

#         self.gButton5 = CTk.CTkButton(self.gframe,width=50,text="Profile",font=('Courier',25),command=self.pro).place(x=1300,y=40)

#         self.balance = bef.getbalance(f'{self.username}')
#         self.WalletL = CTk.CTkLabel(self.gframe,text=f'{self.balance}' + ' USD',font=('Courier',25)).place(x=700,y=40)

#         #curent data
#         self.curquant = bef.coinquant(self.username,self.curname)
#         self.cLabel1 = CTk.CTkLabel(self.gframe,text = f"CURRENT QUANTITY: {self.curquant}",font=('Courier',20)).place(x=900,y=450)

#         #selling
#         self.quantityS = tk.StringVar()
#         self.qLabel = CTk.CTkLabel(self.gframe,text="QUANTITY",font=('Courier',20)).place(x=720,y=550)
#         self.qEntry = CTk.CTkEntry(self.gframe,textvariable=self.quantityS).place(x=850,y=550)
#         self.sellingc = CTk.CTkButton(self.gframe,text="SELL",font=('Courier',20),command=self.selling).place(x=800,y=620)

#         #buying
#         self.quantityB = tk.StringVar()
#         self.qLabel = CTk.CTkLabel(self.gframe,text="QUANTITY",font=('Courier',20)).place(x=1020,y=550)
#         self.qEntry = CTk.CTkEntry(self.gframe,textvariable=self.quantityB).place(x=1150,y=550)
#         self.buyingc = CTk.CTkButton(self.gframe,text="BUY",font=('Courier',20),command=self.buying).place(x=1100,y=620)
#         self.root.mainloop()

#     def selling(self):
#         if self.quantityS.get() == "":
#             selfmes7 = tk.messagebox.showinfo("ERROR","ENTER SOME AMOUNT")
#         else:
#             self.coinq1 = Decimal(self.quantityS.get())
#             self.p1 = bef.current_data(f"{self.curname}")
#             self.curp1 = self.p1['price'][0]
#             if self.curquant == 0 or self.curquant < 0:
#                 self.Smes0 = tk.messagebox.showinfo("ERROR MESSAGE","ENTER VALID AMOUNT")
#             else:
#                 if self.coinq1 == 0:
#                     self.Smes1 = tk.messagebox.showinfo("INVALID AMOUNT","You Entered 0\nEnter Valid Amount")
#                 elif self.coinq1 > self.curquant:
#                     self.Smes2 = tk.messagebox.showinfo("NOT ENOUGH COINS",f"YOU CURRENT ONLY HOLD {self.curquant}")
#                 else:
#                     self.Smes3 = tk.messagebox.askquestion("SELLING",f"ORDER TO SELL {self.coinq1} AT PRICE {self.curp1}")
#                     if self.Smes3 == "yes":
#                         bef.selling(self.username,self.curname,self.coinq1)
#                     else:
#                         self.quantityS.set("")


#     def buying(self):
#         self.coinq2 = Decimal(self.quantityB.get())
#         self.p2 = bef.current_data(f"{self.curname}")
#         self.curp2 = self.p2['price'][0]
#         if self.coinq2 == 0 or self.coinq2 < 0:
#             self.Bmes1 = tk.messagebox.showinfo("INVALID AMOUNT","Enter Valid Amount")
#         elif self.balance < self.curp2 * self.coinq2:
#             self.maxamt = self.balance/self.curp2
#             self.Bmes2 = tk.messagebox.showinfo("NOT ENOUGH FUNDS",f"THE QUANTITY SHOULD BE LESS THAN {self.maxamt}")
#         else:
#             self.Bmes3 = tk.messagebox.askquestion("BUYING",f"ORDER TO BUY {self.coinq2} AT PRICE {self.curp2}")
#             if self.Bmes3 == "yes":
#                 bef.buying(self.username,self.curname,self.coinq2)
#             else:
#                 self.quantityB.set("")


#     def graphing(self,time):
#         self.interval = time
#         self.curdata = bef.get_his(self.curname,self.interval)

#         self.fig = Figure(figsize=(8,5),dpi=100,facecolor='grey')
#         self.plot1 = self.fig.add_subplot(111)
#         self.plot1.plot(self.curdata['time'],self.curdata['price'])
#         self.ax = plt.axes()
#         self.ax.set_facecolor("grey")
#         self.canvas1 = FigureCanvasTkAgg(self.fig,self.root)

#         self.canvas1.draw()
#         self.canvas1.get_tk_widget().place(x=50,y=220)

#     def pro(self):
#         pass

class Profile:
#     def __init__(self,username):
#         self.username = username


#         self.wallet = CTk.CTk()
#         self.wallet.state("zoomed")

#         self.wlabel0 = CTk.CTkLabel(self.wallet,text=f'{self.username}',font=('Courier',30))
#         self.wlabel0.place(x=140,y=40)
#         self.userd0 = CTk.CTkLabel(self.wallet,text="SOME DETAILS",font=('Courier',20))
#         self.userd0.place(x=180,y=120)

#         #balance
#         self.Pframe0 = CTk.CTkFrame(self.wallet,width=550,height=380)
#         self.Pframe0.place(x=850,y=420)
#         self.wlabel3 = CTk.CTkLabel(self.Pframe0,text="FUND YOUR WALLET ",font=('Courier',30))
#         self.wlabel3.place(x=20,y=30)
#         self.balance = bef.getbalance(f'{self.username}')
#         self.wlabel1 = CTk.CTkLabel(self.Pframe0,text="BALANCE AVAILABLE",font=('Courier',27))
#         self.wlabel1.place(x=40,y=100)
#         self.wlabel2 = CTk.CTkLabel(self.Pframe0,text=f'{self.balance} USD',font=('Courier',20))
#         self.wlabel2.place(x=60,y=160)

#         self.amt = tk.StringVar()
#         self.wlabel3 = CTk.CTkLabel(self.Pframe0,text="ENTER THE AMOUNT",font=('Courier',20))
#         self.wlabel3.place(x=40,y=230)
#         self.wentry0 = CTk.CTkEntry(self.Pframe0,textvariable = self.amt)
#         self.wentry0.place(x=280,y=230)
#         self.addbut = CTk.CTkButton(self.Pframe0,text="DEPOSIT MONEY",font=('Courier',20),command =self.add)
#         self.addbut.place(x=40,y=300)
#         self.withdrawbut = CTk.CTkButton(self.Pframe0,text="WITHDRAW MONEY",font=('Courier',20),command = self.withdraw)
#         self.withdrawbut.place(x=300,y=300)

#         #edit profile
#         self.Pframe1 = CTk.CTkFrame(self.wallet,width=700,height=440)
#         self.Pframe1.place(x=60,y=360)
#         self.curpwd = tk.StringVar()
#         self.newpwd = tk.StringVar()
#         self.newpwd1 = tk.StringVar()
#         self.wlabel5 = CTk.CTkLabel(self.Pframe1,text="CHANGE YOUR PASSWORD",font=('Courier',30))
#         self.wlabel5.place(x=20,y=40)
#         self.wlabel6 = CTk.CTkLabel(self.Pframe1,text="Enter Your Current Password",font=('Courier',25))
#         self.wlabel6.place(x=40,y=90)
#         self.wentry1 = CTk.CTkEntry(self.Pframe1,textvariable=self.curpwd,show="*",width=600,height=30)
#         self.wentry1.place(x=40,y=130)
#         self.wlabel7 = CTk.CTkLabel(self.Pframe1,text="Enter Your New Password",font=('Courier',25))
#         self.wlabel7.place(x=40,y=190)
#         self.wentry2 = CTk.CTkEntry(self.Pframe1,textvariable=self.newpwd,show="*",width=600,height=30)
#         self.wentry2.place(x=40,y=230)
#         self.wlabel8 = CTk.CTkLabel(self.Pframe1,text="Re-Enter Your New Password",font=('Courier',25))
#         self.wlabel8.place(x=40,y=280)
#         self.wentry3 = CTk.CTkEntry(self.Pframe1,textvariable=self.newpwd1,show="*",width=600,height=30)
#         self.wentry3.place(x=40,y=320)
#         self.wbutton0 = CTk.CTkButton(self.Pframe1,text="Change Password",font=('Courier',20),command=self.chgpwd)
#         self.wbutton0.place(x=450,y=380)


#     def chgpwd(self):
#         self.curpwd1 = self.curpwd.get()
#         self.newpwd00 = self.newpwd.get()
#         self.newpwd01 = self.newpwd1.get()

#         if self.curpwd1=="" or self.newpwd00=="" or self.newpwd01=="":
#             self.cp0 = tk.messagebox.showinfo("ERROR","FIELD IS EMPTY")
        
#         elif bef.logindatabase(self.username,self.curpwd1) != True:
#             self.cp2 = tk.messagebox.showinfo("ERROR","CURRENT PASSWORD IS INCORRECT")
        
#         elif self.newpwd00 != self.newpwd01:
#             self.cp1 = tk.messagebox.showinfo("ERROR","PASSWORD DON'T MATCH")

#         else:
#             bef.chgpassword(self.username,self.newpwd00)
#             self.curpwd.set("")
#             self.newpwd.set("")
#             self.newpwd1.set("")


#     def add(self):
#         if self.amt.get()=="":
#             self.ames0 = tk.messagebox.showinfo("ERROR","ENTER SOME AMOUNT")
#         else:
#             self.addamt = Decimal(self.amt.get())
#             if self.addamt == 0 or self.addamt < 0:
#                 self.ames1 = tk.messagebox.showinfo("INVALID AMOUNT","ENTER SOME AMOUNT")
#             elif self.addamt > 0:
#                 self.ames2 = tk.messagebox.askquestion("DEPOSITING MONEY",f"ADDING {self.addamt}USD TO BALANCE")
#                 if self.ames2 == "yes":
#                     bef.addbalance(self.username,self.addamt)
#                 else:
#                     self.amt.set("")

#     def withdraw(self):
#         self.balance = bef.getbalance(f'{self.username}')
#         if self.balance == None:
#             self.wmes3 = tk.messagebox.showinfo("ERROR","NO BALANCE")
#         elif self.amt.get()=="":
#             self.wmes0 = tk.messagebox.showinfo("ERROR","ENTER SOME AMOUNT")
#         else:
#             self.withamt = Decimal(self.amt.get())
#             if self.withamt == 0 or self.withamt < 0:
#                 self.wmes1 = tk.messagebox.showinfo("INVALID AMOUNT","ENTER SOME AMOUNT")
#             elif self.balance < self.withamt:
#                 self.wmes1 = tk.messagebox.showinfo("INVALID AMOUNT",f"INSUFFICIENT BALANCE\nCURRENT BALANCE: {self.balance}")
#             elif self.withamt > 0:
#                 self.wmes2 = tk.messagebox.askquestion("DEPOSITING MONEY",f"ADDING {self.withamt}USD TO BALANCE")
#                 if self.wmes2 == "yes":
#                     bef.withdrawwallet(self.username,self.withamt)
#                 else:
#                     self.amt.set("")



#Main program execution
if (__name__=="__main__"):
    app = MainWindow("Whitedevil")
    
