'''

Authors: Farhan Ahmad, Keyi Chai, Luyi Sun, Harish Balaji, Yikun Yang

'''
from tkinter import *
import tkinter.ttk as ttk
import csv
import pandas as pd

f_name = "rockwellrealty_l.csv" #change to your specific path if doesn't work
f1 = pd.read_csv(f_name)

def extractTitle(f):
    return f.split('\\')[-1]

def displayTableR():
    root = Tk()
    title = extractTitle(f_name)
    root.title(f'{title}')
    width = 1000
    height = 500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Name", "Address", "Price"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Address', text="Address", anchor=W)
    tree.heading('Price', text="Price", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=300)
    tree.column('#2', stretch=NO, minwidth=0, width=400)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.pack()

    reader = f1
    reader1 = pd.DataFrame(reader).reset_index(drop= True)
    Name = reader1['Name']
    Address = reader1['Address']
    Price = reader1['Price']
    tree.insert("", 0, values=(Name, Address, Price))

    if __name__ == '__main__':
        root.mainloop()