import tkinter as tk
from add_window import Add
from table import Table


class Main(tk.Frame):
    def __init__(self, root, db):
        super().__init__(root)
        self.db = db
        self.root = root
        self.init_interface()

    def init_interface(self):
        self.image_add = tk.PhotoImage(file='icons/add.png')
        self.image_data = tk.PhotoImage(file='icons/data.png')
        self.image_exit = tk.PhotoImage(file='icons/exit.png')

        button_add = tk.Button(bg='#ffffff', bd=0, image=self.image_add, command=self.call_save, pady='8')
        button_check = tk.Button(bg='#ffffff', bd=0, image=self.image_data, pady='8', command=self.call_table)
        button_exit = tk.Button(bg='#ffffff', bd=0, image=self.image_exit, pady='8', command=self.exit)

        label_add = tk.Label(text='Добавить информацию', width=20, bg='#ffffff', font='ArialBlack 14')
        label_data = tk.Label(text='База данных', width=20, bg='#ffffff', font='ArialBlack 14')
        label_exit = tk.Label(text='Выйти', width=20, bg='#ffffff', font='ArialBlack 14')

        button_add.grid(row=0, column=0, sticky='W', pady=50, padx=50)
        label_add.grid(row=0, column=1, sticky='W', pady=50)

        button_check.grid(row=1, column=0, sticky='W', pady=50, padx=50)
        label_data.grid(row=1, column=1, sticky='W', pady=50)

        button_exit.grid(row=2, column=0, sticky='W', pady=50, padx=50)
        label_exit.grid(row=2, column=1, sticky='W', pady=50)

    def call_save(self):
        Add(self.root, self.db)

    def call_table(self):
        Table(self.root, self.db)

    def exit(self):
        self.root.destroy()
