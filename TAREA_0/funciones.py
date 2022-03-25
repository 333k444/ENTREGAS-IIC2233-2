from datetime import datetime
from datetime import date
from parametros import MAX_PESO


def ingreso_encomienda():
    lista = []
    with open ("usuarios.csv" , "r", encoding='utf-8') as usuarios:
        for i in usuarios.readlines():
            lista.append(i.strip().split(",")[0])
    lista.pop(0)

    nombre_invalido = True   
    while nombre_invalido:
        nombre_articulo = input("Ingrese el nombre del articulo: ")
        if nombre_articulo.count(',') == 0:
            nombre_invalido = False
        else:
            print("--- El valor ingresado no puede tener comas (,) ---")
            a=True
            while a:
                decision = input("Que desea hacer: \n \n [1] Continuar \n [2] Cancelar encomienda\nIngrese su opcion: ")
                if decision.isdigit():
                    if int(decision) == 1:
                        a = False
                    elif int(decision) == 2:
                        print("\nCancelando encomienda...\n")
                        a = False
                        nombre_invalido = False
                        return None
                    else:
                        print("Ingrese una opcion valida.")
                else:
                        print("Ingrese una opcion valida.")


    destinatario_invalido = True
    while destinatario_invalido:        
        nombre_destinatario = input("Ingrese el nombre del destinatario: ")
        if nombre_destinatario in lista:
            destinatario_invalido = False
        else:
            print("--- El valor ingresado no cumple con los requisitos ---")
            a=True
            while a:
                decision = input("Que desea hacer: \n \n [1] Continuar \n [2] Cancelar encomienda\nIngrese su opcion: ")
                if decision.isdigit():
                    if int(decision) == 1:
                        a = False
                    elif int(decision) == 2:
                        print("\nCancelando encomienda...\n")
                        a = False
                        nombre_invalido = False
                        return None
                    else:
                        print("Ingrese una opcion valida.")
                else:
                        print("Ingrese una opcion valida.")

    peso_invalido = True
    while peso_invalido:
        peso_articulo = input("Ingrese el peso del articulo: ")
        if peso_articulo.isdigit():
            if int(peso_articulo) < MAX_PESO:
                peso_invalido = False
            else:
                print("--- El peso ingresado sobrepasa el maximo permitido ---")
                decision = input("Que desea hacer: \n \n [1] Continuar \n [2] Cancelar encomienda\nIngrese su opcion: ")

                a=True
                while a:
                    decision = input("Que desea hacer: \n \n [1] Continuar \n [2] Cancelar encomienda\nIngrese su opcion: ")
                    if decision.isdigit():
                        if int(decision) == 1:
                            a = False
                        elif int(decision) == 2:
                            print("\nCancelando encomienda...\n")
                            a = False
                            peso_invalido = False
                            return None
                        else:
                            print("Ingrese una opcion valida.")
                    else:
                        print("Ingrese una opcion valida.")

        else:
            print("\nIngrese un valor valido.\n")
            peso_invalido = True

    destino_invalido = True
    while destino_invalido:

        destino_articulo = input("Ingrese el destino del articulo: ")
        if destino_articulo.count(",") == 0:
            destino_invalido = False

        else:
            print("--- El valor ingresado no cumple con los requisitos ---")
            a = True
            while a:
                decision = input("Que desea hacer: \n \n [1] Continuar \n [2] Cancelar encomienda\nIngrese su opcion: ")
                if decision.isdigit():
                    if int(decision) == 1:
                        a = False
                    elif int(decision) == 2:
                        print("\nCancelando encomienda...\n")
                        a = False
                        destino_invalido = False
                        return None
                    else:
                        print("Ingrese una opcion valida.")
                else:
                    print("Ingrese una opcion valida.")
        
    print("Datos entregados satisfactoriamente.")

    #Codigo basado en stack overflow #Codigo basado en stack overflow
    now = datetime.now()
    tiempo = now.strftime("%H:%M:%S")
    fecha = date.today()
    #Codigo basado en stack overflow #Codigo basado en stack overflow
    with open("encomiendas.csv" ,"a",encoding='utf-8') as encomiendas_write:
        encomiendas_write.write(f"\n{nombre_articulo},{nombre_destinatario},{peso_articulo},{destino_articulo},{fecha} {tiempo},Emitida")


def estado_encomienda(nombre_usuario):
    estado = False
    lista = []
    with open ("encomiendas.csv","r",encoding='utf-8') as encomiendas:
        for i in encomiendas.readlines():
            lista.append(i.strip().split(","))
    lista.pop(0)

    for i in lista:
        nombre_articulo = (i[0])
        estado_articulo = (i[5])
        if i[1] == nombre_usuario:
            print(f"\nEl estado de su articulo {nombre_articulo} es {estado_articulo}.\n")
            estado = True
    return estado
       
            
