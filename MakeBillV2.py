
from tkinter import *
from tkinter import ttk
from Recharge.customerdatabase import CustomerDataBase
from Recharge.invoicedatabase import InvoiceDataBase
from Recharge.customerdatabase import CustomerDataBase
from datetime import datetime as dt
from Recharge.stock import StockDataBase
from tkinter import messagebox


class Bill(ttk.Frame):

    def __init__(self, **kw):
        super().__init__(**kw)

        #-------------Time 00:00:00
        self.time_label = ttk.Label(self, text = "00:00:00", background = "yellow", width = 10, anchor = "center")
        self.time_label.grid(row = 0, column = 0)
        self.today_date = self.getCurrentTime()
        #------------------quantity  entry
        frame_label_quantity = ttk.LabelFrame(self, text = "Quantity")
        frame_label_quantity.grid(row = 1, column = 0, sticky = (W,E))
        frame_label_quantity.columnconfigure(1, weight = 1)

        self.quantity = StringVar()
        self.quantity_entry = ttk.Entry(frame_label_quantity, justify = "center", textvariable = self.quantity)
        self.quantity_entry.grid(row = 0, column = 1, pady = (5,10))



        self.product = {
                    "Jawal 05":5,
                    "Jawal 10":10,
                    "Jawal 20":20,
                    "Jawal 50":50,
                    "Jawal 100":100,
                    "Jawal 500":500,
                    "Jawal 1000":1000,
                    "Inwi 05":5,
                    "Inwi 10":10,
                    "Inwi 20":20,
                    "Inwi 50":50,
                    "Inwi 100":100,
                    "Inwi 500":500,
                    "Inwi 1000":1000,
                    "Inwi 5000":5000,
                    "Orange 05":5,
                    "Orange 10":10,
                    "Orange 20":20,
                    "Orange 30":30,
                    "Orange 50":50,
                    "Orange 100":100,
                    "Orange 500":500,
                    "Orange 1000":1000,
                    "Orange 5000":5000,


        }
    #------------JAWAL------------------------------------#
        frame_label_jawal = ttk.LabelFrame(self, text = "Jawal")
        frame_label_jawal.grid(row = 2, column = 0, sticky = (W,E,N))

        i,j, = 0,0
        btn_jawal_list = []
        for name in self.product:
            if name[0:1] == "J":
                btn_jawal = ttk.Button(frame_label_jawal, text = name)
                btn_jawal.grid(row = i, column = j, ipadx = 5, ipady = 5, padx = 2, pady = 2)
                btn_jawal_list.append(btn_jawal)
                if j == 3:
                    i+=1
                    j = -1
                j+=1


        btn_jawal_list[0].configure(command = lambda : self.click_btn("Jawal 05"))
        btn_jawal_list[1].configure(command=lambda: self.click_btn("Jawal 10"))
        btn_jawal_list[2].configure(command=lambda: self.click_btn("Jawal 20"))
        btn_jawal_list[3].configure(command=lambda: self.click_btn("Jawal 50"))
        btn_jawal_list[4].configure(command=lambda: self.click_btn("Jawal 100"))
        btn_jawal_list[5].configure(command=lambda: self.click_btn("Jawal 500"))
        btn_jawal_list[6].configure(command=lambda: self.click_btn("Jawal 1000"))



    #----------------Inwi------------------------#
        frame_label_inwi = ttk.LabelFrame(self, text = "Inwi")
        frame_label_inwi.grid(row = 3, column = 0, sticky = (W,E,N))

        i,j, = 0,0
        btn_inwi_list = []
        for name in self.product:
            if name[0:1] == "I":
                btn_inwi = ttk.Button(frame_label_inwi, text = name)
                btn_inwi.grid(row = i, column = j, ipadx = 5, ipady = 5, padx = 2, pady = 2)
                btn_inwi_list.append(btn_inwi)
                if j == 3:
                    i+=1
                    j = -1
                j+=1


        btn_inwi_list[0].configure(command = lambda : self.click_btn("Inwi 05"))
        btn_inwi_list[1].configure(command=lambda: self.click_btn("Inwi 10"))
        btn_inwi_list[2].configure(command=lambda: self.click_btn("Inwi 20"))
        btn_inwi_list[3].configure(command=lambda: self.click_btn("Inwi 50"))
        btn_inwi_list[4].configure(command=lambda: self.click_btn("Inwi 100"))
        btn_inwi_list[5].configure(command=lambda: self.click_btn("Inwi 500"))
        btn_inwi_list[6].configure(command=lambda: self.click_btn("Inwi 1000"))
        btn_inwi_list[7].configure(command=lambda: self.click_btn("Inwi 5000"))


    #--------------------Orange----------------------------#
        frame_label_orange = ttk.LabelFrame(self, text = "Orange")
        frame_label_orange.grid(row = 4, column = 0, sticky = (W,N))

        i,j, = 0,0
        btn_orange_list = []
        for name in self.product:
            if name[0:1] == "O":
                btn_orange = ttk.Button(frame_label_orange, text = name, width = 10)
                btn_orange.grid(row = i, column = j, ipadx = 5, ipady = 5, padx = 2, pady = 2)
                btn_orange_list.append(btn_orange)
                if j == 3:
                    i+=1
                    j = -1
                j+=1


        btn_orange_list[0].configure(command = lambda : self.click_btn("Orange 05"))
        btn_orange_list[1].configure(command=lambda: self.click_btn("Orange 10"))
        btn_orange_list[2].configure(command=lambda: self.click_btn("Orange 20"))
        btn_orange_list[3].configure(command=lambda: self.click_btn("Orange 30"))
        btn_orange_list[4].configure(command=lambda: self.click_btn("Orange 50"))
        btn_orange_list[5].configure(command=lambda: self.click_btn("Orange 100"))
        btn_orange_list[6].configure(command=lambda: self.click_btn("Orange 500"))
        btn_orange_list[7].configure(command=lambda: self.click_btn("Orange 1000"))
        btn_orange_list[8].configure(command=lambda: self.click_btn("Orange 5000"))

    #------------Frame1 <optionMenu, creditLb, credit valuelv>
        frame1 = ttk.Frame(self,)
        frame1.grid(row = 0, column = 1, sticky = (W,N),)

    #--------------------OptionMenu inside Frame1------------------------------
        self.customerDataBase = CustomerDataBase()
        customer = self.customerDataBase.dumpcolumn('name')
        names = [name[0] for name in customer]

        selected = StringVar()
        selected.set("Customer")
        optionMenu = OptionMenu(frame1, selected, *names, command = self.Selected_customer)
        optionMenu.configure(background = "#EDE6DB", width = "10",
                             foreground = "black",
                             activebackground = "#B4E197", activeforeground = "white")
        optionMenu["menu"].configure(background = "#005555", foreground = "white", activebackground = "#069A8E", activeforeground = "white")
        optionMenu.grid(row = 0, column = 0, sticky = (W,N), ipadx = 5, ipady = 5, pady = (10, 0), padx = (30, 0))

        # ---------- Remove from TreeView-----------
        btn_remove = ttk.Button(frame1, text="Remove", command=self.RemoveFromTreeView)
        btn_remove.grid(row=1, column=0, sticky=(W, N), padx=(30, 0), pady=(10, 0))

        # -------------- remove all button ------------------
        # this button is for free out tree view from data

        btn_remove_all = ttk.Button(frame1, text = "Remove All", command = self.RemoveAll)
        btn_remove_all.grid(row = 1, column = 1, sticky = (W, N), padx = (30, 0), pady = (10, 0))

    #---------credit label name and value ---------------------------
        credit_label = ttk.Label(frame1, text = "Credit: ")
        credit_label.configure(foreground = "#001E6C")
        credit_label.grid(row = 0, column = 1, ipady = 5, ipadx = 5, padx = 30, pady = (10, 0))

        self.credit_label_value = ttk.Label(frame1, text = "0.0 dh")
        self.credit_label_value.configure(foreground = "#001E6C")
        self.credit_label_value.grid(row = 0, column = 2, ipady = 5, ipadx = 5, padx = 20, pady = (10, 0), sticky = W)

        # ---------------Discount frame1--------------
        discount_frame = ttk.Frame(frame1)
        discount_frame.grid(row=0, column = 3)

        inwi_discount_lable = ttk.Label(discount_frame, text = "Inwi %")
        inwi_discount_lable.grid(row = 0, column = 0)

        self.inwi_discount = StringVar()
        self.inwi_discount_entry = ttk.Entry(discount_frame, width = 8, textvariable = self.inwi_discount, justify = "center")
        self.inwi_discount_entry.grid(row = 1, column = 0)

        jawal_discount_lable = ttk.Label(discount_frame, text = "Jawal %")
        jawal_discount_lable.grid(row = 0, column = 1)

        self.jawal_discount = StringVar()
        self.jawal_discount_entry = ttk.Entry(discount_frame, width = 8, textvariable = self.jawal_discount, justify = "center")
        self.jawal_discount_entry.grid(row = 1, column = 1)


        orange_discount_lable = ttk.Label(discount_frame, text = "Orange %")
        orange_discount_lable.grid(row = 0, column = 2)

        self.orange_discount = StringVar()
        self.orange_discount_entry = ttk.Entry(discount_frame, width = 8, textvariable = self.orange_discount, justify = "center")
        self.orange_discount_entry.grid(row=1, column=2)
    #--------------------TreeView---------------------------------
        mystyle = ttk.Style()
        mystyle.configure('Treeview', rowheight = 20)
        columns = ["Quan", "Pro", "amount"]
        self.tree = ttk.Treeview(self, column = columns, show = "headings")
        self.tree.heading("Quan", text = "Quantity")
        self.tree.heading("Pro", text = "Product")
        self.tree.heading("amount", text="Amount")
        self.tree.column(0, anchor = "center")
        self.tree.column(1, anchor = "center")
        self.tree.column(2, anchor = "center")
        self.tree.grid(row = 1, column = 1, rowspan = 4, padx = (30,0), sticky = N, pady = (20,0))
        self.tree.configure(height = 16)

    #--------------Globale Variables------
        self.selected_customer = "Customer"
        self.credit = 0.0
        self.billTotal = 0.0
        self.Total = 0.0
        self.rest = 0.0
        self.pay = 0.0
        self.saved = False



    #--------------Frame2 pay, total+rest, save bill, print------------------------

        frame2 = ttk.Frame(self,)
        frame2.grid(row = 5, column = 1, sticky = (W, N), padx = (100, 0), pady = (5, 0))

        total_label = ttk.Label(frame2, text = "TOTAL: ")
        total_label.grid(row = 0, column = 0, sticky = (W))

        self.total_label_value = ttk.Label(frame2, text = "0.0 dh")
        self.total_label_value.grid(row = 0, column = 1, padx = (20,20))

        label_pay = ttk.Label(frame2, text = "Pay: ")
        label_pay.grid(row = 1, column = 0, pady = (10,0), sticky = (W))

        self.pay_value = StringVar()
        self.pay_value.set("0")
        entry_pay = ttk.Entry(frame2, textvariable = self.pay_value, width = 18)
        entry_pay.grid(row = 1, column = 1, padx = (10, 0), pady = (10,0))

        label_rest = ttk.Label(frame2, text = "Rest: ")
        label_rest.grid(row = 2, column = 0, pady = (10, 0), sticky = (W))

        self.label_rest_value = ttk.Label(frame2, text = "0.0 dh")
        self.label_rest_value.grid(row = 2, column = 1, padx = (20,20))

        #---------- save the bill btn------
        btn_save_bill = ttk.Button(frame2, text = "Save Bill", command = self.SaveBill)
        btn_save_bill.grid(row = 2, column = 3, sticky = (E), padx = 100)
        # self.mainloop()

    #---------------- this function will listen to ech change in my data on update it on the screen
        self.update_label_value()

    def click_btn(self, productType):
        # data = self.customerDataBase.getdiscountpercent(self.selected_customer)
        stockdatabase = StockDataBase()

        stock_Product_Quantity = int(stockdatabase.dumpProductQantity(productType)[0][0])
        product_quantity_ordered = int(self.quantity.get())
        rest = stock_Product_Quantity - product_quantity_ordered
        if rest < 0:
            messagebox.showwarning("Stock warning","you don't have this amount of product in you stock")
        else:

            INWI_DISCOUNT = float(self.inwi_discount.get())
            JAWAL_DISCOUNT = float(self.jawal_discount.get())
            ORANGE_DISCOUNT = float(self.orange_discount.get())

            price = int(self.product[productType])
            quantity = 0
            try:
                quantity = int(self.quantity.get())
                amount = 0.0
                tag = ""
                if productType[0:1] == "I":
                    tag = "Inwi"
                    amount = quantity * price - (quantity*price)*INWI_DISCOUNT/100
                if productType[0:1] == "J":
                    tag = "Jawal"
                    amount = quantity * price - (quantity * price) * JAWAL_DISCOUNT / 100
                if productType[0:1] == "O":
                    tag = "Orange"
                    amount = quantity * price - (quantity * price) * ORANGE_DISCOUNT / 100

                self.billTotal += amount

                item = self.tree.get_children()
                if len(item) > 1:
                    item = item[-1:]
                    self.tree.delete(item)
                    self.update_treeView(quantity, productType, amount, tag)
                else:
                    self.update_treeView(quantity, productType, amount, tag)

                self.quantity_entry.delete(0,END)
                print(productType)
            except ValueError:
                pass


    def update_treeView(self, quantity, type, amount, tag):
        self.tree.insert("", END, values=(quantity, type, amount), tags = tag)
        self.tree.insert('', END, values=("", "Total = ", self.billTotal), tags="last")
        if tag == "Orange":
            self.tree.tag_configure(tag, background = "#FF7700", foreground = "white")
        if tag == "Inwi":
            self.tree.tag_configure(tag, background = "#A63EC5", foreground = "white")
        if tag == "Jawal":
            self.tree.tag_configure(tag, background = "#4B7BE5", foreground = "white")

        self.tree.tag_configure("last", background="yellow")


    def Selected_customer(self, name):
        self.selected_customer = name
        data = self.customerDataBase.getdiscountpercent(self.selected_customer)
        INWI_DISCOUNT = data[0][0]
        JAWAL_DISCOUNT = data[0][1]
        ORANGE_DISCOUNT = data[0][2]
        self.inwi_discount_entry.delete(0, END)
        self.jawal_discount_entry.delete(0, END)
        self.orange_discount_entry.delete(0, END)
        self.inwi_discount_entry.insert(0, INWI_DISCOUNT)
        self.jawal_discount_entry.insert(0, JAWAL_DISCOUNT)
        self.orange_discount_entry.insert(0, ORANGE_DISCOUNT)
        self.credit = self.customerDataBase.getRest(name)
        self.credit_label_value["text"] = str(self.credit) +" dh"


    def update_label_value(self):
        self.total_label_value['text'] = str(self.billTotal + self.credit) +" dh"
        self.Total = self.billTotal + self.credit
        try:
            # this exception activate when o delete pay entry
            self.pay = float(self.pay_value.get())
            self.rest = self.Total - float(self.pay_value.get())
            self.rest = self.Convert(self.rest)
        except ValueError:
            self.rest = self.Total
        self.label_rest_value['text'] = self.rest

        data = self.customerDataBase.getdiscountpercent(self.selected_customer)
        self.inwi_discount.set(data[0][0])
        self.jawal_discount.set(data[0][1])
        self.orange_discount.set(data[0][2])
        self.after(100, self.update_label_value)




    def RemoveFromTreeView(self):
        item = self.tree.selection()



        # here if the item more than 2 we delete selected item and we update the last line in our tree
        if len(self.tree.get_children()) > 2:
            if len(item) >0 :
                value = self.tree.item(item)['values']
                self.billTotal -= float(value[2])
                print(value)

                self.tree.delete(item[0])
                last_child = self.tree.get_children()[-1:]
                self.tree.delete(last_child)
                self.tree.insert('', END, values=("", "Total = ", self.billTotal), tags="last")
                # return saved variable state to default because we made change on the bill that why we need to save it
                self.saved = False
            else:
                messagebox.showwarning("select Item ", "please selec the item you wanna delete")
        else:
            # this if for delete all the item in the tree if only have 2 item
            # we don't want to left last item because if we have 2 item in the tree the last one is just for total
            # than when we delete the only item have hada the total will be 0 that's why I want to free all tree from data
            items = self.tree.get_children()
            for item in items:
                self.tree.delete(item)


    def RemoveAll(self):
        if self.saved :
            children = self.tree.get_children()
            for child in children:
                self.tree.delete(child)

            self.billTotal = 0.0
            self.pay_value.set("0")
            # return saved variable state to default because we made change on the bill that why we need to save it
            self.saved = False
        else:
            result = messagebox.askyesno("save bill", "you didn't save the bill are you sure you wanna remove all")

            if result == True:
                self.saved = True
                self.RemoveAll()





    def SaveBill(self):
        if not self.saved :

            database = InvoiceDataBase()
            customerDatabase = CustomerDataBase()
            stockdatabase = StockDataBase()

            children = []
            try:
                children = self.tree.get_children()
            except TclError:
                pass
            if len(children) > 0:
                for rows in children[:-1]:
                    data = self.tree.item(rows)['values']
                    # this function insert data that we get from tree in insert it to database
                    database.insertfirstdata(self.today_date, self.selected_customer,
                                             data[0], data[1], data[2])

                    stock_Product_Quantity = int(stockdatabase.dumpProductQantity(data[1])[0][0])
                    product_quantity_ordered = int(data[0])
                    rest = stock_Product_Quantity - product_quantity_ordered
                    if rest >= 0 :
                        stockdatabase.Update(product=data[1], quantity=rest)
                        print("product amount : ", int(data[0]))
                    else:
                        print("product amount err: ", int(data[0]), " rest: ", rest)
                        messagebox.showwarning("Stock warning", "you don't have this amount of product in you stock")

                # this function insert some other data to data base thie functio after we insert all data in tree to database
                database.insertlastdata(date=self.today_date, name=self.selected_customer,
                                        stotal=self.billTotal, total=self.Total, pay=self.pay, rest=float(self.rest))
                # this function update the rest value in data base of each customer
                customerDatabase.UpdateRest(self.selected_customer, self.rest)
                self.saved = True
        else:
            messagebox.showwarning("save bill", "You already saved the bill")


    def Convert(self, num):
        value = format(num, '.2f')
        value = float(value)
        if num > -1:
            return abs(value)
        else:
            return value


    def getCurrentTime(self):
        today = dt.now()
        f1 = "%H:%M:%S"
        f2 = "%d/%m/%y"
        DATE = today.strftime(f2)+"\n"+today.strftime(f1)
        self.time_label["text"] = DATE
        self.after(100, self.getCurrentTime)
        return today.strftime(f2) +" | "+today.strftime(f1)


if __name__ == "__main__":
    Bill()

