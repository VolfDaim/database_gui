import tkinter as tk
from tkinter import ttk

from database import DB
from menu import Main

if __name__ == '__main__':
    root = tk.Tk()
    db = DB()
    app = Main(root, db)
    #app.pack()
    root.title("Database university")
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w //= 2
    h //= 2
    root.geometry(f"550x650+{w - 550 // 2}+{h - 650 // 2}")
    root.config(bg='#ffffff')
    root.resizable(False, False)
    root.mainloop()
