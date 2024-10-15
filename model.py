import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
import csv


class StockManagementSystem:
    def __init__(self, master):
        self.master = master
        self.master.title("Stock Management System")
        self.window_width, self.window_height = 800, 600
        self.configure_window()

        self.fileArray = ['student_clustering', 'Cars', 'Repair Tools', 'Gadgets']

        self.file_value = tk.StringVar(value=self.fileArray[0])
        self.x_axis = tk.StringVar()
        self.y_axis = tk.StringVar()

        self.create_widgets()
        self.setup_layout()

    def configure_window(self):
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()
        position_top = int(screen_height / 2 - self.window_height / 2)
        position_right = int(screen_width / 2 - self.window_width / 2)
        self.master.geometry(f'{self.window_width}x{self.window_height}+{position_right}+{position_top}')
        self.master.resizable(False, False)

    def create_widgets(self):
        self.frame = tk.Frame(self.master, bg="#33f6ff")
        self.frame.pack()
        self.entries_frame = tk.LabelFrame(self.frame, text="Input", borderwidth=5)
        self.manage_frame = tk.LabelFrame(self.frame, text="Graph", borderwidth=5)

        # Buttons
        self.bar_chart_btn = tk.Button(self.manage_frame, text="BarChart", width=10, borderwidth=3,
                                       bg="#196E78", fg='white',
                                       command=self.show_bar)
        self.line_chart_btn = tk.Button(self.manage_frame, text="Line", width=10, borderwidth=3,
                                        bg="#196E78", fg='white',
                                        command=self.line_chart)
        self.clear_btn = tk.Button(self.manage_frame, text="CLEAR", width=10, borderwidth=3,
                                   bg="#196E78", fg='white',
                                   command=self.clear_selection)
        self.exit_btn = tk.Button(self.manage_frame, text="EXIT", width=10, borderwidth=3,
                                  bg="#196E78", fg="white",
                                  command=self.exit_app)

        self.item_id_label = tk.Label(self.entries_frame, text="ITEM ID", anchor="e", width=10)
        self.item_id_combobox = ttk.Combobox(self.entries_frame, width=47,
                                             textvariable=self.file_value, values=self.fileArray)
        self.x_label = tk.Label(self.entries_frame, text="X-axis", anchor="e", width=10)
        self.y_label = tk.Label(self.entries_frame, text="Y-axis", anchor="e", width=10)

        headers = self.get_headers(self.file_value.get())
        self.x_combobox = ttk.Combobox(self.entries_frame, width=47, textvariable=self.x_axis, values=headers)
        self.y_combobox = ttk.Combobox(self.entries_frame, width=47, textvariable=self.y_axis, values=headers)

        # Event binding
        self.item_id_combobox.bind('<<ComboboxSelected>>', self.update_headers)

    def setup_layout(self):
        # Layout for Graph Frame
        self.manage_frame.grid(row=0, column=0, sticky="w", padx=100, pady=20, ipadx=5)
        self.bar_chart_btn.grid(row=0, column=0, padx=5, pady=5)
        self.line_chart_btn.grid(row=0, column=1, padx=5, pady=5)
        self.clear_btn.grid(row=0, column=2, padx=5, pady=5)
        self.exit_btn.grid(row=0, column=3, padx=5, pady=5)

        # Layout for Input Frame
        self.entries_frame.grid(row=1, column=0, sticky="w", padx=100, pady=20, ipadx=30)
        self.item_id_label.grid(row=0, column=0, padx=10)
        self.item_id_combobox.grid(row=0, column=1, padx=5, pady=5)
        self.x_label.grid(row=1, column=0, padx=10)
        self.x_combobox.grid(row=1, column=1, padx=5, pady=5)
        self.y_label.grid(row=2, column=0, padx=10)
        self.y_combobox.grid(row=2, column=1, padx=5, pady=5)

    def get_headers(self, file_name):
        try:
            with open(f'{file_name}.csv', mode='r') as file:
                csv_reader = csv.reader(file)
                header = next(csv_reader)
                return header
        except FileNotFoundError:
            return []

    def update_headers(self, event):
        selected_file = self.file_value.get()
        headers = self.get_headers(selected_file)
        self.x_combobox['values'] = headers
        self.y_combobox['values'] = headers
        if headers:
            self.x_combobox.current(0)
            self.y_combobox.current(0)

    def show_bar(self):
        self.plot_graph(plot_type='bar')

    def line_chart(self):
        self.plot_graph(plot_type='line')

    def plot_graph(self, plot_type):
        file = self.file_value.get()
        x = self.x_axis.get()
        y = self.y_axis.get()
        try:
            df = pd.read_csv(f'{file}.csv')
            df = df.sort_values(by=x, ascending=False)
            plt.xlabel(x.upper(), fontsize=18)
            plt.ylabel(y.upper(), fontsize=16)

            if plot_type == 'bar':
                plt.bar(df[x], df[y])
            elif plot_type == 'line':
                plt.plot(df[x], df[y], marker='o')
                plt.scatter(df[x], df[y])

            plt.style.use('bmh')
            plt.show()
        except FileNotFoundError:
            messagebox.showerror("File Error", "CSV file not found.")
        except KeyError:
            messagebox.showerror("Column Error", "Selected columns not found in the file.")

    def clear_selection(self):
        self.item_id_combobox.set('')
        self.x_combobox.set('')
        self.y_combobox.set('')

    def exit_app(self):
        self.master.destroy()