def realizar_reclamo(nombre_usuario):
    titulo = input("Ingrese el titulo del reclamo: ")
    descripcion = input("Ingrese la descripcion del reclamo: ")
    with open ("reclamos.csv","a",encoding='utf-8') as reclamos:
        reclamos.write(f"\n{nombre_usuario},{titulo},{descripcion}")
    print("\nSu reclamo fue enviado satisfactoriamente, lo revisaremos lo mas pronto posible.\n")


    
def estado_encomiendas(nombre_usuario):
    estado = False
    print(nombre_usuario)
    lista_encomiendas = []
    with open("encomiendas.csv","r",encoding='utf-8') as encomiendas:
        for i in encomiendas:
            lista_encomiendas.append(i.strip().split(","))
    lista_encomiendas.pop(0)
    num = 1

    for i in lista_encomiendas:
        if nombre_usuario == i[1]:
            print(f"[{num}]  ||NOMBRE||: {i[0]}   ||USUARIO||: {i[1]}   ||PESO||: {i[2]}   ||DESTINO||: {i[3]}   ||FECHA||: {i[4]}   ||ESTADO||: {i[5]}")
            num +=1
            estado = True
    return estado
     

def actualizar_encomiendas():
    print("--- Encomiendas registradas ---")
    lista_encomiendas = []
    with open("encomiendas.csv","r",encoding='utf-8') as encomiendas:
        for i in encomiendas.readlines():
            lista_encomiendas.append(i.strip().split(","))

    primera_linea = lista_encomiendas.pop(0) 
    num = 1

    for i in lista_encomiendas:
        print(f"[{num}]  |NOMBRE|: {i[0]}   |USUARIO|: {i[1]}   |PESO|: {i[2]}   |DESTINO|: {i[3]}   |FECHA|: {i[4]}   |ESTADO|: {i[5]}")
        num +=1

    seleccion = input('Seleccione el numero de encomienda que desea cambiar: ')
    if seleccion.isdigit():
        for i in range(len(lista_encomiendas)):
            if i == int(seleccion) - 1:
                estado_encomienda = lista_encomiendas[(i)][5]
                cambio = (actualizar_estado(estado_encomienda))
                if cambio != None:
                    lista_encomiendas[i][5] = cambio
                    print("\nEncomienda actualizada\n")
                else:
                    print("Porfavor, pruebe otra opcion.")
                    actualizar_encomiendas()
    else:
        print("Ingrese una opcion valida.")
        actualizar_encomiendas()


    lista_archivo = [primera_linea]
    for i in lista_encomiendas:
        lista_archivo.append(i)

    with open("encomiendas.csv","w",encoding='utf-8') as encomiendas_nuevas:

        for i in range(len(lista_archivo)):
            if i != 0:
                encomiendas_nuevas.write("\n")

            for j in range(len(lista_archivo[i])):
                encomiendas_nuevas.write(lista_archivo[i][j])
                if lista_archivo[i][j] != lista_archivo[i][-1]:
                    encomiendas_nuevas.write(",")
    

def actualizar_estado(estado_encomienda):

    if estado_encomienda == "Emitida":
        return "Revisada por agencia"
    elif estado_encomienda == "Revisada por agencia":
        return "En camino"
    elif estado_encomienda == "En camino":
        return "En destino"
    else:
        print("\nLa encomienda elegida ya esta en destino.\n")

def revisar_reclamos():
    lista_reclamos = []
    cuerpo_reclamos = []
    titulo_reclamos = []
    
    with open("reclamos.csv","r",encoding='utf-8') as reclamos:
        for i in reclamos.readlines():
            lista_reclamos.append(i.strip().split(",",maxsplit=2))
    lista_reclamos.pop(0)
    for i in lista_reclamos:
        titulo_reclamos.append(i[1])
        cuerpo_reclamos.append(i[2])
 
    num = 1
    print("\nSeleccione el reclamo deseado:\n")
    for i in titulo_reclamos:
        print(f"[{num}] {i}")
        num += 1
    respuesta = input("Ingrese un numero: ")
    if respuesta.isdigit():
        for j in range(len(cuerpo_reclamos)+1):
            if int(respuesta) - 1 == j:
                print(f"Descripcion: {cuerpo_reclamos[j]}")
    else:
        print("\nSeleccione una opcion valida.\n")
        revisar_reclamos()

    



    












            
    





                


        
