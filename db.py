import sqlite3

conn = sqlite3.connect("Agenda.sqlite")
cur = conn.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS Contactos 
                (id INTEGER PRIMARY KEY, nombre TEXT, apellido TEXT, movil INTEGER, correo TEXT)""")
conn.commit()