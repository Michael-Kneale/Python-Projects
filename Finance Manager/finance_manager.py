from __future__ import print_function
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import * #"????"
from tkinter import *
from tkinter import messagebox
from urllib.request import pathname2url

import sqlite3

import urllib
import json

#import numpy as np

HUGE_FONT= ("Verdana", 46)
LARGE_FONT= ("Verdana", 20)
MEDIUM_FONT= ("Verdana", 16)
SMALL_FONT= ("Verdana", 8)


    
def ExitApplication():
    MsgBox = messagebox.askquestion ('Exit Application','Are you sure you want to exit the application?',icon = 'warning')
    if MsgBox == 'yes':
        quit(app)
    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen')

#Creates database first time around (afterwards it connects to the one already created)
connection = sqlite3.connect('address_book.db')

#Creates cursor
c = connection.cursor()


#Creates table (only needs to happen first time running the program)



c.execute("""CREATE TABLE IF NOT EXISTS addresses (
        date integer,
        cost integer,
        category text
        )""")

    
class finance(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "Finance Manager")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):

            frame= F(container, self)

            frame.configure(bg="#FFFFFF")
                           
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()




class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Finances 2019-2020", font=HUGE_FONT)
        label.grid(row=0, column=1)

        button1 = ttk.Button(self, text="Enter expenses",
                            command=lambda: controller.show_frame(PageOne))
        button1.grid(row=1, column=1)

        button2 = ttk.Button(self, text="View expenses",
                            command=lambda: controller.show_frame(PageTwo))
        button2.grid(row=2, column=1)

        canvas1 = tk.Canvas(self, width = 300, height = 300, bg="#FFFFFF", highlightthickness=0)
        canvas1.grid(row=3, column=1)


        button1 = tk.Button (self, text='Exit application',command=ExitApplication)
        canvas1.create_window(150, 150, window=button1)

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label1 = tk.Label(self, text="Enter expenses", font=LARGE_FONT)
        label1.grid(row=0, column=0)
        label1.config(bg="#FFFFFF")
    
        label2 = tk.Label(self, text="Date", font=MEDIUM_FONT)
        label2.grid(row=1, column = 0, sticky="sw")
        label2.config(bg="#FFFFFF")


        label3 = tk.Label(self, text="Cost", font=MEDIUM_FONT)
        label3.grid(row=2, column = 0, sticky="sw")
        label3.config(bg="#FFFFFF")
        
        label4 = tk.Label(self, text="Category", font=MEDIUM_FONT)
        label4.grid(row=3, column = 0, sticky="sw")
        label4.config(bg="#FFFFFF")

        button1 = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=5, column=1, pady=10, padx=10)
        
        dateEntry = ttk.Entry(self)
        dateEntry.grid(row=1, column=1)


        variable = tk.StringVar()
        drop = ttk.OptionMenu(self, variable, "cars", "cars", "clothes", "electronics", "rates", "donations", "gas/electricity", "entertainment", "groceries", "gifts", "health", "holidays", "insurance", "house/garden", "books/music", "petrol", "school", "phone/internet", "transport", "water")
        drop.grid(row=3, column=1, sticky="ew")
        
        costEntry = ttk.Entry(self)
        costEntry.grid(row=2, column=1)

        def submit():
            connection = sqlite3.connect('address_book.db')
            c = connection.cursor()
            c.execute("INSERT INTO addresses VALUES (:date, :category, :cost)",
                {        
                    'date': dateEntry.get(),
                    'category': variable.get(),
                    'cost': costEntry.get()
                })
                    

            connection.commit()
            connection.close()
            
            
            dateEntry.delete(0, END)
            costEntry.delete(0, END)
            
        submitButton = ttk.Button(self, text="Add record to database", command=submit)
        submitButton.grid(row=4, column=1)
        
        #dateEntry.get()
        #entry2.get()
        #costEntry.get()
        
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="View expenses", font=LARGE_FONT)
        label.grid(row=0, column=0)
        label.config(bg="#FFFFFF")


        
        
        def delete():
            connection = sqlite3.connect('address_book.db')
            c = connection.cursor()

            c.execute("DELETE from addresses WHERE oid = " + deleteBox.get())
            
            connection.commit()
            connection.close()
            
        deleteButton = ttk.Button(self, text="Delete ID", command=delete)
        deleteButton.grid(row=3, column=1)
        deleteBox = ttk.Entry(self, width=30)
        deleteBox.grid(row=2, column=1)
        deleteBoxLabel = ttk.Label(self, text="ID Number")
        deleteBoxLabel.grid(row=2, column=0)
        

        button1 = ttk.Button(self, text="Back",
                            command=lambda: controller.show_frame(StartPage))
        button1.grid(row=3, column=2)


        def view():
            connection = sqlite3.connect('address_book.db')
            c = connection.cursor()

            c.execute("SELECT * FROM addresses")
            rows = c.fetchall()
            self.i = 0
            for row in rows:
                print(row)
                tree.insert("", tk.END, text=str(self.i), values=row)
    
                self.i = self.i + 1

                    


            connection.commit()
            connection.close()


        tree = ttk.Treeview(self)
        tree.grid(row=4, column=0, pady=20)
        tree['columns'] = ('cost', 'category', 'date')
        tree.heading('#0', text='ID number', anchor='w')
        tree.column('#0', anchor='w')
        tree.heading('#1', text='Cost')
        tree.column('#1', anchor='center', width=100)
        tree.heading('category', text='Category')
        tree.column('category', anchor='center', width=100)
        tree.heading('date', text='Date')
        tree.column('date', anchor='center', width=100)
        self.Treeview = tree

           

        viewButton = ttk.Button(text="view data", command=view)
        viewButton.pack()


app = finance()
app.resizable(False, False)
#app.iconbitmap("C:/Users/User-PC/Desktop/software_assignment/money2.ico")
app.geometry("633x600")

def on_closing():
    if messagebox.askokcancel("Exit Application", "Are you sure you want to exit the application?", icon = 'warning'):
        app.destroy()
    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen')
app.protocol("WM_DELETE_WINDOW", on_closing)

app.mainloop()

#Commits changes made to database/spreadsheet
connection.commit()

#Closes connection to database
connection.close()
