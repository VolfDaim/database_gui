import tkinter as tk


class Add(tk.Toplevel):
    def __init__(self, root, db):
        super().__init__(root)
        self.db = db
        self.root=root
        self.init_interface()

    def init_interface(self):
        w = self.root.winfo_screenwidth()
        h = self.root.winfo_screenheight()
        w //= 2
        h //= 2
        self.geometry(f"550x650+{w - 550 // 2}+{h - 650 // 2}")
        self.config(bg='#000000')
        self.title('Добавить информацию о материале')
        self.resizable(False, False)

        self.name = tk.Entry(self, width=30)
        self.typeof = tk.Entry(self, width=30)
        self.author = tk.Entry(self, width=30)
        self.discipline = tk.Entry(self, width=30)
        self.year = tk.Entry(self, width=30)
        self.places = tk.Entry(self, width=30)

        name_hint = tk.Label(self, text='Наименование', width=30)
        typeof_hint = tk.Label(self, text='Вид работы', width=30)
        author_hint = tk.Label(self, text='Автор', width=30)
        discipline_hint = tk.Label(self, text='Дисциплина', width=30)
        year_hint = tk.Label(self, text='Год', width=30)
        place_hint = tk.Label(self, text='Место хранения', width=30)

        self.name.place(x=10, y=20)
        self.typeof.place(x=10, y=50)
        self.author.place(x=10, y=80)
        self.discipline.place(x=10, y=110)
        self.year.place(x=10, y=140)
        self.places.place(x=10, y=170)

        name_hint.place(x=300, y=20)
        typeof_hint.place(x=300, y=50)
        author_hint.place(x=300, y=80)
        discipline_hint.place(x=300, y=110)
        year_hint.place(x=300, y=140)
        place_hint.place(x=300, y=170)

        self.button_save = tk.Button(self, text='Сохранить', bg='#ffff33', width=40)
        self.button_save.bind('<Button-1>', lambda add: self.insert_table(self.name.get(),
                                                                          self.typeof.get(),
                                                                          self.author.get(),
                                                                          self.discipline.get(),
                                                                          self.year.get(),
                                                                          self.places.get()))
        self.button_save.pack(side=tk.BOTTOM)

        self.button_back = tk.Button(self, text='Назад', bg='#ffff33', width=40, command=self.close)
        self.button_back.pack(side=tk.BOTTOM)

        self.grab_set()
        self.focus_set()

    def insert_table(self, name, typeof, author, discipline, year, place):
        self.db.insert(name, typeof, author, discipline, year, place)
        self.db.view_table()
        self.destroy()

    def close(self):
        self.destroy()
