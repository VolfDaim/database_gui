import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb


class Table(tk.Toplevel):
    def __init__(self, root, db):
        super().__init__(root)
        self.db = db
        self.grab_set()
        self.focus_set()

        self.init_interface()
        self.view_table()

    def init_interface(self):
        self.config(bg='#ffffff')
        self.title('Просмотреть информацию о материалах')
        self.resizable(False, False)

        self.search_dict = {
            'Наименование': 'name',
            'Вид работы': 'typeof',
            'Автор': 'author',
            'Дисциплина': 'discipline',
            'Год': 'year',
            'Место хранения': 'place'
        }

        self.combobox_search = ttk.Combobox(self, values=[
            'Наименование',
            'Вид работы',
            'Автор',
            'Дисциплина',
            'Год',
            'Место хранения'

        ])
        self.combobox_search.current(0)

        self.image_search = tk.PhotoImage(file='icons/search.png')
        self.image_back = tk.PhotoImage(file='icons/small_back.png')
        self.image_delete = tk.PhotoImage(file='icons/delete.png')
        self.image_delete_all = tk.PhotoImage(file='icons/delete_all.png')

        self.enter_search = ttk.Entry(self)
        button_search = tk.Button(self, image=self.image_search, bg='#ffffff', bd=0, command=self.view_search)
        button_cancel = tk.Button(self, image=self.image_back, bg='#ffffff', bd=0, command=self.destroy)
        button_delete_by = tk.Button(self, image=self.image_delete, bg='#ffffff', bd=0, command=self.delete_by)
        button_delete_all = tk.Button(self, image=self.image_delete_all, bg='#ffffff', bd=0, command=self.delete_all)

        label_search = tk.Label(self, text='Поиск', width=10, bg='#ffffff')
        label_cancel = tk.Label(self, text='Назад', width=10, bg='#ffffff')
        label_delete_by = tk.Label(self, text='Удалить', width=10, bg='#ffffff')
        label_delete_all = tk.Label(self, text='Очистить базу данных', width=20, bg='#ffffff')

        self.tree = ttk.Treeview(self, columns=('id', 'name', 'typeof', 'author', 'discipline', 'year', 'place'),
                                 height=20, show='headings')

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

        self.combobox_search.grid(row=0, column=0, sticky='W',padx=10)
        self.enter_search.grid(row=0, column=1, sticky='W')

        button_search.grid(row=0, column=2)
        button_cancel.grid(row=0, column=3)
        button_delete_by.grid(row=0, column=4)
        button_delete_all.grid(row=0, column=5)

        label_search.grid(row=1, column=2, sticky='W')
        label_cancel.grid(row=1, column=3, sticky='W')
        label_delete_by.grid(row=1, column=4, sticky='W')
        label_delete_all.grid(row=1, column=5, sticky='W')

        self.tree.grid(row=2, column=0, columnspan=6, padx=10)

    def view_table(self):
        self.db.view_table()
        self.show_table()

    def view_search(self):
        self.db.search_by(self.search_dict[self.combobox_search.get()], self.enter_search.get())
        fetch = self.db.c.fetchall()

        if not fetch:
            mb.showinfo('Поиск', 'Данные не найдены')
        else:
            [self.tree.delete(item) for item in self.tree.get_children()]
            [self.tree.insert('', 'end', values=row) for row in fetch]

    def delete_by(self):

        self.db.search_by(self.search_dict[self.combobox_search.get()], self.enter_search.get())
        fetch = self.db.c.fetchall()

        if not fetch:
            mb.showinfo('Удаление', 'Данные для удаления не найдены')
        else:
            answer = mb.askyesno(message='Вы уверены, что хотите удалить эти данные?')
            if answer:
                self.db.delete_by(self.search_dict[self.combobox_search.get()], self.enter_search.get())
                self.db.view_table()
                self.show_table()

    def delete_all(self):
        answer = mb.askyesno(message='Вы уверены, что хотите очистить базу данных?')

        if answer:
            self.db.delete_all()
            mb.showinfo(message='База данных очищена')
            self.show_table()

    def show_table(self):
        [self.tree.delete(item) for item in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]
