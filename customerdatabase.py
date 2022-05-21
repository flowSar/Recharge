

import sqlite3
class CustomerDataBase:

    def __init__(self):
        try:
            self.connect = sqlite3.connect("/home/exsar/PycharmProjects/python_oop_Gui/Recharge/Customers/customer.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute(""" CREATE TABLE customers(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name text,
                                    phone text,
                                    rest BLOB,
                                    inwi BLOB,
                                    jawal BLOB,
                                    orange BLOB
                                    )""")
            self.cursor.execute(f"INSERT INTO customers (name,phone,rest,inwi,jawal,orange) VALUES ( 'Customer', '0000000000','0.0','6.0','7.0','6.0')")
        except sqlite3.OperationalError:
            pass
        finally:
            self.connect.commit()
            # self.connect.close()


    def insert(self, name, phone, inwi, jawal, orange):
        self.cursor.execute(f"INSERT INTO customers (name,phone,rest,inwi,jawal,orange) VALUES ( '{name}', '{phone}','0.0','{inwi}','{jawal}','{orange}')")
        self.connect.commit()

    def insertName(self, name):
        self.cursor.execute(f"INSERT INTO customers (name) VALUES ('{name}')")
        self.connect.commit()

    def dump(self):
        data = []

        # select all data from table order by name ASC(ascending) or DESC(descending)
        self.cursor.execute("SELECT * FROM customers ORDER BY NULL")
        # you can rather than put name of the column put his number like
        # self.cursor.execute("SELECT * FROM customers ORDER BY 2")

        # WHERE to put constraint on what you will select from table
        # self.cursor.execute("SELECT * FROM customers WHERE name ='brahim'")

        # this if you want to select only one column in a table like name or phone or id
        """
        id | name   |  phone     |
        1   brahim   0668725152
        2   khalid   0668725152
        3   hassan   0668725152
        4   rachid   0668725152
        """
        # self.cursor.execute("SELECT DISTINCT name FROM customers")
        return self.cursor.fetchall()
    def close(self):
        self.connect.close()

    def dumpcolumn(self, column):

        self.cursor.execute(f"SELECT DISTINCT {column} FROM customers")
        return self.cursor.fetchall()

    def getRest(self, name):

        self.cursor.execute(f"SELECT rest FROM customers WHERE name ='{name}'")
        return float(self.cursor.fetchall()[0][0])



    def UpdateRest(self, name, rest):
        if name != "Customer":
            print("Result: ", self.cursor.execute(f"UPDATE customers SET rest = '{rest}' WHERE name = '{name}'"))
            self.connect.commit()

    def getdiscountpercent(self, name):
        self.cursor.execute(f"SELECT inwi,jawal,orange FROM customers WHERE name = '{name}'")
        return self.cursor.fetchall()

    def dumpAll(self):
        self.cursor.execute("SELECT name,phone,rest,inwi,jawal,orange from customers")
        return self.cursor.fetchall()


if __name__ == "__main__":
    pass
    data = CustomerDataBase()
    # data.UpdateRest('aziz',32.5)
    # data.insert("hassan","23456789")
    print(data.getdiscountpercent('brahim'))
    # da = data.dumpAll()
    # print(da)