from tkinter import *
from tkinter import ttk
from invoicedatabase import InvoiceDataBase
from InvoiceOnPaper import Invoice
from customerdatabase import CustomerDataBase
from datetime import date, datetime
from tkinter import messagebox


class Mytree (ttk.Treeview):
    columns = ["number", "type", "total"]

    def __init__(self, windows, **kw):
        super().__init__(windows, **kw)
        # show = "headings" insure the tree show only the column you insert
        self.configure(columns=self.columns, show="headings", height=15)
        self.heading("number", text="Quantity")
        self.heading("type", text="Type")
        self.heading("total", text="AMOUNT")
        self.configure(padding="10 5 5 5")
        self.column("0", anchor=CENTER)
        self.column("1", anchor=CENTER)
        self.column("2", anchor=CENTER)


class Frame2 (Frame):

    def __init__(self):
        super().__init__()
        self.database = CustomerDataBase()
        self.configure(background="white")
        # we store credit of each customer when we select it in option menu and get it from database
        self.credit = 0
        # this total = invoice total + rest
        self.bill_total_add_credit = 0
        # this only for current invoice
        self.bill_total = 0
        # this rest value is for current invoice
        self.restvalue = 0
        # this variable is for to check if the bill is saved to database
        self.saved = False

        self.pay = 0
        """ this variable store the name of the customerwhrn we select it in the optionMenu
            and we but the default value is "Customer" 
        """
        self.customer_selected_name = "Customer"

        self.old_date = []

        today = date.today()
        day_format = "%d/%m/%Y"

        time_frame = Frame(self, background="yellow")
        time_frame.grid(row=0, column=0)
        self.today_date = today.strftime(day_format)
        date_label = Label(time_frame, text=self.today_date, background="yellow", foreground="black")
        date_label.grid(row=0, column=0, columnspan=2)

        self.time_libel = Label(time_frame, text="00:00:00", background="yellow", foreground="black")
        self.time_libel.grid(row=1, column=0)
        self.getCurrentTime()
        self.quantity = StringVar()
        self.quantity_label = Entry(self, background="white", textvariable=self.quantity, foreground="black")
        self.quantity_label.grid(row=1, column=0, columnspan=2)

        self.select = StringVar()
        self.select.set("Select")
        items = ["Jawal 05", "Jawal 10", "Jawal 20", "Jawal 50", "Jawal 100", "Jawal 500", "Jawal 1000",
                 "Inwi 05", "Inwi 10", "Inwi 20", "Inwi 50", "Inwi 100", "Inwi 500", "Inwi 1000", "Inwi 5000",
                 "Orange 05", "Orange 10", "Orange 20", "Orange 30", "Orange 50", "Orange 100", "Orange 500",
                 "Orange 1000"]

        self.option = OptionMenu(self, self.select, *items)
        self.option.configure(width = 15, background = "#0093AB", activebackground = "#006778")
        self.option.grid(row=2, column= 0, columnspan = 2)
        self.option["menu"].configure(background = "white", foreground = "black")

        # we intialized out TreeView
        self.tree = Mytree(self)
        self.tree.grid(row=0, column= 2, sticky = (N), rowspan = 15)



        add_btn = Button(self, text = "Add", width = 17, background = "#0093AB", foreground = "white", activebackground = "#006778", command = self.add_to_treeView)
        add_btn.grid(row = 3 , column = 0, padx = (9, 6), columnspan = 2)

        remove_btn = Button(self, text = "Remove", width = 17, background = "#0093AB", foreground = "white", activebackground = "#006778", command = self.remove_from_treeView)
        remove_btn.grid(row = 4 , column = 0, padx = (9, 6), columnspan = 2)

        t_frame = Frame(self, background = "white")
        t_frame.grid(row = 5, column = 0)

        total_label_text = Label(t_frame, text = "total", background = "white", foreground = "black")
        total_label_text.grid(row = 0, column = 0, pady = (0, 5))

        sep = ttk.Separator(t_frame, orient = "horizontal")
        sep.grid(row = 1, column = 0,  columnspan = 3, sticky = (E, W))

        self.total_label_value = Label(t_frame, text = "0.0", width = 19, background = "white", foreground = "black")
        self.total_label_value.grid(row = 2, column = 0, padx = (10, 5), pady = (10, 0))

        self.CreateOptionMenu()

        credit_label_text = Label(self, text = "Credit: ", background = "white", foreground = "black")
        credit_label_text.grid(row = 1, column = 3, padx = (10, 10), sticky = N)

        self.credit_label_value = Label(self, text ="0.0", background ="white", foreground ="black")
        self.credit_label_value.grid(row = 2, column = 3, padx = (10, 10), sticky = N)

        sep = ttk.Separator(self, orient = "horizontal")
        sep.grid(row = 3, column = 3, sticky = (E, W, N))

        discount_label = Label(self, text = "Discount ", background = "white", foreground = "black")
        discount_label.grid(row=4, column=3, padx=(10, 10), sticky=N)

        discount_frame = Frame(self, background = "white")
        discount_frame.grid(row=5, column=3, padx=(10, 10), sticky=N)

        inwi_discount_label = Label(discount_frame, text="Inwi : ", background="white", foreground="black")
        inwi_discount_label.grid(row = 0 , column = 0, pady = (0, 10))

        self.inwidiscount = StringVar()
        inwi_discount_entry = Entry(discount_frame, textvariable = self.inwidiscount, width = 10, background="white", foreground="black")
        inwi_discount_entry.grid(row =0, column=1, padx=(10, 0))
        inwi_discount_entry.insert(END, 6)

        jawal_discount_label = Label(discount_frame, text="Jawal : ", background ="white", foreground="black")
        jawal_discount_label.grid(row=1, column =0, pady=(0, 10))

        self.jawaldiscount = StringVar()
        jawal_discount_entry = Entry(discount_frame, textvariable=self.jawaldiscount, width=10, background="white", foreground="black")
        jawal_discount_entry.grid(row=1, column=1, padx=(10, 0))
        jawal_discount_entry.insert(END, 6)

        orange_discount_label = Label(discount_frame, text = "Orange : ", background = "white", foreground = "black")
        orange_discount_label.grid(row=2, column=0, pady=(0, 10))

        self.orangediscount = StringVar()
        orange_discount_entry = Entry(discount_frame, textvariable=self.orangediscount,width=10, background="white", foreground="black")
        orange_discount_entry.grid(row=2, column=1, padx=(10, 0))
        orange_discount_entry.insert(END, 6)


        f = Frame(self, background = "white")
        f.grid(row = 16, column = 2, sticky = W, padx = (5, 5), pady = (10, 5))

        total_after_add_rest = Label(f, text = "Total: ", background = "white", foreground = "black")
        total_after_add_rest.grid(row =0, column = 0, sticky = W, padx = (0, 10), pady = (5, 5))

        self.total_after_add_rest_value_label = Label(f,text="0.0 dh", background="white", foreground="black")
        self.total_after_add_rest_value_label.grid(row=0, column=1, sticky=W, padx=(40, 10), pady=(5, 5))

        sep = ttk.Separator(f, orient = "horizontal")
        sep.grid(row = 1, column = 0,  columnspan = 4, sticky = (E,W))

        pay_label = Label(f,text = "Pay: ", background = "white", foreground = "black")
        pay_label.grid(row = 2, column = 0, sticky = W, padx = (0, 10), pady = (5, 5))

        self.payvariable = StringVar()
        self.pay_entry = Entry(f, textvariable = self.payvariable, background = "white", foreground = "black")
        self.pay_entry.grid(row = 2, column = 1)

        confirm_btn = Button(f,text = "Calculate", background = "#0093AB", foreground = "white", activebackground = "#006778", command = self.Calculatebtn)
        confirm_btn.grid(row = 2, column = 2, padx = (40,0), pady = (5,5))

        sep = ttk.Separator(f, orient = "horizontal")
        sep.grid(row = 3, column = 0,  columnspan = 4, sticky = (E,W))

        rest_after_pay = Label(f,text = "Rest: ", background = "white", foreground = "black")
        rest_after_pay.grid(row =4, column = 0, sticky = W, padx = (0, 10), pady = (5,5))

        self.rest_after_pay_value = Label(f,text = "0.0 dh", background = "white", foreground = "black")
        self.rest_after_pay_value.grid(row = 4, column = 1, sticky = W, padx = (40, 10), pady = (5,5))

        save_invoice_btn = Button(f, text = "Save Invoice", background = "#0093AB", foreground = "white", activebackground = "#006778")
        save_invoice_btn.configure(command = self.Save_data_to_data_base)
        save_invoice_btn.grid(row = 5, column = 2, padx = (70,10), sticky  = W)

        print_invoice_btn = Button(f, text = "Print", background = "#0093AB", foreground = "white", activebackground = "#006778")
        print_invoice_btn.configure(command = self.PrintInvoice)
        print_invoice_btn.grid(row = 5, column = 3, padx = (20,0))

        self.keepListenToChange_and_update()

        # self.mainloop()


    # this function activate when we click on calculate btn it calculate total - pay = rest
    def Calculatebtn(self):
        try:
            self.pay = float(self.payvariable.get())
            # this format func is for get rid of all dicimal number and left only 2 digits
            # to know why this is happening search for  "Floating-Point Arithmetic"
            self.restvalue = float(format(self.bill_total_add_credit - self.pay, '.2f'))
            print(self.restvalue)
            self.rest_after_pay_value["text"] = format(self.restvalue ,".2f")+ " dh"


        except ValueError:
            print("you cant enter string")



    # this func if for add to teeview
    def add_to_treeView(self):
        tag = ""
        # we get number from entry
        total = 0
        try:
            num = int(self.quantity.get())
            if num>0:
                price = int(self.getvalue(self.select.get()))
                # self.select it a variable store item we selected from option menu
                selecteditem = self.select.get()
                # we need to ckeck if the selected is Inwi that why we only take the first letter in the word
                # because we only  have 3 word be diffent first letter
                if selecteditem[0:1] == "I":
                    inwi = float(self.inwidiscount.get())
                    total = (num * price) - (num * price) * inwi / 100
                    tag = "inwi"
                    self.tree.tag_configure(tag, background="#F900BF", foreground = "white", font = ("Bold",10,"italic"))
                elif selecteditem[0:1] == "J":
                    jawal = float(self.jawaldiscount.get())
                    total = (num * price) - (num * price) * jawal / 100
                    """ because we want to set bg color for each type of product that why we change tag variable each time we select deferent product 
                        that how we can change bg color each time
                    """
                    tag = "jawal"
                    self.tree.tag_configure(tag, background="#FF5F00", foreground="white", font=("Bold",10,"italic"))
                elif selecteditem[0:1] == "O":
                    orange = float(self.orangediscount.get())
                    total = (num * price) - (num * price) * orange / 100

                    tag = "orange"
                    self.tree.tag_configure(tag , background="#FF1700", foreground="white", font=("Bold",10,"italic"))


                self.bill_total += total
                self.total_label_value["text"] = str(format(self.bill_total, ".2f")) + " dh"

                # insert to tree view
                self.tree.insert("", END, value=(self.quantity.get(), self.select.get(), total), tags=tag)
                self.quantity_label.delete(0, END)

                self.bill_total_add_credit = self.cF(self.bill_total + self.credit)
                self.total_after_add_rest_value_label["text"] = str(self.cF(self.bill_total_add_credit)) + " dh"
            else:
                messagebox.showwarning("Error", "You Cant Enter 0 as input")
        except ValueError:
            messagebox.showwarning("Error","You input is not valid try again")


    def remove_from_treeView(self):
        """ self.tree.selection()
            this function return id of rows that we selected in tree in type of tuple
            we loop throw tuple to get id of each row .

        """
        selected_item = self.tree.selection()
        total_value = 0
        for item in selected_item:
            total_value = float(self.tree.item(item)['values'][2])
            """ because we have to label that show total of current invoice and the total of current invoice and the rest from old invoice
            that when when we delete item from treen view we need to correct the value of this variable
            """

            self.bill_total -= self.cF(total_value)
            self.bill_total_add_credit -= self.cF(total_value)

            self.total_label_value['text'] = self.cF(self.bill_total)
            self.total_after_add_rest_value_label['text'] = self.cF(self.bill_total)


        for item in selected_item:
            self.tree.delete(item)

        self.saved = False

    def Save_data_to_data_base(self):

        if not self.saved :
            database = InvoiceDataBase()
            if self.bill_total_add_credit > 0:
                # here we loop throw tree and we get all data and insert it database
                children = []
                try:
                    children = self.tree.get_children()
                except TclError:
                    pass
                if len(children)>0:
                    for rows in children:
                        data = self.tree.item(rows)['values']
                        # this function insert data that we get from tree in insert it to database
                        database.insertfirstdata(self.today_date+" | "+self.getTimeNow(), self.customer_selected_name, data[0], data[1], data[2])

                    # this function insert some other data to data base thie functio after we insert all data in tree to database

                    database.insertlastdata(self.today_date +" | " + self.getTimeNow(), self.customer_selected_name, self.bill_total, self.bill_total_add_credit, self.pay, self.restvalue)
                    # this function update the rest value in data base of each customer
                    self.database.UpdateRest(self.customer_selected_name,self.restvalue)
                    self.pay_entry.delete(0,END)
            else:
                messagebox.showwarning("Error","Youdon't have Invoice to Store")


            # after we insert all tree data to data base we free tree from data
            children2 = self.tree.get_children()
            if len(children2)>0:
                for row in children2:
                    self.tree.delete(row)

            self.total_label_value["text"] = "0.0 dh"
            self.total_after_add_rest_value_label["text"] = "0.0 dh"

            self.restbyname = 0
            # this total = invoice total + rest
            self.bill_total_add_credit = 0
            # this only for current invoice
            self.bill_total = 0
            # this rest value is for current invoice
            self.restvalue = 0

            self.pay = 0
            self.saved = True

        else:
            messagebox.showwarning("save bill", "you already saved the bill")



    # this functio return the value of each item
    def getvalue(self, key):
        my_dic = {"Inwi 05": 5,
                  "Inwi 10": 10,
                  "Inwi 20": 20,
                  "Inwi 50": 50,
                  "Inwi 100": 100,
                  "Inwi 500": 500,
                  "Inwi 1000": 1000,
                  "Jawal 05": 5,
                  "Jawal 10": 10,
                  "Jawal 20": 20,
                  "Jawal 50": 50,
                  "Jawal 100": 100,
                  "Jawal 500": 500,
                  "Jawal 1000": 1000,
                  "Orange 05": 5,
                  "Orange 10": 10,
                  "Orange 20": 20,
                  "Orange 30": 30,
                  "Orange 50": 50,
                  "Orange 100": 100,
                  "Orange 500": 500,
                  "Orange 1000": 1000,
                  }
        return my_dic[key]
    customer_label = None

    # from it's name it's just functio for creating option menu

    def CreateOptionMenu(self):

        users = []

        for name in self.database.dumpcolumn("name"):
            users += [name[0]]

        if len(self.old_date) < len(users) or len(users) < len(self.old_date):
            self.old_date = users
            selected = StringVar()
            selected.set("Customer")
            option = OptionMenu(self, selected, *users, command=self.selectedItem)
            option.configure(width=15, background="#0093AB", activebackground="#006778")
            option["menu"].configure(background="white", foreground="black")
            option.grid(row=0, column=3, pady=(5, 0), sticky=N)

            print(selected.get())

        self.after(100, self.CreateOptionMenu)
        # return option





    # this functio is for option menu is give us the item that we select in the option menu (name)
    def selectedItem(self, name):

        # we get the customer name
        self.customer_selected_name = name
        self.credit = self.database.getRest(name)
        print(self.credit)
        # get rest of the customer from database
        self.credit_label_value["text"] = self.credit
        # self.restbyname = self.database.getRest(name)
        self.bill_total_add_credit = self.credit
        self.total_after_add_rest_value_label["text"] = str(self.bill_total_add_credit) + " dh"

        # each customer has his discount percent that why we store it in database
        # and we call it when we need it
        dis = self.database.getdiscountpercent(name)

        # the return value from database if list of tuple [(6.5,7,6.75)]
        self.inwidiscount.set(dis[0][0])
        self.jawaldiscount.set(dis[0][1])
        self.orangediscount.set(dis[0][2])

    # this fucn return time is this format 00:00:00
    def getCurrentTime(self):
        today = date.today()
        current_time = datetime.now()
        format = "%H:%M:%S"
        mytime = current_time.strftime(format)
        self.time_libel["text"] = mytime
        self.after(1,self.getCurrentTime)

    # this fucn return time in 00:00 format and I dont want to store 00:00:00 this format in database
    def getTimeNow(self):
        today = date.today()
        current_time = datetime.now()
        format = "%H:%M"
        mytime = current_time.strftime(format)
        return mytime



    def cF(self, num):
        if num>-1:
            value = float(format(num, '.2f'))
            return abs(value)
        else:
            value = float(format(num, '.2f'))
            return value



    def keepListenToChange_and_update(self):
        self.total_after_add_rest_value_label["text"] = \
            str(self.cF(self.bill_total_add_credit)) + " dh"
        self.bill_total_add_credit = self.bill_total + self.database.getRest(self.customer_selected_name)
        # I put float inside str because i want print on the screen 0.0 dh if don't put float will only print 0 dh
        self.rest_after_pay_value["text"] = str(float(self.restvalue)) + " dh"
        self.after(100, self.keepListenToChange_and_update)
        self.credit_label_value["text"] = self.database.getRest(self.customer_selected_name)


    def PrintInvoice(self):
        children = self.tree.get_children()
        data = []
        for item in children:
            data.append(self.tree.item(item)["values"])
        Invoice(data, date=self.today_date,
                customerName=self.customer_selected_name,
                invoice_total=self.cF(self.bill_total),
                restb=self.cF(self.database.getRest(self.customer_selected_name)),
                restafter=self.cF(self.restvalue),
                total=self.cF(self.bill_total_add_credit),
                pay=self.pay)



if __name__ == "__main__":
    Frame2()
    # pass