import tkinter as tk
from tkinter import messagebox as mb


class Add(tk.Toplevel):
    def __init__(self, root, db):
        super().__init__(root)
        self.db = db
        self.root = root
        self.init_interface()

    def init_interface(self):
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        w //= 2
        h //= 2
        self.geometry(f"550x650+{w - 550 // 2}+{h - 650 // 2}")
        self.config(bg='#ffffff')
        self.title('Добавить информацию о материале')
        self.resizable(False, False)

        self.name = self.create_entry()
        self.typeof = self.create_entry()
        self.author = self.create_entry()
        self.discipline = self.create_entry()
        self.year = self.create_entry()
        self.places = self.create_entry()

        name_hint = self.create_label('Наименование')
        typeof_hint = self.create_label('Вид работы')
        author_hint = self.create_label('Автор')
        discipline_hint = self.create_label('Дисциплина')
        year_hint = self.create_label('Год')
        place_hint = self.create_label('Место хранения')

        self.image_save = tk.PhotoImage(file='icons/save.png')
        self.image_back = tk.PhotoImage(file='icons/back.png')
        self.button_save = tk.Button(self, image=self.image_save, bg='#ffffff', bd=0)

        self.button_save.bind('<Button-1>', lambda add: self.insert_table(self.name.get(),
                                                                          self.typeof.get(),
                                                                          self.author.get(),
                                                                          self.discipline.get(),
                                                                          self.year.get(),
                                                                          self.places.get()))

        self.button_back = tk.Button(self, image=self.image_back, text='Назад', bg='#ffffff', bd=0,
                                     command=self.close)

        self.name.grid(row=0, column=0, sticky='W', pady=10, padx=20)
        self.typeof.grid(row=1, column=0, sticky='W', pady=10, padx=20)
        self.author.grid(row=2, column=0, sticky='W', pady=10, padx=20)
        self.discipline.grid(row=3, column=0, sticky='W', pady=10, padx=20)
        self.year.grid(row=4, column=0, sticky='W', pady=10, padx=20)
        self.places.grid(row=5, column=0, sticky='W', pady=10, padx=20)

        name_hint.grid(row=0, column=1)
        typeof_hint.grid(row=1, column=1)
        author_hint.grid(row=2, column=1)
        discipline_hint.grid(row=3, column=1)
        year_hint.grid(row=4, column=1)
        place_hint.grid(row=5, column=1)

        self.button_back.grid(row=7, column=1, sticky='W', pady=200, padx=50)
        self.button_save.grid(row=7, column=0, sticky='W', pady=200, padx=100)

        self.grab_set()
        self.focus_set()

    def insert_table(self, *args):
        for item in args:
            if not item:
                mb.showinfo(message='Вы не заполнили все поля')
                break
        else:
            self.db.insert(*args)
            self.db.view_table()
            self.destroy()

    def create_entry(self):
        return tk.Entry(self, width=30, bg='#F4EA7C')

    def create_label(self, text):
        return tk.Label(self, text=text, width=30, bg='#BFE5E8')

    def close(self):
        self.destroy()
