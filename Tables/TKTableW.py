'''

Authors: Farhan Ahmad, Keyi Chai, Luyi Sun, Harish Balaji, Yikun Yang

'''
from tkinter import *
import tkinter.ttk as ttk
import csv
import pandas as pd

f_name = "walnutcapital_live.csv" #change to your specific path if doesn't work
f1 = pd.read_csv(f_name)

def extractTitle(f):
    return f.split('\\')[-1]

def displayTableW():
    root = Tk()
    title = extractTitle(f_name)
    print(title)
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
    tree = ttk.Treeview(TableMargin, columns=("Name", "Address", "Rent", "Bedroom", "Bathroom", "Property Features"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Address', text="Address", anchor=W)
    tree.heading('Rent', text="Rent", anchor=W)
    tree.heading('Bedroom', text="Bedroom", anchor=W)
    tree.heading('Bathroom', text="Bathroom", anchor=W)
    tree.heading('Property Features', text="Property Features", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=400)
    tree.column('#2', stretch=NO, minwidth=0, width=400)
    tree.column('#3', stretch=NO, minwidth=0, width=400)
    tree.column('#4', stretch=NO, minwidth=0, width=400)
    tree.column('#5', stretch=NO, minwidth=0, width=400)
    tree.column('#6', stretch=NO, minwidth=0, width=400)
    tree.pack()

    reader = f1
    reader1 = pd.DataFrame(reader).reset_index(drop= True)
    Name = reader1['Name']
    Address = reader1['Address']
    Rent = reader1['Rent']
    Bedroom = reader1['Bedroom']
    Bathroom = reader1['Bathroom']
    PropertyFeatures = reader1['Property Features']
    tree.insert("", 0, values=(Name, Address, Rent, Bedroom, Bathroom, PropertyFeatures))

    if __name__ == '__main__':
        root.mainloop()