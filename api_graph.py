import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import backend as bef
import tkinter as tk
from decimal import Decimal
import mysql.connector
import customtkinter as CTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk

general_font=('Courier',25)
#click in tables -> graph and sell and buy   
class CurrencyDetails:
    def __init__(self,username,curname):
        
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
        # self.gButton1 = CTk.CTkButton(self.tab_view.tab('1D'),width=50,text="1D",font=('Courier',10),
        #                               command = lambda: self.graphing("1d",self.tab_view.tab('1D'))).place(x=0,y=0)
        # self.gButton2 = CTk.CTkButton(self.tab_view.tab('1W'),width=50,text="1W",font=('Courier',10),
        #                               command = lambda: self.graphing("1w",self.tab_view.tab('1W'))).place(x=0,y=0)
        # self.gButton3 = CTk.CTkButton(self.tab_view.tab('1M'),width=50,text="1M",font=('Courier',10),
        #                               command = lambda: self.graphing("1m",self.tab_veiw.tab('1M'))).place(x=0,y=0)
        # self.gButton4 = CTk.CTkButton(self.tab_view.tab('1Y'),width=50,text="1Y",font=('Courier',10),
        #                               command = lambda: self.graphing("1y",self.tab_veiw.tab('1Y'))).place(x=0,y=0)

        self.menu = CTk.CTkFrame(self.mainframe,width=1500,height=50)
        self.menu.place(x=0,y=0)
        self.exit_but = CTk.CTkButton(self.menu,text="X",width=50,height=50,command = self.exit_)
        self.exit_but.place(x=1370,y=0)
        #--------navigation profile-------------
        self.gButton5 = CTk.CTkButton(self.menu,width=50,height=50,text='=',
                                      font=('Courier',40),
                                      command=self.switch)
        self.gButton5.place(x=1420,y=0)
        self.btnState=False# initially navbar is closed
        self.navRoot= CTk.CTkFrame(self.mainframe, height=900, width=400)
        self.navRoot.place(x=1600,y=50)
        #menu frame
        CTk.CTkLabel(self.navRoot,text=self.username,font=general_font,width=300,height=50).place(x=10,y=10)
        
        #option widgets inside navbar  
        color='grey20'
        CTk.CTkButton(self.navRoot,text='PROFILE',width=300,height=50,font=general_font,
                      hover_color='OliveDrab2',text_color='black',fg_color=color).place(x=-10,y=200)
        CTk.CTkButton(self.navRoot,text='WISHLIST',width=300,height=50,font=general_font,
                      hover_color='RoyalBlue2',text_color='black',fg_color=color).place(x=-10,y=250)
        CTk.CTkButton(self.navRoot,text='HOLDING',width=300,height=50,font=general_font,
                      hover_color='yellow',text_color='black',fg_color=color).place(x=-10,y=300)
        CTk.CTkButton(self.navRoot,text='LOG OUT',width=300,height=50,font=general_font,
                      hover_color='white',text_color='black',fg_color=color).place(x=-10,y=500)
        
        
        self.balance = bef.getbalance(f'{self.username}')
        self.WalletL = CTk.CTkLabel(self.mainframe,text=f'{self.balance}' + ' USD',font=general_font)
        self.WalletL.place(x=700,y=40)

        #curent data
        self.curquant = bef.coinquant(self.username,self.curname)
        self.cLabel1 = CTk.CTkLabel(self.mainframe,text = f"CURRENT QUANTITY: {self.curquant}",font=('Courier',20))
        self.cLabel1.place(x=900,y=450)

        #selling
        # self.quantityS = tk.StringVar()
        # self.qLabel = CTk.CTkLabel(self.mainframe,text="QUANTITY",font=('Courier',20)).place(x=720,y=550)
        # self.qEntry = CTk.CTkEntry(self.mainframe,textvariable=self.quantityS).place(x=850,y=550)
        self.sellingc = CTk.CTkButton(self.mainframe,text="SELL",font=('Courier',20),command=self.selling)
        self.sellingc.place(x=800,y=620)

        #buying
        # self.quantityB = tk.StringVar()
        # self.qLabel = CTk.CTkLabel(self.mainframe,text="QUANTITY",font=('Courier',20)).place(x=1020,y=550)
        # self.qEntry = CTk.CTkEntry(self.mainframe,textvariable=self.quantityB).place(x=1150,y=550)
        self.buyingc = CTk.CTkButton(self.mainframe,text="BUY",font=('Courier',20),command=self.buying)
        self.buyingc.place(x=1000,y=620)

        #initially 24hrs graph
        self.graphing('1d',self.tab_view.tab('1D'))
    
    def exit_(self):
            self.root.destroy()
            exit()
    def switch(self):
    
        if self.btnState is True:
            # create animated Navbar closing:
            for x in range(1200,1600):
                self.navRoot.place(x=x, y=50)
                self.mainframe.update()
            # turning button OFF:
            self.btnState = False
        
        else:
            # created animated Navbar opening:
            for x in range(1600,1200,-1):
                self.navRoot.place(x=x, y=50)
                self.mainframe.update()

            # turing button ON:
            self.btnState = True
    

    
    # def selling(self):
    #     if self.quantityS.get() == "":
    #         selfmes7 = tk.messagebox.showinfo("ERROR","ENTER SOME AMOUNT")
    #     else:
    #         self.coinq1 = Decimal(self.quantityS.get())
    #         self.p1 = bef.current_data(f"{self.curname}")
    #         self.curp1 = self.p1['price'][0]
    #         if self.curquant == 0 or self.curquant < 0:
    #             self.Smes0 = tk.messagebox.showinfo("ERROR MESSAGE","ENTER VALID AMOUNT")
    #         else:
    #             if self.coinq1 == 0:
    #                 self.Smes1 = tk.messagebox.showinfo("INVALID AMOUNT","You Entered 0\nEnter Valid Amount")
    #             elif self.coinq1 > self.curquant:
    #                 self.Smes2 = tk.messagebox.showinfo("NOT ENOUGH COINS",f"YOU CURRENT ONLY HOLD {self.curquant}")
    #             else:
    #                 self.Smes3 = tk.messagebox.askquestion("SELLING",f"ORDER TO SELL {self.coinq1} AT PRICE {self.curp1}")
    #                 if self.Smes3 == "yes":
    #                     bef.selling(self.username,self.curname,self.coinq1)
    #                 else:
    #                     self.quantityS.set("")


    # def buying(self):
    #     self.coinq2 = Decimal(self.quantityB.get())
    #     self.p2 = bef.current_data(f"{self.curname}")
    #     self.curp2 = self.p2['price'][0]
    #     if self.coinq2 == 0 or self.coinq2 < 0:
    #         self.Bmes1 = tk.messagebox.showinfo("INVALID AMOUNT","Enter Valid Amount")
    #     elif self.balance < self.curp2 * self.coinq2:
    #         self.maxamt = self.balance/self.curp2
    #         self.Bmes2 = tk.messagebox.showinfo("NOT ENOUGH FUNDS",f"THE QUANTITY SHOULD BE LESS THAN {self.maxamt}")
    #     else:
    #         self.Bmes3 = tk.messagebox.askquestion("BUYING",f"ORDER TO BUY {self.coinq2} AT PRICE {self.curp2}")
    #         if self.Bmes3 == "yes":
    #             bef.buying(self.username,self.curname,self.coinq2)
    #         else:
    #             self.quantityB.set("")

    def selling(self): pass
    def buying(self): pass
    
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

    def pro(self):
        self.canvas1.destroy()

        self.root.destroy()
        app=Profile('thejabh')

