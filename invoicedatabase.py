

import sqlite3

class InvoiceDataBase:

    def __init__(self, databasename=None):

        # self.connect  = sqlite3.connect(f"/home/exsar/PycharmProjects/python_oop_Gui/Recharge/databaseinvoice/{databasename}.db")
        self.connect  = sqlite3.connect(f"/home/exsar/PycharmProjects/python_oop_Gui/Recharge/databaseinvoice/invoices.db")
        self.cursor = self.connect.cursor()
        try:
            self.cursor.execute("""CREATE TABLE invoice (
                                date text,
                                name text,
                                number text,
                                type text,
                                stotal text,
                                total BLOB,
                                pay BLOB,
                                rest BLOB
                            )""")
        except sqlite3.OperationalError:
            pass

        # self.connect.commit()


    def insertfirstdata(self, date, name, number, type, stotal):
        self.cursor.execute(f"INSERT INTO invoice(date,name,number,type,stotal) VALUES ('{date}','{name}','{number}','{type}','{stotal}')")
        self.connect.commit()

    def insertlastdata(self, date, name, stotal, total, pay, rest):
        self.cursor.execute(f"INSERT INTO invoice(date,name,stotal, total,pay,rest) VALUES ('{date}','{name}','{stotal}', '{total}','{pay}','{rest}')")
        self.connect.commit()


    def getAllData(self, name=None, date = None):
        if name != "All" and date == None:
            self.cursor.execute(f"SELECT * FROM invoice WHERE name = '{name}'")
            return self.cursor.fetchall()
        elif name == "All" and date == None:
            self.cursor.execute("SELECT * FROM invoice")
            return self.cursor.fetchall()
        elif name == "All" and date != None:
            self.cursor.execute(f"SELECT * FROM invoice WHERE date LIKE '{date}%'")
            return self.cursor.fetchall()
        elif date != None and name != None:
            self.cursor.execute(f"SELECT * FROM invoice WHERE name = '{name}' AND date LIKE '{date}%'")
            return self.cursor.fetchall()


    def Cf(self, v):
        value = format(v, '.2f')
        return value







