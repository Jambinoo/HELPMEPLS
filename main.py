from fileinput import filename
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import random
import matplotlib.pyplot as plt
import pandas as pd
import csv


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
    file = itemIdEntry.get()
    df = pd.read_csv(f'{file}.csv')
    df.sort_values(by='last')
    x = df['iq']
    y = df['cgpa']
    plt.xlabel('IQ', fontsize=18)
    plt.ylabel('CGPA', fontsize=16)
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.show()


def exit1():
    window.destroy()


if __name__ == "__main__":
    window_width, window_height = 800, 600
    window = tk.Tk()
    window.title("Stock Management System")

    placeholderArray = ['', '', '', '', '']
    plt.style.use('bmh')
    categoryArray = ['student_clustering', 'Computer Parts', 'Repair Tools', 'Gadgets']

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    my_tree = ttk.Treeview(window, show='headings', height=20)
    style = ttk.Style()

    frame = tk.Frame(window, bg="#33f6ff")
    frame.pack()
    entriesFrame = tk.LabelFrame(frame, text="Input", borderwidth=5)

    btn_color = "#196E78"
    item_id_value = StringVar()
    manageFrame = tk.LabelFrame(frame, text="Graph", borderwidth=5)
    manageFrame.grid(row=0, column=0, sticky="w", padx=100, pady=20, ipadx=5)
    save_btn = Button(manageFrame, text="BarChart", width=10, borderwidth=3, bg=btn_color, fg='white',
                     command=lambda: show_bar())
    update_btn = Button(manageFrame, text="Line", width=10, borderwidth=3, bg=btn_color, fg='white',
                       command=lambda: line_bar())
    delete_Btn = Button(manageFrame, text="DELETE", width=10, borderwidth=3, bg=btn_color, fg='white')
    itemIdLabel = Label(entriesFrame, text="ITEM ID", anchor="e", width=10)
    itemIdEntry = ttk.Combobox(entriesFrame, width=47, textvariable=item_id_value, values=categoryArray)
    clearBtn = Button(manageFrame, text="CLEAR", width=10, borderwidth=3, bg=btn_color, fg='white',
                      command=lambda: itemIdEntry.delete(0, tk.END))
    exBtn = Button(manageFrame, text="EXIT", width=10, borderwidth=3, bg=btn_color, fg="white", command=lambda: exit1())

    save_btn.grid(row=0, column=0, padx=5, pady=5)
    update_btn.grid(row=0, column=1, padx=5, pady=5)
    delete_Btn.grid(row=0, column=2, padx=5, pady=5)
    clearBtn.grid(row=0, column=3, padx=5, pady=5)
    exBtn.grid(row=0, column=4, padx=5, pady=5)
    entriesFrame.grid(row=1, column=0, sticky="w", padx=100, pady=20, ipadx=30)
    itemIdLabel.grid(row=0, column=0, padx=10)
    itemIdEntry.grid(row=0, column=2, padx=5, pady=5)

    window.resizable(False, False)
    window.mainloop()
