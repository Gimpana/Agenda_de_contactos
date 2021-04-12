from func import *

print("""
******************************************
*               Bienvenido!!             *
*                                        *             
* Dime lo que quieres hacer en la Agenda *
*                                        *
******************************************""")

print("""
1) Crear contacto
2) Buscar contacto
3) Actualizar contacto
4) Borrar contacto
5) Mostrar todos los contactos""")

hacer = input("\nEscoge el número de una opción o salir: ")

while True:
    if hacer == "salir":
        break

    if hacer == "1":
        crear_contacto()

    if hacer == "2":    
        buscar_contcto()
        
    if hacer == "3":
        actualizar_contactos()
        
    if hacer == "4":
        borrar_contacto()
        
    if hacer == "5":
        mostrar_todos_los_contactos()
    
    if comprobar_Entrada(hacer) == False:
        print("""
*******************************************
** Por favor introduce una opción válida **
*******************************************""")
    
    print("""
******************************************
*                                        *       
* Dime lo que quieres hacer en la Agenda *
*                                        *
******************************************""")

    print("""
1) Crear contacto
2) Buscar contacto
3) Actualizar contacto
4) Borrar contacto
5) Mostrar todos los contactos""")

    hacer = input("\nEscoge el número de una opción o salir: ")
    