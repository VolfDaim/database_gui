import sqlite3 as sl
import tkinter as tk


class DB:
    def __init__(self):
        self.connection = sl.Connection('university.db')
        self.c = self.connection.cursor()
        self.c.execute(
            'CREATE TABLE IF NOT EXISTS university (id integer primary key, name text, typeof text, author text, discipline text, year integer, place text)')

        self.connection.commit()

    def insert(self, name, typeof, author, discipline, year, place):
        self.connection.execute(
            'INSERT INTO university(name, typeof, author, discipline, year, place) VALUES (?,?,?,?,?,?)',
            (name, typeof, author, discipline, year, place)
        )
        self.connection.commit()

    def view_table(self):
        self.c.execute('SELECT * FROM university')
        self.connection.commit()

    def search_by(self, parameter, value):
        self.c.execute(f'SELECT * FROM university WHERE {parameter} = (?)', (value,))
        self.connection.commit()

    def delete_by(self,parameter,value):
        self.c.execute(f'DELETE FROM university WHERE {parameter} = (?)', (value, ))
        self.connection.commit()

    def delete_all(self):
        self.c.execute('DELETE FROM university')
        self.connection.commit()
