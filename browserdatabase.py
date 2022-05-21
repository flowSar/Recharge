
from invoicedatabase import InvoiceDataBase
from tkinter import *
from tkcalendar import  DateEntry
from datetime import date, datetime
from tkinter import ttk
from customerdatabase import CustomerDataBase




class BrowserDataBase (ttk.Frame):

    def __init__(self):
        super().__init__()

        self.grid(row = 0, column = 0, sticky = "news")



        self.database = CustomerDataBase()
        self.invoicedataBase = InvoiceDataBase()

        self.selected = StringVar()
        self.selected.set("All")

        self.frame = ttk.Frame(self)
        self.frame.grid(row = 0, column = 0, pady = (20,20))
        self.old_data = ["All"]
        self.InsertDataToOptionMenu(self.frame)

        # self.cal = DateEntry(self.frame, width=12, background='darkblue',
        #                      foreground='white', borderwidth=2,
        #                      date_pattern='dd/mm/y')
        # self.cal.configure(background="red")
        # self.cal.bind("<<DateEntrySelected>>", self.selectedDate)
        # self.cal.grid(row=0, column=1)



        self.tree = self.CreateTreeView()

        sco = ttk.Scrollbar(self, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=sco.set)
        sco.grid(row = 1, column = 1, sticky=(W,N,S))
        # self.mainloop()


    def InsertDataToOptionMenu(self, frame):
        users = ["All"]
        for name in self.database.dumpcolumn("name"):
            users += name
        if len(self.old_data)< len(users) or len(self.old_data)> len(users):
            self.old_data = users
            self.CreateOptionMenu(users, frame)


        self.after(100, self.InsertDataToOptionMenu,self.frame)

    def CreateOptionMenu(self, users, frame):
        option = OptionMenu(frame, self.selected, *users, command=self.Selectes_item)
        option.configure(background = "#DDDDDD", foreground = "white")
        option.configure(width=15)
        option.grid(row=0, column=0, padx=(0, 10))
        option["menu"].configure(background = "white", foreground = "black")
        return option


    def CreateTreeView(self):
        columns = ["date", "name", "number", "type", "total", "sum", "pay", "rest"]
        tree = ttk.Treeview(self, columns=columns, show="headings")
        tree.configure(height = 20)
        tree.heading("date", text="Date", anchor = "center")
        tree.heading("name", text="Name")
        tree.heading("number", text="Number")
        tree.heading("type", text="Type")
        tree.heading("total", text="Total")
        tree.heading("sum", text="Sum")
        tree.heading("pay", text="Pay")
        tree.heading("rest", text="Rest")
        tree.column("name", width = 180, anchor = "center")
        tree.column("date", width = 140, anchor = "center")
        tree.column("number", width = 140, anchor = "center")
        tree.column("type", width = 100, anchor = "center")
        tree.column("total", width = 140, anchor = "center")
        tree.column("sum", width = 140, anchor = "center")
        tree.column("pay", width = 140, anchor = "center")
        tree.column("rest", width = 120, anchor = "center")
        tree.grid(row = 1, column = 00)

        return tree

    def Selectes_item(self, name):
        self.selected.set(name)
        print(name)
        # this functio if you want select from database with date
        # self.insertDataToTreeView(name = name, date = self.cal.get())
        self.insertDataToTreeView(name = name )



    def insertDataToTreeView(self, name, date = None):
        data = self.invoicedataBase.getAllData(name = name, date = date)
        print(data)
        for row in self.tree.get_children():
            self.tree.delete(row)
        for d in data:
            tag = 'f'
            if d[2] == None:
                """ here I check if the Number is None that mean we are at last row in database
                    we change the tag of row to "l" that's help us change the bg color of the last row
                    that's changing of bg color it's just for distinguish the row when we stored the data when customer pay
                """
                tag = 'l'
            self.tree.insert("", END, value = (d[0], d[1],
                                               self.check(d[2]),
                                               self.check(d[3]),
                                               self.check(d[4]),
                                               self.check(d[5]),
                                               self.check(d[6]),
                                               self.check(d[7])),
                                      tags = tag)

            self.tree.tag_configure('f', background = "orange")
            self.tree.tag_configure('l', background="red", foreground = "white")

    def check(self, v:str) -> str:
        if v == None:
            return "-------"
        else:
            return v

    def selectedDate(self, e):
        # selected_date = self.cal.get()
        # print(self.invoicedataBase.getAllData("All", date = selected_date))
        self.insertDataToTreeView(name = self.selected.get())
        #print("selected name : ", self.selected.get(), " date : ", selected_date)
        # pass

if __name__ == "__main__":
    pass
    # browser = BrowserDataBase()
    # b = InvoiceDataBase()
    # data = b.getAllData(name = "yassine")
    # #
    # for d in data:
    #     print(d)

