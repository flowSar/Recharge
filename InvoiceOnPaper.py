
from tkinter import *
from tkinter import ttk
import os
import tempfile
import subprocess as sp


class Invoice (Toplevel):

    def __init__(self, data = None, customerName = "Anonymos", date=None, invoice_total=0.0, restb = 0.0, restafter = 0.0, total=0.0, pay=0.0):
        super().__init__()
        self.title("Print Bill")
        self.data = data
        self.date = date
        self.customerName = customerName
        self.invoice_total = invoice_total
        self.restb = restb
        self.restafter = restafter
        self.summe = total
        self.pay = pay
        print(self.data)
        labelFrame = LabelFrame(self, text = "Bill")
        labelFrame.pack()
        self.text = Text(labelFrame)
        self.text.delete("1.0", END)
        self.text.insert(END, f" Date: {self.date}")
        self.text.insert(END, f"\n Customer Name: {self.customerName}")
        self.text.insert(END, f"\n Credit: {self.restb} dh ")
        self.text.insert(END, "\n ==================================================================")
        self.text.insert(END, "\n Quantity\t\t\t type\t\t\t total")
        self.text.insert(END, "\n ==================================================================")

        for row in self.data:
            if row[0]<10:
                self.text.insert(END, f"\n  0{row[0]}\t\t\t  {row[1]} \t\t\t {row[2]}")
            else:
                self.text.insert(END, f"\n  {row[0]}\t\t\t  {row[1]} \t\t\t {row[2]}")

        self.text.insert(END, "\n ==================================================================")
        self.text.insert(END, f"\n\t\t\t\t\t\t total: {self.invoice_total} dh")

        self.text.insert(END, f"\n\t\t\t\t\t\t Summe: {self.summe} dh")
        self.text.insert(END, f"\n\t\t\t\t\t\t Pay: {self.pay} dh")
        self.text.insert(END, f"\n\t\t\t\t\t\t rest:{self.restafter} dh")
        self.text['state'] = "disabled"

        self.text.pack(fill = "both")
        btn_print = Button(self, text = "Print", command = self.PrintBill)
        btn_print.pack(pady = (10,0))

        self.mainloop()


    def PrintBill(self):

        with open("bill.txt", "w") as file:
            file.write(self.text.get("1.0", END))
        file_name = "bill.txt"
        ex_programme = "xed"

        sp.Popen([ex_programme, file_name])


if __name__ == "__main__":
    Invoice()