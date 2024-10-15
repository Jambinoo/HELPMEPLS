from fileinput import filename
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
import random
import matplotlib.pyplot as plt
import pandas as pd
import csv

CGPA = 0
IQ = 1

def readCSV(filename):
    infile = open(filename, 'r')
    mylist = []
    csv_obj = csv.reader(infile)
    for row in csv_obj:
        mylist.append(row)
    infile.close()
    return mylist

def readRecordToList(filename):
    infile = open(filename, 'r')
    mylist = []
    heading = next(infile)
    csv_obj = csv.reader(infile)
    for row in csv_obj:
        mylist.append(row)
    infile.close()
    return mylist

def typeConvert(mylist):
    newList = []
    for i in range(len(mylist)):
        tmpcgpa = mylist[i][CGPA].strip()
        tmpiq = mylist[i][IQ].strip()
        newList.append([tmpcgpa ,tmpiq])
    return newList

def merge(A, p, q, r):
    if type(A) is list:
        left = A[p: q+1]
        right = A[q+1: r+1]
    else:
        left = list(A[p: q+1])
        right = list(A[q+1: r+1])

    i = 0
    j = 0
    k = p

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        k += 1

    if i < len(left):
        A[k: r+1] = left[i:]
    if j < len(right):
        A[k: r+1] = right[j:]

def merge_sort(A, p=0, r=None):
    if r is None:
        r = len(A)-1
    if p>=r:
        return
    q = (p+r)//2
    merge_sort(A,p,q)
    merge_sort(A, q+1, r)
    merge(A,p,q,r)


window_width, window_height = 800, 600
window=tkinter.Tk()
window.title("Stock Management System")

placeholderArray=['','','','','']
plt.style.use('bmh')
categoryArray=['student_clustering','Computer Parts','Repair Tools','Gadgets']

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

my_tree=ttk.Treeview(window,show='headings',height=20)
style=ttk.Style()


frame=tkinter.Frame(window,bg="#33f6ff")
frame.pack()

btnColor="#196E78"

manageFrame=tkinter.LabelFrame(frame,text="Graph",borderwidth=5)
manageFrame.grid(row=0,column=0,sticky="w",padx=[100],pady=20,ipadx=[5])

saveBtn=Button(manageFrame,text="BarChart",width=10,borderwidth=3,bg=btnColor,fg='white',command = lambda : show_bar())
updateBtn=Button(manageFrame,text="Line",width=10,borderwidth=3,bg=btnColor,fg='white',command = lambda : line_bar())
deleteBtn=Button(manageFrame,text="DELETE",width=10,borderwidth=3,bg=btnColor,fg='white')
clearBtn=Button(manageFrame,text="CLEAR",width=10,borderwidth=3,bg=btnColor,fg='white',command = lambda : clear())
exBtn = Button(manageFrame,text="EXIT",width=10,borderwidth=3,bg=btnColor,fg="white",command = lambda : exit1())

saveBtn.grid(row=0,column=0,padx=5,pady=5)
updateBtn.grid(row=0,column=1,padx=5,pady=5)
deleteBtn.grid(row=0,column=2,padx=5,pady=5)
clearBtn.grid(row=0,column=3,padx=5,pady=5)
exBtn.grid(row=0,column=4,padx=5,pady=5)


entriesFrame=tkinter.LabelFrame(frame,text="Input",borderwidth=5)
entriesFrame.grid(row=1,column=0,sticky="w",padx=[100],pady=[0,20],ipadx=[30])

itemIdLabel=Label(entriesFrame,text="ITEM ID",anchor="e",width=10)


itemIdLabel.grid(row=0,column=0,padx=10)


itemIdvalue = StringVar()

itemIdEntry=ttk.Combobox(entriesFrame,width=47,textvariable=placeholderArray[4],values=categoryArray)


itemIdEntry.grid(row=0,column=2,padx=5,pady=5)

def show_bar():
    file = itemIdEntry.get()
    df = pd.read_csv(f'{file}.csv')
    x = df['iq']
    y = df['cgpa']
    plt.xlabel('IQ', fontsize=18)
    plt.ylabel('CGPA', fontsize=16)
    plt.bar(x, y)
    plt.show()


def line_bar():
    file_name = "student_clustering.csv"
    my_list = readRecordToList(file_name)
    converted_list = typeConvert(my_list)
    merge_sort(converted_list)
    for row in converted_list:
        print(row)
    file = itemIdEntry.get()
    df = pd.read_csv(f'{file}.csv')
    x = df['iq']
    y = df['cgpa']
    plt.xlabel('IQ', fontsize=18)
    plt.ylabel('CGPA', fontsize=16)
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.show()

def clear():
    itemIdvalue.set('')

def exit1():
    window.destroy()

window.resizable(False,False)
window.mainloop()