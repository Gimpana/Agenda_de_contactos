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

hacer = int(input("\nEscoge el número de una opción: "))

while True:
    if hacer == 1:
        crear_contacto(hacer)

    if hacer == 2:    
        buscar_contcto(hacer)
        
    if hacer == 3:
        actualizar_contactos(hacer)
        
    if hacer == 4:
        borrar_contacto(hacer)
        
    if hacer == 5:
        mostrar_todos_los_contactos(hacer)
    
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

    hacer = int(input("\nEscoge el número de una opción: "))
    