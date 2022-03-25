from funciones import *
from parametros import LARGO_CONTRASENA, MIN_CARACTERES, CONTRASENA_ADMIN

usuario_g = None
def main_menu():
    global usuario_g
    print("--- Bienvenido a DCCorreos de Chile ---")
    respuesta = input("¿Que desea hacer?\n[1] Iniciar sesion como usuario \
                [2] Registrarse como usuario \n[3] Iniciar sesion como administrador \
          [4] Salir del programa\n\nIndique su opcion: ")
    if respuesta.isdigit():
        if int(respuesta) == 1:
            usuario_g = input("Ingrese el nombre de usuario: ")
            autentificar_usuario(usuario_g)
        elif int(respuesta) == 2:
            registrar_usuario()

        elif int(respuesta) == 3:
            admin = input("Ingrese la contraseña de administrador: ")
            if admin == CONTRASENA_ADMIN:
                print("Inicio como administrador exitoso.")
                menu_administrador()
            else:
                print("Contraseña erronea.")
                menu_opciones_main()
        else:
            print("Saliendo del programa...")
    else:
        print("Ingrese una respuesta valida.")
        main_menu()



def autentificar_usuario(usuario):
    lista_usuario = []
    usuarios_password = {}
    with open ("usuarios.csv","r",encoding='utf-8') as usuarios:
        for linea in usuarios.readlines():
            lista_usuario.append(linea.strip().split(","))

    for i in lista_usuario:
        usuarios_password[i[0]] = i[1]

    if usuario not in usuarios_password.keys():
        print("El nombre de usuario no esta registrado.")
        main_menu()
    
    else:
        autentificar_contraseña(usuario)
 
def autentificar_contraseña(usuario):   

    contraseña = input("Ingrese la contraseña: ")
    lista_usuario = []
    usuarios_password = {}

    with open ("usuarios.csv","r",encoding='utf-8') as usuarios:
        for linea in usuarios.readlines():
            lista_usuario.append(linea.strip().split(","))

    for i in lista_usuario:
        usuarios_password[i[0]] = i[1]

    if contraseña not in usuarios_password[usuario]:
        print("La contraseña es erronea.")
        main_menu()
    else:
        print("Autentificacion exitosa.")
        menu_usuario() 

def registrar_usuario():
    global usuario_g
    lista_usuario = []
    usuarios_password = {}
    print("---Registrar usuario---")
    with open("usuarios.csv","r",encoding='utf-8') as usuarios:
        for i in usuarios.readlines():
            lista_usuario.append(i.strip().split(","))
    for i in lista_usuario:
        usuarios_password[i[0]] = i[1]
    usuario_g = input("Ingrese el nombre de su usuario:")
    if usuario_g not in usuarios_password.keys() and len(usuario_g) >= MIN_CARACTERES:
        print("Nombre valido.")
    elif usuario_g in usuarios_password.keys():
        print("El nombre ingresado se encuentra ocupado.")
        respuesta_invalida = True
        while respuesta_invalida:
            respuesta = (input("¿Que desea hacer?\n[1] Reintentar \
                [2] Menu de inicio: "))
            if respuesta.isdigit():
                if int(respuesta) == 1:
                    registrar_usuario()
                    respuesta_invalida = False
                elif int(respuesta) == 2:
                    main_menu()
                else:
                    print("Ingrese una opcion valida.")
                    respuesta_invalida = True
                    
            else:
                print("Ingrese una opcion valida.")
                respuesta_invalida = True
    else:
        print("El nombre ingresado debe tener minimo 5 caracteres")

        respuesta = int(input("¿Que desea hacer?\n[1] Reintentar \
                [2] Menu de inicio\n "))
        if respuesta == 1:
            registrar_usuario()
        else:
            main_menu()
    password = input("Ingrese una contraseña: ")
    print(f"{usuario_g},{password}")
    if len(password) >= LARGO_CONTRASENA and password.isalnum():
        print("Contraseña valida.")
        print('Registro exitoso.')
        with open("usuarios.csv","a",encoding='utf-8') as usuarios_act:
            usuarios_act.write(f"{usuario_g},{password}\n")
        menu_usuario()
    elif len(password) < LARGO_CONTRASENA:
        print("La contraseña debe ser de minimo 6 caracteres.")
        respuesta = int(input("¿Que desea hacer?\n[1] Reintentar \
                [2] Menu de inicio: "))
        if respuesta == 1:
            registrar_usuario()
        else:
            main_menu()
    else:
        print("La contraseña debe ser alfanumerica.")
        respuesta = int(input("¿Que desea hacer?\n[1] Reintentar \
                [2] Menu de inicio\nEliga una opcion: "))
        if respuesta == 1:
            registrar_usuario()
        else:
            main_menu()
     
