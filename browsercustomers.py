
from customerdatabase import CustomerDataBase
from tkinter import *
from tkinter import ttk

from tkinter import messagebox
class BrowserCustomers (ttk.Frame):

    def __init__(self):
        super().__init__()

        self.grid(row = 0, column = 0, sticky = "news")

        self.database = CustomerDataBase()

        columns = ["name", "phone", "rest", "inwi", "jawal", "orange"]
        self.tree = ttk.Treeview(self, columns = columns, show = "headings", selectmode = 'browse')
        self.tree.heading("name", text = "Name")
        self.tree.heading("phone", text="Phone")
        self.tree.heading("rest", text="Rest")
        self.tree.heading("inwi", text="Inwi %")
        self.tree.heading("jawal", text="Jawal %")
        self.tree.heading("orange", text="Orange %")

        self.tree.column(0, anchor = "center")
        self.tree.column(1, anchor = "center")
        self.tree.column(2, anchor = "center")
        self.tree.column(3, anchor = "center")
        self.tree.column(4, anchor = "center", width = 140)
        self.tree.column(5, anchor = "center", width = 140)
        self.tree.grid(row =1, column = 0)

        self.old_data = []
        self.checkDataBaseChange_and_updateTreeView()


        frame = ttk.Frame(self)
        frame.grid(row = 0, column = 0)
        btn = Button(frame, text = "Edit Customer Data", command = self.btn_click)
        btn.configure(background = "orange", foreground = "white", font  = ("bold", 15, "italic"))
        btn.grid(row = 0, column = 0, pady = (20,20), padx = (5,5))

        btn_remove = Button(frame, text = "Remove Customer", command = self.remove_customer)
        btn_remove.configure(background = "orange", foreground = "white", font  = ("bold", 15, "italic"))
        btn_remove.grid(row = 0, column = 1, pady = (5,5), padx = (5,5))



    def checkDataBaseChange_and_updateTreeView(self):
        customerdata = self.database.dumpAll()
        if len(self.old_data)<len(customerdata) or len(self.old_data)>len(customerdata):
            self.old_data = customerdata
            for item in self.tree.get_children():
                self.tree.delete(item)
            for data in customerdata:
                self.tree.insert("", END, value=(data[0], data[1], data[2], data[3], data[4], data[5]))

        self.after(100, self.checkDataBaseChange_and_updateTreeView)


    def test(self):
        print("sar")
    def btn_click(self):

        item = self.tree.selection()
        if len(item)>0:
            EditeCustomerInfo(self.tree.item(item)['values'])
        else:
            messagebox.showwarning("Edite", " Plase Select the Customer You wanna Edite")


    def remove_customer(self):
        item = self.tree.selection()
        if len(item)>0:
            name  = self.tree.item(item)['values'][0]
            msg = messagebox.askokcancel("Delete Customer", f"Are you sure you wanna Delete this Customer {name}")

            if msg:
                self.database.cursor.execute(f"DELETE from customers WHERE name = '{name}'")
                self.tree.delete(item)
                self.database.connect.commit()
                pass
        else:
            messagebox.showwarning("Select"," Plase Select the Customer You wanna delete")

class Error (TclError):

    def __init__(self, name):
        super().__init__()
        self.msg = messagebox.askokcancel(f"Delete Customer", "Are you sure you wanna Delete this Customer {name}")

    def getValue(self):
        return self.msg



class EditeCustomerInfo (Toplevel):

    def __init__(self, data):
        super().__init__()
        self.title("---Edite---")


        self.data = data
        self.database = CustomerDataBase()

        frame = ttk.Frame(self, padding = "10 10 10 10")
        frame.grid(row = 0, column = 0)

        User_name_label = ttk.Label(frame, text = "User Name:", font = ('bold',12,"italic"))
        User_name_label.grid(row = 0, column = 0, pady = (5, 5))

        self.user_name_value = StringVar()
        User_name_entry = ttk.Entry(frame, textvariable = self.user_name_value)
        User_name_entry.grid(row = 0, column = 1, padx = (5, 5))


        phone_label = ttk.Label(frame, text = "Phone:", font = ('bold',12,"italic"))
        phone_label.grid(row = 1, column = 0, pady = (5,5))

        self.phone_value = StringVar()
        phone_entry = ttk.Entry(frame, textvariable = self.phone_value)
        phone_entry.grid(row = 1, column = 1)

        inwi_name_label = ttk.Label(frame, text = "Inwi %:", font = ('bold',12,"italic"))
        inwi_name_label.grid(row = 2, column = 0, pady = (5,5))

        self.inwi_value = StringVar()
        inwi_name_entry =ttk.Entry(frame, textvariable = self.inwi_value )
        inwi_name_entry.grid(row = 2, column = 1)

        jawal_label = ttk.Label(frame, text = "Jawal %:", font = ('bold',12,"italic"))
        jawal_label.grid(row = 3, column = 0, pady = (5,5))

        self.jawal_value = StringVar()
        jawal_entry = ttk.Entry(frame, textvariable = self.jawal_value)
        jawal_entry.grid(row = 3, column = 1)

        orange_label = ttk.Label(frame, text = "Orange %:", font = ('bold',12,"italic"))
        orange_label.grid(row = 4, column = 0, pady = (5,5))

        self.orange_value = StringVar()
        orange_entry = ttk.Entry(frame, textvariable = self.orange_value)
        orange_entry.grid(row = 4, column = 1)

        btn_update = ttk.Button(frame, text = "Update", command  = self.Updatedata)
        btn_update.grid(row = 5, column = 0, pady = (5,5), columnspan = 2)



        self.setDataIntoEntry()

        self.old_name = str(self.data[0])
        self.mainloop()



    def setDataIntoEntry(self):
        self.user_name_value.set(str(self.data[0]))
        self.phone_value.set(str(self.data[1]))
        self.inwi_value.set(str(self.data[3]))
        self.jawal_value.set(str(self.data[4]))
        self.orange_value.set(str(self.data[5]))


    def Updatedata(self):
        _user_name = self.user_name_value.get()
        _phone = self.phone_value.get()
        _inwi = self.inwi_value.get()
        _jawal = self.jawal_value.get()
        _orange= self.orange_value.get()
        self.database.cursor.execute(f"UPDATE customers SET name = '{_user_name}', phone = '{_phone}', inwi = '{_inwi}', jawal = '{_jawal}', orange = '{_orange}' WHERE name = '{self.old_name}'")
        self.database.connect.commit()


if __name__ == "__main__":
    BrowserCustomers()



