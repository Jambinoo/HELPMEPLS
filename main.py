from fileinput import filename
from tkinter import *
from tkinter import ttk, filedialog
from tkinter import messagebox
import tkinter as tk
import random
import matplotlib.pyplot as plt
import pandas as pd
import csv


def show_bar(var1, var2):

    file = item_id_combobox.get()
    df = pd.read_csv(f'{file}.csv')
    x = str(var1)
    y = str(var2)
    plt.xlabel(x.upper(), fontsize=18)
    plt.ylabel(y.upper(), fontsize=16)
    plt.bar(df[x], df[y])
    plt.show()


def line_bar(var1, var2):
    file = item_id_combobox.get()
    df = pd.read_csv(f'{file}.csv')
    d = df.sort_values(by=str(var1), ascending=False)
    x = str(var1)
    y = str(var2)
    plt.xlabel(x.upper(), fontsize=18)
    plt.ylabel(y.upper(), fontsize=16)
    plt.scatter(d[x], d[y])
    plt.plot(d[x], d[y])
    plt.show()


def update_header(event):
    selected_file = file_value.get()
    headers = get_header(selected_file)
    x_combobox['value'] = headers
    y_combobox['value'] = headers
    if headers:
        x_combobox.current(0)
        y_combobox.current(0)


def get_header(file_name: str):
    with open(file_name + ".csv", mode='r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        return header


def exit1():
    window.destroy()


if __name__ == "__main__":
    window_width, window_height = 800, 600
    window = tk.Tk()
    window.title("Stock Management System")

    placeholderArray = ['', '', '', '', '']
    plt.style.use('bmh')
    fileArray = ['student_clustering', 'Cars', 'Repair Tools', 'Gadgets']

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
    file_value = StringVar(value=fileArray[0])
    x_axis = StringVar()
    y_axis = StringVar()

    manageFrame = tk.LabelFrame(frame, text="Graph", borderwidth=5)
    manageFrame.grid(row=0, column=0, sticky="w", padx=100, pady=20, ipadx=5)
    save_btn = Button(manageFrame, text="BarChart", width=10, borderwidth=3, bg=btn_color, fg='white',
                      command=lambda: show_bar(x_axis.get(),y_axis.get()))
    update_btn = Button(manageFrame, text="Line", width=10, borderwidth=3, bg=btn_color, fg='white',
                        command=lambda: line_bar(x_axis.get(),y_axis.get()))
    delete_btn = Button(manageFrame, text="DELETE", width=10, borderwidth=3, bg=btn_color, fg='white')
    itemIdLabel = Label(entriesFrame, text="ITEM ID", anchor="e", width=10)
    item_id_combobox = ttk.Combobox(entriesFrame, width=47, textvariable=file_value, values=fileArray)

    x_label = Label(entriesFrame, text="X-axis", anchor="e", width=10)
    y_label = Label(entriesFrame, text="Y-axis", anchor="e", width=10)
    headerArray = get_header(file_value.get())
    x_combobox = ttk.Combobox(entriesFrame, width=47, textvariable=x_axis, values=headerArray)
    y_combobox = ttk.Combobox(entriesFrame, width=47, textvariable=y_axis, values=headerArray)
    clearBtn = Button(manageFrame, text="CLEAR", width=10, borderwidth=3, bg=btn_color, fg='white',
                      command=lambda: item_id_combobox.delete(0, tk.END))
    exit_btn = Button(manageFrame, text="EXIT", width=10, borderwidth=3, bg=btn_color, fg="white",
                      command=lambda: exit1())

    item_id_combobox.bind('<<ComboboxSelected>>', update_header)

    save_btn.grid(row=0, column=0, padx=5, pady=5)
    update_btn.grid(row=0, column=1, padx=5, pady=5)
    delete_btn.grid(row=0, column=2, padx=5, pady=5)
    clearBtn.grid(row=0, column=3, padx=5, pady=5)
    exit_btn.grid(row=0, column=4, padx=5, pady=5)
    entriesFrame.grid(row=1, column=0, sticky="w", padx=100, pady=20, ipadx=30)
    itemIdLabel.grid(row=0, column=0, padx=10)
    item_id_combobox.grid(row=0, column=2, padx=5, pady=5)
    x_label.grid(row=1, column=0, padx=10)
    y_label.grid(row=2, column=0, padx=10)
    x_combobox.grid(row=1, column=2, padx=5, pady=5)
    y_combobox.grid(row=2, column=2, padx=5, pady=5)
    window.resizable(False, False)
    window.mainloop()
