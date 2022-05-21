
from tkinter import *
from customerdatabase import CustomerDataBase
import sqlite3
from tkinter import ttk

class NewCustomer(ttk.Frame):

    def __init__(self):
        super().__init__()
        self.database = CustomerDataBase()
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

        frame = ttk.Frame(self)
        frame.grid(row = 0, column = 0, sticky = (N,S,E,W))
        user_label = ttk.Label(frame, text = "User Name: ")
        user_label.grid(row = 0, column = 0, padx = (200,5), pady = (100,5))
        self.Customer_name = StringVar()
        self.user_entry = ttk.Entry(frame, textvariable = self.Customer_name)
        self.user_entry.grid(row = 0, column = 1, padx = (5,5), pady = (100,5))

        phone_label = ttk.Label(frame, text = "Phone Number: ")
        phone_label.grid(row = 1, column = 0, padx = (200,5), pady = (5,5))

        self.Customer_phone = StringVar()
        self.phone_entry = ttk.Entry(frame, textvariable = self.Customer_phone)
        self.phone_entry.grid(row = 1, column = 1, padx = (5,5), pady = (5,5))

        inwi_label = ttk.Label(frame, text = "Inwi %: ")
        inwi_label.grid(row = 2, column = 0, padx = (200,5), pady = (5,5))
        self.inwi_per = StringVar()
        self.inwi_entry = ttk.Entry(frame, textvariable = self.inwi_per)
        self.inwi_entry.grid(row = 2, column = 1, padx = (5,5), pady = (5,5))

        jawal_label = ttk.Label(frame, text = "Jawal %: ")
        jawal_label.grid(row = 3, column = 0, padx = (200,5), pady = (5,5))
        self.jawal_per = StringVar()
        self.jawal_entry = ttk.Entry(frame, textvariable = self.jawal_per)
        self.jawal_entry.grid(row = 3, column = 1, padx = (5,5), pady = (5,5))

        orange_label = ttk.Label(frame, text = "Orange %: ")
        orange_label.grid(row = 4, column = 0, padx = (200,5), pady = (5,5))

        self.orange_per = StringVar()
        self.orange_entry = ttk.Entry(frame, textvariable = self.orange_per)
        self.orange_entry.grid(row = 4, column = 1, padx = (5,5), pady = (5,5))

        btn_add_customer = ttk.Button(frame, text = "Add", width = 20, command = self.addnewCustomer)
        btn_add_customer.grid(row = 5, column = 0, columnspan = 2, pady = (5,5), padx = (200,5))



    def addnewCustomer(self):

        _name = self.Customer_name.get()
        _phone = self.Customer_phone.get()
        _inwi = self.inwi_per.get()
        _jawal = self.jawal_per.get()
        _orange = self.orange_per.get()
        print(_name, _phone)
        self.database.insert(_name,_phone,_inwi,_jawal,_orange)
        self.phone_entry.delete(0, END)
        self.user_entry.delete(0, END)
        self.inwi_entry.delete(0, END)
        self.jawal_entry.delete(0, END)
        self.orange_entry.delete(0, END)
        # self.createCustomerdatabase(_name.replace(" ","_"))


    def createCustomerdatabase(self, name):
        database = sqlite3.connect(f"/home/exsar/PycharmProjects/python_oop_Gui/Recharge/UsersDataBase/{name}.db")
        try:
            cursor = database.cursor()
            cursor.execute(f"CREATE TABLE {name} (date, total, pay, rest)")
        except sqlite3.OperationalError:
            pass
        finally:
            database.commit()
            database.close()