def menu_usuario():
    print("--- Bienvenido al menu de usuario ---")
    respuesta = input("¿Que desea hacer?\n[1] Hacer encomienda \
                [2] Revisar estado de encomiendas hechas \n[3] Realizar reclamo \
                [4] Ver estado de pedidos personales\n[5] Cerrar sesion\n\nIndique su opcion: ")
    if respuesta.isdigit():

        if int(respuesta) == 1:
            print("--- Hacer encomienda ---")
            ingreso_encomienda()
            menu_opciones_usuario()
        elif int(respuesta) == 2:
            valor_funcion = estado_encomienda(usuario_g)
            if valor_funcion == True:
                menu_opciones_usuario()
            else:
                print("No se encontraron encomiendas.")
                menu_opciones_usuario()
        elif int(respuesta) == 3:
            realizar_reclamo(usuario_g)
            print("Redirigiendo al menu de usuario...")
            menu_usuario()
        elif int(respuesta) == 4:
            valor_funcion = estado_encomiendas(usuario_g)
            if valor_funcion == True:
                menu_opciones_usuario()
            else:
                print("No se encontraron encomiendas")
                menu_opciones_usuario()

            
        elif int(respuesta) == 5:
            main_menu()
        else: 
            print("Ingrese una respuesta valida.")
            menu_usuario()
    else:
        print("Ingrese una opcion valida.")
        menu_usuario()

def menu_administrador():
    print("--- Bienvenido al menu de administrador ---")
    respuesta = (input("\n¿Que desea hacer?\n[1] Actualizar encomiendas \
                 [2] Revisar reclamos \n[3] Cerrar sesion \nEliga una opcion:"))
    if respuesta.isdigit():

        if int(respuesta) == 1:
            print("--- Actualizar encomiendas ---")
            actualizar_encomiendas()
            print("Redirigiendo al menu de administrador...")
            menu_administrador()
        elif int(respuesta) == 2:
            revisar_reclamos()
            menu_opciones_admin_reclamos()
        elif int(respuesta) == 3:
            main_menu()
    else: 
        print("Ingrese una respuesta valida.")
        menu_administrador()

def menu_opciones_usuario():
    decision = input("Que desea hacer: \n \n[1] Volver al menu anterior \n[2] Cerrar sesion \nEliga una opcion: ")
    if decision.isdigit():
        if int(decision) == 1:
            menu_usuario()
        elif int(decision) == 2:
            main_menu()
    else:
        print("Pruebe una opcion valida")
        menu_opciones_usuario()
        
def menu_opciones_admin():
    decision = input("Que desea hacer: \n \n[1] Volver al menu anterior \n[2] Cerrar sesion \nEliga una opcion: ")
    if decision.isdigit():
        if int(decision) == 1:
            menu_administrador()
        elif int(decision) == 2:
            main_menu()
    else:
        print("Pruebe una opcion valida")
        menu_opciones_admin()

def menu_opciones_main():
    decision = input("Que desea hacer: \n \n[1] Volver al menu anterior \n[2] Cerrar programa \nEliga una opcion: ")
    if decision.isdigit():
        if int(decision) == 1:
            main_menu()
        elif int(decision) == 2:
            print("Saliendo del programa...")
            None
    else:
        print("Pruebe una opcion valida")
        menu_opciones_main()


def menu_opciones_admin_reclamos():
    decision = input("Que desea hacer: \n \n[1] Revisar otro reclamo\n[2] Volver al menu anterior \nEliga una opcion: ")
    if decision.isdigit():
        if int(decision) == 1:
            revisar_reclamos()
            menu_opciones_admin_reclamos()
        elif int(decision) == 2:
            menu_administrador()
    else:
        print("Pruebe una opcion valida")
        menu_opciones_admin_reclamos()



main_menu()


