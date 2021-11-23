import tkinter as tk
from tkinter import ttk


class Table(tk.Toplevel):
    def __init__(self, root, db):
        super().__init__(root)

        self.db = db

        self.config(bg='#000000')
        self.title('Просмотреть информацию о материалах')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

        self.init_interface()
        self.view_table()

    def init_interface(self):
        self.tree = ttk.Treeview(self, columns=('id', 'name', 'typeof', 'author', 'discipline', 'year', 'place'),
                                 height=15, show='headings')

        self.tree.column('id', width=30, anchor=tk.CENTER)
        self.tree.column('name', width=150, anchor=tk.CENTER)
        self.tree.column('typeof', width=150, anchor=tk.CENTER)
        self.tree.column('author', width=150, anchor=tk.CENTER)
        self.tree.column('discipline', width=150, anchor=tk.CENTER)
        self.tree.column('year', width=70, anchor=tk.CENTER)
        self.tree.column('place', width=150, anchor=tk.CENTER)

        self.tree.heading('id', text='id')
        self.tree.heading('name', text='name')
        self.tree.heading('typeof', text='typeof')
        self.tree.heading('author', text='author')
        self.tree.heading('discipline', text='discipline')
        self.tree.heading('year', text='year')
        self.tree.heading('place', text='place')

        self.tree.pack()

    def view_table(self):
        self.db.view_table()
        [self.tree.delete(item) for item in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    class Search(tk.Toplevel):
        def __init__(self):
            super().__init__()
            self.init_interface()

        def init_interface(self):
            w = self.root.winfo_screenwidth()
            h = self.root.winfo_screenheight()
            w //= 2
            h //= 2
            self.geometry(f"300x150+{w - 300 // 2}+{h - 150 // 2}")
            self.config(bg='#000000')
            self.title('Просмотреть информацию о материалах')
            self.resizable(False, False)

            search = tk.Label(self, text='Поиск')
            search.place(x=50, y=30)

            self.enter_search = ttk.Entry(self)
            self.enter_search.place(x=150, y=30, width=120)

            button_cancel = ttk.Button(self, text='Назад', command=self.destroy())
            button_cancel.place(x=125, y=50, width=50)

            self.grab_set()
            self.focus_set()
