from tkinter import *
from tkinter import ttk
from newcustomer import NewCustomer
from MakeBill import Frame2
from MakeBillV2 import Bill
from browserdatabase import BrowserDataBase
from browsercustomers import BrowserCustomers
from newuser import NewUser
from login import LogIn
from stock import Stock
import time

class Recharge (Tk):

    def __init__(self):
        super().__init__()
        self.title("---Recharge---")
        self.geometry("1100x700")
        self.maxsize(width = 1300, height = 700)
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)


        frame = ttk.Frame(self)
        frame.grid(row = 0, column = 0, sticky = (N,S,W,E))
        frame.columnconfigure(0, weight = 1)
        frame.rowconfigure(0, weight = 1)
        # this instance for login frame
        self.login_frame = LogIn(frame)
        self.login_frame.grid(row = 0, column = 0)

        """ I initiated this button here even it belong to login frame 
            because I want to press action of this button to happen her
        """
        btn_login = ttk.Button(self.login_frame.frame, text = "Login", command = self.press_login)
        btn_login.grid(row = 4, column = 0, columnspan = 2, pady = (10, 10))


        #self.buildHome()

        self.mainloop()


    def press_login(self):
        self.login_frame.log_in()
        if self.login_frame.get_access_permission():
            # after loging success we hide login frame
            self.login_frame.grid_remove()
            self.buildHome()



    def buildHome(self):
        self.update()
        noteBook = ttk.Notebook(self)
        noteBook.grid(row=0, column=0, sticky=(N, S, E, W))

        buildInvoiceV1 = Frame2()
        buildInvoiceV2 = Bill()
        browserInvoices = BrowserDataBase()
        add_new_customer = NewCustomer()
        browser_customers = BrowserCustomers()
        new_user = NewUser()
        stock = Stock()

        img_customer = PhotoImage(file = "../Recharge/Icon/add_customer.png")
        img_invoice = PhotoImage(file = "../Recharge/Icon/invoice.png")
        img_invoice_browser = PhotoImage(file = "../Recharge/Icon/invoice_browser.png")
        img_customer_b = PhotoImage(file = "../Recharge/Icon/browser_customer.png")
        img_newuser = PhotoImage(file="../Recharge/Icon/new_user.png")
        img_stock = PhotoImage(file = "../Recharge/Icon/stock.png")

        if self.login_frame.selectedVersion.get() == "v1":
            noteBook.add(buildInvoiceV1, image=img_invoice)
        elif self.login_frame.selectedVersion.get() == "v2":
            noteBook.add(buildInvoiceV2, image=img_invoice)

        noteBook.add(browserInvoices, image = img_invoice_browser)
        noteBook.add(add_new_customer, image = img_customer)
        noteBook.add(browser_customers, image = img_customer_b)
        if self.login_frame.get_permession() != "low":
            noteBook.add(new_user, image = img_newuser)
            noteBook.add(stock, image = img_stock)




        # this scrollbar is just for decoration
        sc = ttk.Scrollbar(self, orient = "vertical")

        sc.grid(row = 0, column = 1, sticky = (N,S))
        self.mainloop()



def main():
    recharge = Recharge()



if __name__ == "__main__":
    main()

