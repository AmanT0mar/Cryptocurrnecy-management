import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import backend as bef
import tkinter as tk
from decimal import Decimal
import mysql.connector
import customtkinter as CTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2Tk
   
#click in tables -> graph and sell and buy   
class CurrencyDetails:
    def __init__(self,username,curname):
        self.username = username
        self.curname = curname
        
        self.root = CTk.CTk()
        self.root.state("zoomed")

        self.gframe = CTk.CTkFrame(self.root,width=2500,height=700).place(x=0,y=0)
        self.gLabel1 = CTk.CTkLabel(self.gframe,text=f'{self.curname}',font=('Courier',30)).place(x=50,y=60)
        self.gLabel2 = CTk.CTkLabel(self.gframe,text="PRICE",font=('Courier',30)).place(x=50,y=100)
        self.gLabel3 = CTk.CTkLabel(self.gframe,text="Profit/Loss",font=('Courier',15)).place(x=50,y=130)
        
        self.gButton1 = CTk.CTkButton(self.gframe,width=50,text="1D",font=('Courier',10),command = lambda: self.graphing("1d")).place(x=50,y=620)
        self.gButton2 = CTk.CTkButton(self.gframe,width=50,text="1W",font=('Courier',10),command = lambda: self.graphing("1w")).place(x=150,y=620)
        self.gButton3 = CTk.CTkButton(self.gframe,width=50,text="1M",font=('Courier',10),command = lambda: self.graphing("1m")).place(x=250,y=620)
        self.gButton4 = CTk.CTkButton(self.gframe,width=50,text="1Y",font=('Courier',10),command = lambda: self.graphing("1y")).place(x=350,y=620)

        self.gButton5 = CTk.CTkButton(self.gframe,width=50,text="Profile",font=('Courier',25),command=self.pro).place(x=1300,y=40)

        self.balance = bef.getbalance(f'{self.username}')
        self.WalletL = CTk.CTkLabel(self.gframe,text=f'{self.balance}' + ' USD',font=('Courier',25)).place(x=700,y=40)

        #curent data
        self.curquant = bef.coinquant(self.username,self.curname)
        self.cLabel1 = CTk.CTkLabel(self.gframe,text = f"CURRENT QUANTITY: {self.curquant}",font=('Courier',20)).place(x=900,y=450)

        #selling
        self.quantityS = tk.StringVar()
        self.qLabel = CTk.CTkLabel(self.gframe,text="QUANTITY",font=('Courier',20)).place(x=720,y=550)
        self.qEntry = CTk.CTkEntry(self.gframe,textvariable=self.quantityS).place(x=850,y=550)
        self.sellingc = CTk.CTkButton(self.gframe,text="SELL",font=('Courier',20),command=self.selling).place(x=800,y=620)

        #buying
        self.quantityB = tk.StringVar()
        self.qLabel = CTk.CTkLabel(self.gframe,text="QUANTITY",font=('Courier',20)).place(x=1020,y=550)
        self.qEntry = CTk.CTkEntry(self.gframe,textvariable=self.quantityB).place(x=1150,y=550)
        self.buyingc = CTk.CTkButton(self.gframe,text="BUY",font=('Courier',20),command=self.buying).place(x=1100,y=620)


    def selling(self):
        if self.quantityS.get() == "":
            selfmes7 = tk.messagebox.showinfo("ERROR","ENTER SOME AMOUNT")
        else:
            self.coinq1 = Decimal(self.quantityS.get())
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
                    else:
                        self.quantityS.set("")


    def buying(self):
        self.coinq2 = Decimal(self.quantityB.get())
        self.p2 = bef.current_data(f"{self.curname}")
        self.curp2 = self.p2['price'][0]
        if self.coinq2 == 0 or self.coinq2 < 0:
            self.Bmes1 = tk.messagebox.showinfo("INVALID AMOUNT","Enter Valid Amount")
        elif self.balance < self.curp2 * self.coinq2:
            self.maxamt = self.balance/self.curp2
            self.Bmes2 = tk.messagebox.showinfo("NOT ENOUGH FUNDS",f"THE QUANTITY SHOULD BE LESS THAN {self.maxamt}")
        else:
            self.Bmes3 = tk.messagebox.askquestion("BUYING",f"ORDER TO BUY {self.coinq2} AT PRICE {self.curp2}")
            if self.Bmes3 == "yes":
                bef.buying(self.username,self.curname,self.coinq2)
            else:
                self.quantityB.set("")


    def graphing(self,time):
        self.interval = time
        self.curdata = bef.get_his(self.curname,self.interval)

        self.fig = Figure(figsize=(8,5),dpi=100,facecolor='grey')
        self.plot1 = self.fig.add_subplot(111)
        self.plot1.plot(self.curdata['time'],self.curdata['price'])
        self.ax = plt.axes()
        self.ax.set_facecolor("grey")
        self.canvas1 = FigureCanvasTkAgg(self.fig,self.root)

        self.canvas1.draw()
        self.canvas1.get_tk_widget().place(x=50,y=220)

    def pro(self):
        pass

class Profile:
    def __init__(self,username):
        self.username = username


        self.wallet = CTk.CTk()
        self.wallet.state("zoomed")

        self.wlabel0 = CTk.CTkLabel(self.wallet,text=f'Hello {self.username}',font=('Courier',30)).place(x=80,y=40)

        self.balance = bef.getbalance(f'{self.username}')
        self.wlabel1 = CTk.CTkLabel(self.wallet,text="BALANCE AVAILABLE",font=('Courier',30)).place(x=80,y=200)
        self.wlabel2 = CTk.CTkLabel(self.wallet,text=f'{self.balance} USD',font=('Courier',20)).place(x=80,y=240)
        
        self.amt = tk.StringVar()
        self.wlabel3 = CTk.CTkLabel(self.wallet,text="ENTER THE AMOUNT",font=('Courier',20)).place(x=80,y=450)
        self.wentry0 = CTk.CTkEntry(self.wallet,textvariable = self.amt).place(x=350,y=450)
        self.addbut = CTk.CTkButton(self.wallet,text="DEPOSIT MONEY",font=('Courier',20),command =self.add).place(x=80,y=530)
        self.withdrawbut = CTk.CTkButton(self.wallet,text="WITHDRAW MONEY",font=('Courier',20),command = self.withdraw).place(x=300,y=530)

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
    abc = CurrencyDetails('aman','bitcoin')
    abc.root.mainloop()
