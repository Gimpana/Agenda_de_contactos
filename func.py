import db
import re

def comprobar_nombre_o_apellido():
    pass

def comprobar_mail(mail):
    pass

def crear_contacto():
        nombre = input("Dime el nombre: ") 
        nombre = nombre.lower()
        apellido = input("Dime el apellido: ")
        apellido = apellido.lower()
        movil = int(input("Dime el móvil: "))
        correo = input("Dime el correo: ")

        db.cur.execute("INSERT INTO Contactos (nombre, apellido, movil, correo) VALUES (?,?,?,?)",(nombre,apellido,movil,correo))
        db.conn.commit()
        
        if db.cur.rowcount != 0:
            print("\nContacto creado")

def buscar_contcto():

    buscar = input("Dime el nombre para buscar el contacto: ")
    buscar = buscar.lower()
    try:
        db.cur.execute("SELECT * FROM Contactos WHERE nombre = ?", (buscar,))
        contactos = db.cur.fetchall()[0]
        print("\n")
        for columna in contactos:
            print(" - ",columna, end="")
        print("\n")
    except:
        print("No existe contactos con este Nombre")

def actualizar_contactos():
    try:
        id_ = int(input("Dime el ID del contacto: "))
        db.cur.execute("SELECT id FROM Contactos")
        id_validas = []
        for ids in db.cur:
            id_validas.append(ids)
        
        id_validas_ok = []
        for l in id_validas:
            id_validas_ok.append(l[0])

        if id_ in id_validas_ok:
            db.cur.execute("SELECT * FROM Contactos WHERE id = ?", (id_,))
            fila = db.cur.fetchone()
            print("\n", end="")
            print(fila)
            print("""
    ¿Qué quieres modificar?

    1) Nombre
    2) Apellido
    3) Móvil
    4) Correo""")
            campo_A_modificar = int(input(
        """-:"""))
            if campo_A_modificar == 1:
                nuevo_nombre = (input("Dime el nuevo Nombre: "))
                nuevo_nombre = nuevo_nombre.lower()
                db.cur.execute("UPDATE Contactos SET nombre = ? WHERE id = ?", (nuevo_nombre, id_))
                db.conn.commit()
                if db.cur.rowcount != 0:
                    print("Se ha actualizado el contacto")
                    db.cur.execute("SELECT * FROM Contactos WHERE id = ?", (id_,))
                    x = db.cur.fetchone()
                    print("\n", end="")
                    print(x)
                else:
                    print("No se ha actualizado el contacto")

            if campo_A_modificar == 2:
                nuevo_apellido = input("Dime el nuevo Apellido: ")
                nuevo_apellido = nuevo_apellido.lower()
                db.cur.execute("UPDATE Contactos SET apellido = ? WHERE id = ?", (nuevo_apellido, id_))
                db.conn.commit()

            if campo_A_modificar == 3:
                nuevo_movil = int(input("Dime el nuevo Móvil: "))
                db.cur.execute("UPDATE Contactos SET movil = ? WHERE id = ?", (nuevo_movil, id_))
                db.conn.commit()

            if campo_A_modificar == 4:
                nuevo_correo = input("Dime el nuevo Correo: ")
                db.cur.execute("UPDATE Contactos SET correo = ? WHERE id = ?", (nuevo_correo, id_))
                db.conn.commit()

                for columna in db.cur:
                    print(columna)
    except:
        print("\nNo ingresas una ID válida")
        pregunta = input("\n¿Quieres ver todos los contactos para verificar ID? (y/n): ")
        if pregunta == "y":
            mostrar_todos_los_contactos()
        elif pregunta == "n":
            print("\n Hasta luego")
        else:
            print("\nNo es una opción válida, vuelve a escoger que quieres hacer")

def borrar_contacto():
    contacto_a_borrar = int(input("Dime el ID del contacto que quieres borrar: "))
    db.cur.execute("DELETE FROM Contactos WHERE id = ?", (contacto_a_borrar,))
    db.conn.commit()

    if db.cur.rowcount != 0:
        print("Se ha eliminado el contacto")
    else:
        print("No existe el contacto")

def mostrar_todos_los_contactos():
    db.cur.execute("SELECT * FROM Contactos")
    print("")
    for columna in db.cur:
        print(columna)


def comprobar_Entrada(hacer):
    lista = ["1","2","3","4","5"]
    if hacer in lista:
        return True
    else:
        return False