class Profile:
    def __init__(self,username):
        self.username = username


        self.wallet = CTk.CTk()
        self.wallet.state("zoomed")

        self.wlabel0 = CTk.CTkLabel(self.wallet,text=f'Hello {self.username}',font=('Courier',30))
        self.wlabel0.place(x=80,y=40)

        self.balance = bef.getbalance(f'{self.username}')
        self.wlabel1 = CTk.CTkLabel(self.wallet,text="BALANCE AVAILABLE",font=('Courier',30))
        self.wlabel1.place(x=80,y=200)
        self.wlabel2 = CTk.CTkLabel(self.wallet,text=f'{self.balance} USD',font=('Courier',20))
        self.wlabel2.place(x=80,y=240)
        
        self.amt = tk.StringVar()
        self.wlabel3 = CTk.CTkLabel(self.wallet,text="ENTER THE AMOUNT",font=('Courier',20))
        self.wlabel3.place(x=80,y=450)
        self.wentry0 = CTk.CTkEntry(self.wallet,textvariable = self.amt).place(x=350,y=450)
        self.addbut = CTk.CTkButton(self.wallet,text="DEPOSIT MONEY",font=('Courier',20),command =self.add)
        self.addbut.place(x=80,y=530)
        self.withdrawbut = CTk.CTkButton(self.wallet,text="WITHDRAW MONEY",font=('Courier',20),command = self.withdraw)
        self.withdrawbut.place(x=300,y=530)
        self.wallet.mainloop()

    def add(self):
        if self.amt.get()=="":
            self.ames0 = tk.messagebox.showinfo("ERROR","ENTER SOME AMOUNT")
        else:
            self.addamt = Decimal(self.amt.get())
            if self.addamt == 0 or self.addamt < 0:
                self.ames1 = tk.messagebox.showinfo("INVALID AMOUNT","ENTER SOME AMOUNT")
            elif self.addamt > 0:
                self.ames2 = tk.messagebox.askquestion("DEPOSITING MONEY",f"ADDING {self.addamt}USD TO BALANCE")
                if self.ames2 == "yes":
                    bef.addbalance(self.username,self.addamt)
                else:
                    self.amt.set("")

    def withdraw(self):
        self.balance = bef.getbalance(f'{self.username}')
        if self.amt.get()=="":
            self.wmes0 = tk.messagebox.showinfo("ERROR","ENTER SOME AMOUNT")
        else:
            self.withamt = Decimal(self.amt.get())
            if self.addamt == 0 or self.addamt < 0:
                self.wmes1 = tk.messagebox.showinfo("INVALID AMOUNT","ENTER SOME AMOUNT")
            elif self.balance < self.withamt:
                self.wmes1 = tk.messagebox.showinfo("INVALID AMOUNT",f"INSUFFICIENT BALANCE\nCURRENT BALANCE: {self.balance}")
            elif self.withamt > 0:
                self.wmes2 = tk.messagebox.askquestion("DEPOSITING MONEY",f"ADDING {self.withamt}USD TO BALANCE")
                if self.wmes2 == "yes":
                    bef.withdrawwallet(self.username,self.withamt)
                else:
                    self.amt.set("")


if __name__ == "__main__":
    abc = CurrencyDetails('thejabh','bitcoin')
    abc.root.mainloop()