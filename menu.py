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
        button_add = tk.Button(text="Добавить информацию о материале", bg='#ffff33', width=40, command=self.call_save,
                               pady='8').pack()
        button_check = tk.Button(text="Просмотреть информацию", bg='#ffff33', width=40, pady='8',
                                 command=self.call_table).pack()

        button_exit = tk.Button(text="Выход", bg='#ffff33', width=40, pady='8', command=self.exit).pack()

    def call_save(self):
        Add(self.root, self.db)

    def call_table(self):
        Table(self.root, self.db)

    def exit(self):
        self.root.destroy()
