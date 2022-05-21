

from tkinter import *
from usersdatabase import UsersDataBase
from tkinter import ttk

class NewUser(Frame):

    def __init__(self):
        super().__init__()
        self.database = UsersDataBase()
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

        frame = ttk.Frame(self)
        frame.grid(row = 0, column = 0, sticky = (N,S,E,W))
        user_label = ttk.Label(frame, text = "User Name: ")
        user_label.grid(row = 0, column = 0, padx = (200,5), pady = (100,5))

        self.userName = StringVar()
        self.user_entry = ttk.Entry(frame, textvariable = self.userName)
        self.user_entry.grid(row = 0, column = 1, padx = (5,5), pady = (100,5))

        password_label = ttk.Label(frame, text = "Password: ")
        password_label.grid(row = 1, column = 0, padx = (200,5), pady = (5,5))

        self.password = StringVar()
        self.password_entry = ttk.Entry(frame, textvariable = self.password)
        self.password_entry.grid(row = 1, column = 1, padx = (5,5), pady = (5,5))

        permession_label = ttk.Label(frame, text = "Permission: ")
        permession_label.grid(row = 2, column = 0, padx = (200,5), pady = (5,5))
        self.permessionType = StringVar()
        self.permession_entry = ttk.Entry(frame, textvariable = self.permessionType)
        self.permession_entry.grid(row = 2, column = 1, padx = (5,5), pady = (5,5))

        permession_type = ttk.Label(frame, text = "high\low")
        permession_type.grid(row = 2, column = 2)



        btn_add_customer = ttk.Button(frame, text = "Add", width = 20, command = self.addnewCustomer)
        btn_add_customer.grid(row = 5, column = 0, columnspan = 2, pady = (5, 5), padx = (200, 5))

        #self.mainloop()

    def addnewCustomer(self):
        user_name = self.userName.get()
        psw = self.password.get()
        per = self.permessionType.get()
        self.database.insertdata(user_name, psw, per)





