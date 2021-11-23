import tkinter as tk


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_interface()

    def init_interface(self):
        button_add = tk.Button(text="Добавить информацию о материале", bg='#ffff33', width=40, command=self.call_save,
                               pady='8').pack()
        button_check = tk.Button(text="Просмотреть информацию", bg='#ffff33', width=40, pady='8').pack()
        button_exit = tk.Button(text="Выход", bg='#ffff33', width=40, pady='8', command=self.exit).pack()

    def call_save(self):
        Add()

    def exit(self):
        root.destroy()


class Add(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        w = root.winfo_screenwidth()
        h = root.winfo_screenheight()
        w //= 2
        h //= 2
        self.geometry(f"550x650+{w - 550 // 2}+{h - 650 // 2}")
        self.config(bg='#000000')
        self.title('Добавить информацию о материале')
        self.resizable(False, False)

        self.grab_set()
        self.focus_set()

        self.init_interface()

    def init_interface(self):
        name = tk.Entry(self, width=30)
        typeof = tk.Entry(self, width=30)
        author = tk.Entry(self, width=30)
        year = tk.Entry(self, width=30)
        place = tk.Entry(self, width=30)

        name_hint = tk.Label(self, text='Наименование', width=30)
        typeof_hint = tk.Label(self, text='Вид работы', width=30)
        author_hint = tk.Label(self, text='Автор', width=30)
        year_hint = tk.Label(self, text='Дисциплина', width=30)
        place_hint = tk.Label(self, text='Место хранения', width=30)

        name.place(x=10, y=20)
        typeof.place(x=10, y=50)
        author.place(x=10, y=80)
        year.place(x=10, y=110)
        place.place(x=10, y=140)

        name_hint.place(x=300, y=20)
        typeof_hint.place(x=300, y=50)
        author_hint.place(x=300, y=80)
        year_hint.place(x=300, y=110)
        place_hint.place(x=300, y=140)

        button_save = tk.Button(self, text='Сохранить', bg='#ffff33', width=40).pack(side=tk.BOTTOM)
        button_back = tk.Button(self, text='Назад', bg='#ffff33', width=40, command=self.close).pack(side=tk.BOTTOM)

    def close(self):
        self.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    root.title("Database university")
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w //= 2
    h //= 2
    root.geometry(f"550x650+{w - 550 // 2}+{h - 650 // 2}")
    root.config(bg='#000000')
    root.resizable(False, False)
    root.mainloop()
