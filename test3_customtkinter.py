# Importing the tkinter module
import customtkinter as CTk
import tkinter as tk
from tkinter import ttk



general_font=('Times 18')
large_font = ('Times 30')
current_theme='dark'
class MainWindow:
    def __init__(self,username):
        self.window = CTk.CTk()
        self.frame = CTk.CTkFrame(self.window,
                                  bg='red',
                                  width=1300,height=850)
        self.frame.place(x=170,y=0)
        #Window will be at maximum windowed size
        self.window.state('zoomed')
        #Window Title
        self.window.title("Crypto")

        self.user_label = CTk.CTkLabel(text=f"{username}",
                          text_font=general_font)
        self.user_label.place(x=0,y=0)
        
        #Wishlist Button
        self.wishlist_Button = CTk.CTkButton(master=self.window,
                               text="Wishlist",
                                             command=self.wishlist_func,
                                             height=50,width=125,
                                             text_font=general_font)
        self.wishlist_Button.place(x=0,y=70)
        
        #BuyIN Button
        self.buyin_Button = CTk.CTkButton(master=self.window,
                            text="BuyIN",
                            command=self.buyin_func,
                            height=50,width=125,
                            text_font=general_font)
        self.buyin_Button.place(x=0,y=150)
        
        #Sellout Button
        self.sellout_Button = CTk.CTkButton(master=self.window,
                              text="Sellout",
                              command=self.sellout_func,
                              height=50,width=125,
                              text_font=general_font)
        self.sellout_Button.place(x=0,y=230)
        
        #Wishlist Button
        self.holdlist_Button = CTk.CTkButton(master=self.window,
                               text="Holdlist",
                               command=self.holdlist_func,
                               height=50,width=125,
                               text_font=general_font)
        self.holdlist_Button.place(x=0,y=310)
        
        #Theme Button
        self.theme_Button = CTk.CTkSwitch(master=self.window,
                            text="Dark Theme",
                            command=self.change_theme)
        self.theme_Button.place(x=0,y=700)
        #Exit button
        self.exit_Button = CTk.CTkButton(text="Exit",
                           command=self.exit_func,
                           height=50,width=70,
                           text_font=general_font)
        self.exit_Button.place(x=10,y=400)
        
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
        self.new_frame.display_list()
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
        self.window = window
        self.frame = CTk.CTkFrame (self.window,
                                width=1300,height=850)
        self.frame.place(x=170,y=0)
        self.title = CTk.CTkLabel(self.frame,
                                  text="Wish List",
                                  text_font=general_font)
        self.title.place(x=0,y=0)

    def display_list(self):
        #Header titles
        columns = ('s no.','symbol', 'name', 'price')
        self.inner_frame = CTk.CTkFrame(self.frame,width=850,height=670)
        self.inner_frame.place(x=70,y=30)
        self.tree = ttk.Treeview(self.inner_frame, 
                                 columns=columns,
                                 show='headings',
                                 height=15)# height is the number of rows to be displayed
        
        #Set style for table (to alter fields design)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        #Configuration of Header fields
        self.style.configure("Treeview.Heading",
                             font=general_font,
                             background="#5e6063",
                             foreground='white')
        
        #Configuration of Row fields
        self.style.configure("Treeview",
                             font=('Times', 15),
                             rowheight=50,
                             background="#646669",
                             foreground='white')
        self.style.configure('.',borderwidth = 0)
        # Define headings
        for col in columns:
            self.tree.column(col,anchor='center',width=250)
            self.tree.heading(col, text=col.upper())

        # Generate sample data
        data = []
        for i in range(26):
            data.append((f'{i}', f'{chr(65+i)}', f'crypto{i+1}',f'{i+100}'))

        # Add data to the treeview
        for row in data:
            self.tree.insert('', CTk.END, values=row)
        self.tree.place(x=20,y=20)

class wishlist_window:
    def __init__(self):
        win = CTk.Toplevel()
        win.state('zoomed')

class boughtlist_frame:
    def __init__(self,window):
        self.window = window
        self.color="orange"
        self.frame = CTk.CTkFrame(self.window,
                                  width=1300,height=850)
        self.frame.place(x=170,y=0)
        self.label = CTk.CTkLabel(self.frame,
                                  text="Bought List")
        self.label.place(x=0,y=0)

class soldlist_frame:
    def __init__(self,window):
        self.window = window
        self.frame = CTk.CTkFrame(self.window,
                                  width=1300,height=850)
        self.frame.place(x=170,y=0)
        self.label = CTk.CTkLabel(self.frame,
                                  text="Sold List")
        self.label.place(x=0,y=0)

class holdlist_frame:
    def __init__(self,window):
        self.window = window
        self.frame = CTk.CTkFrame(self.window,
                                  width=1300,height=850)
        self.frame.place(x=170,y=0)
        self.label = CTk.CTkLabel(self.frame,
                                  text="Hold List")
        self.label.place(x=0,y=0)

#Main program execution
if (__name__=="__main__"):
    app = MainWindow("Whitedevil")
    app.window.mainloop()
    