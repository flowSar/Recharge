
from tkinter import *
from tkinter import ttk
import sqlite3

PRODUCT = ["Jawal 05", "Jawal 10", "Jawal 20", "Jawal 50", "Jawal 100", "Jawal 500", "Jawal 1000",
         "Inwi 05", "Inwi 10", "Inwi 20", "Inwi 50", "Inwi 100", "Inwi 500", "Inwi 1000", "Inwi 5000", "Inwi 10000"
         "Orange 05", "Orange 10", "Orange 20", "Orange 30", "Orange 50", "Orange 100", "Orange 500",
         "Orange 1000"]

class StockDataBase:

    def __init__(self):
        self.connect = sqlite3.connect("/home/exsar/PycharmProjects/python_oop_Gui/Recharge/Stock/stock.db")
        self.cursor = self.connect.cursor()
        try:
            self.cursor.execute(""" CREATE TABLE stock (
                                    id integer PRIMARY KEY AUTOINCREMENT,
                                    product TEXT,
                                    Quantity INTEGER
                                    )""")
            for item in PRODUCT:
                self.cursor.execute(f"INSERT INTO stock (product, Quantity) VALUES ('{item}', '0' )")
            self.connect.commit()
        except sqlite3.OperationalError:
            pass


    def DumpRow(self, product):
        self.cursor.execute(f"SELECT * FROM stock WHERE product = '{product}'")
        return self.cursor.fetchall()



    def DumpAll(self):
        self.cursor.execute("SELECT * FROM stock")
        return self.cursor.fetchall()


    def Update(self, product, quantity):
        self.cursor.execute(f"UPDATE stock SET Quantity = '{quantity}' WHERE product = '{product}'")
        self.connect.commit()

    def dumpProductQantity(self, product):
        self.cursor.execute(f"SELECT Quantity FROM stock WHERE product = '{product}'")
        return self.cursor.fetchall()

class Stock (ttk.Frame):

    def __init__(self):
        super().__init__()
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(1, weight = 1)
        self.database = StockDataBase()


        frame = ttk.Frame(self, )
        frame.grid(row = 0, column = 0)
        edit_btn = ttk.Button(frame, text = "Edite", command = self.Edite_stock)
        edit_btn.grid(row = 0, column = 0, pady = (40, 20))

        reload_btn = ttk.Button(frame, text = "Reload", command = self.reload)
        reload_btn.grid(row = 0, column = 1, padx = (10, 0), pady = (40, 20))

        self.tree = self.Create_TreeView()
        # self.mainloop()

    def reload(self):
        self.listingTodataChange(self.tree)

    def listingTodataChange(self, tree):
        data = self.database.DumpAll()

        children = tree.get_children()
        for child in children:
            self.tree.delete(child)

        tag = ""
        for d in data :
            if d[1][0:1] == "J":
                tag = "J"
                tree.tag_configure(tag, background = "#4D77FF", foreground = "white")
            if d[1][0:1] == "I":
                tag = "I"
                tree.tag_configure(tag, background = "#9145B6", foreground = "white")

            if d[1][0:1] == "O":
                tag = "O"
                tree.tag_configure(tag, background = "#FF5F00", foreground = "white")
            tree.insert("",END, value = (d[1], d[2]), tags = tag)



    def Create_TreeView(self):

        columns = ["Product", "Quantity"]
        tree = ttk.Treeview(self, column=columns, show = "headings")
        tree.heading("Product", text = "Product", anchor = "center")
        tree.heading("Quantity", text = "Quantity", anchor = "center")
        tree.column(0, anchor = "center")
        tree.column(1, anchor = "center")
        tree.grid(row = 1, column = 0, columnspan = 2, sticky = (W,E,N,S))

        self.listingTodataChange(tree)


        sc = ttk.Scrollbar(self, orient = "vertical")
        tree.configure(yscrollcommand = sc.set)
        sc.config(command = tree.yview)
        sc.grid(row = 1, column = 2, sticky = (N,S))


        return tree

    # this function if for edite stock for each producte in my dataBase
    def Edite_stock(self):

        item = self.tree.selection()
        values = []
        if len(item) > 0 :
            values  = self.tree.item(item[0])['values']
            editWindow = EditeWindow(values[0], int(values[1]))





class EditeWindow (Toplevel) :

    def __init__(self, pType, pQuantity):
        super().__init__()

        self.database = StockDataBase()
        self.product = pType

        frame = ttk.Frame(self)
        frame.grid(row = 0, column = 0)

        label_product = ttk.Label(frame, text = "Producte: ")
        label_product.grid(row = 0, column = 0, pady = (10, 0), padx = (10, 5))


        label_product_type = ttk.Label(frame, text = pType)
        label_product_type.grid(row = 0, column = 1)

        label_quantity = ttk.Label(frame, text = "Quantity: ")
        label_quantity.grid(row = 1, column = 0, padx = (10, 5), pady = (5,5))

        self.quantity = StringVar()
        entry_quantity = ttk.Entry(frame, textvariable = self.quantity)
        entry_quantity.grid(row = 1, column = 1)
        entry_quantity.insert(END, pQuantity)


        btn_update = ttk.Button(frame, text = "Update", command = self.UpdateQuantity)
        btn_update.grid(row = 2, column = 0, columnspan = 2, pady = (10, 10))

        self.mainloop()


    def UpdateQuantity(self):
        try:
            quan = int(self.quantity.get())
            self.database.Update(product=self.product, quantity=quan)
            self.destroy()
        except ValueError:
            raise ValueError("You need to inter only digits")






if __name__ == "__main__":
    s  = Stock()
    # database = StockDataBase()
    # data = database.dumpProductQantity('Jawal 10')
    # print(data)
    # print("afetr update")
    # database.Update('Jawal 10', 40)
    # data = database.DumpRow('Jawal 10')
    # print(data)

