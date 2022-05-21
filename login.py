
from tkinter import *
from tkinter import ttk
import sqlite3
from usersdatabase import UsersDataBase


class LogIn(ttk.Frame):

    global _user_name, _password

    def __init__(self, windows):
    # def __init__(self, ):
        super().__init__()
        #self.rowconfigure(0, weight = 1)
        #self.columnconfigure(0, weight = 1)
        self.database = UsersDataBase()
        self.is_login = False
        self.permession = ""

        self.frame = ttk.Frame(self)
        self.frame.grid(row =0, column = 0)
        user_name_label = ttk.Label(self.frame, text = "User Name: ")
        user_name_label.grid(row = 0, column = 0, pady = (10,10))

        self.user_name = StringVar()
        user_name_entry = ttk.Entry(self.frame, textvariable = self.user_name)
        user_name_entry.grid(row = 0, column = 1, pady = (10,10))
        user_name_entry.insert(END, "admin")

        password_label = ttk.Label(self.frame, text="Password: ")
        password_label.grid(row=1, column=0, pady = (10,10))

        self.password = StringVar()
        password_entry = ttk.Entry(self.frame, textvariable = self.password, show = "*")
        password_entry.grid(row=1, column=1, pady = (10,10))

        self.label = ttk.Label(self.frame, text = "wrong password or username")
        self.label.configure(foreground="red")
        self.label.grid(row=2, column=0, columnspan=2)
        self.label.grid_forget()

        label_version = ttk.Label(self.frame, text="Version: ")
        label_version.grid(row=3, column=0)
        radioframe = ttk.Frame(self.frame)
        radioframe.grid(row = 3, column = 1)

        self.selectedVersion = StringVar()
        self.selectedVersion.set("v2")
        checkboxV1 = ttk.Radiobutton(radioframe, text = "V1", value = 'v1', variable = self.selectedVersion)
        checkboxV2 = ttk.Radiobutton(radioframe, text="V2", value='v2', variable=self.selectedVersion)
        checkboxV1.grid(row = 0, column = 0)
        checkboxV2.grid(row = 0, column = 1)
        print("version: ", self.selectedVersion.get())
        # self.mainloop()

    def log_in(self):
        data = self.database.pump_all(self.user_name.get())
        self.permession = data[0][2]
        print("data: ", data)
        if len(data)>0:
            password = data[0][1]
            imput_password = self.password.get()

            if imput_password == password:

                self.is_login = True
            else:
                self.label.grid(row=2, column=0, columnspan=2)
                self.label.update()


    def get_access_permission(self):
        return self.is_login

    def get_permession(self):
        return self.permession

if __name__ == '__main__':
    # LogIn()
    pass
