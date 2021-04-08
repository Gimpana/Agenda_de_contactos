import db

def crear_contacto(hacer):
        nombre = input("Dime el nombre: ") 
        apellido = input("Dime el apellido: ")
        movil = input("Dime el móvil: ")
        correo = input("Dime el correo: ")

        db.cur.execute("INSERT INTO Contactos (nombre, apellido, movil, correo) VALUES (?,?,?,?)",(nombre,apellido,movil,correo))
        db.conn.commit()

def buscar_contcto(hacer):

    buscar = input("Dime el nombre para buscar el contacto: ")
    try:
        db.cur.execute("SELECT * FROM Contactos WHERE nombre = ?", (buscar,))
        contactos = db.cur.fetchall()[0]
        for columna in contactos:
            print(" - ",columna, end="")
    except:
        print("No existe contactos con este Nombre")

def actualizar_contactos(hacer):
    actualizar = input("¿Quieres modificar el contacto? (y/n): ")
    if actualizar == "y":
        id_ = input("Dime el ID del contacto: ")
        escoger = print("""
    ¿Qué quieres modificar?

    1) Nombre
    2) Apellido
    3) Móvil
    4) Correo""")
        campo_A_modificar = int(input("-:"))
        if campo_A_modificar == 1:
            nuevo_nombre = input("Dime el nuevo Nombre: ")
            db.cur.execute("UPDATE Contactos SET nombre = ? WHERE id = ?", (nuevo_nombre, id_))
            db.conn.commit()

        if campo_A_modificar == 2:
            nuevo_apellido = input("Dime el nuevo Apellido: ")
            db.cur.execute("UPDATE Contactos SET apellido = ? WHERE id = ?", (nuevo_apellido, id_))
            db.conn.commit()

        if campo_A_modificar == 3:
            nuevo_movil = input("Dime el nuevo Móvil: ")
            db.cur.execute("UPDATE Contactos SET movil = ? WHERE id = ?", (nuevo_movil, id_))
            db.conn.commit()

        if campo_A_modificar == 4:
            nuevo_correo = input("Dime el nuevo Correo: ")
            db.cur.execute("UPDATE Contactos SET correo = ? WHERE id = ?", (nuevo_correo, id_))
            db.conn.commit()

        for columna in db.cur:
            print(columna)


def borrar_contacto(hacer):
    contacto_a_borrar = int(input("Dime el ID del contacto que quieres borrar: "))
    db.cur.execute("DELETE FROM Contactos WHERE id = ?", (contacto_a_borrar,))
    db.conn.commit()

    if db.cur.rowcount != 0:
        print("Se ha eliminado el contacto")
    else:
        print("No existe el contacto")

def mostrar_todos_los_contactos(hacer):
    db.cur.execute("SELECT * FROM Contactos")
    print("")
    for columna in db.cur:
        print(columna)


def comprobar_Entrada(hacer):
    lista = [1,2,3,4,5]
    if hacer in lista:
        return True
    else:
        return False