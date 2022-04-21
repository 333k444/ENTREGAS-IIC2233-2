
from tabulate import tabulate
from entidades import BrebajeMagico, Gaseosa, Jugo, Ludopata, Tacaño, Bebedor, Casual, Juego, Casino,\
Jugo, Gaseosa, BrebajeMagico, Show

class Menus:

    def lista_jugadores(self):
        lista = []
        with open ("jugadores.csv", "r", encoding='utf-8') as jugadores:
            for linea in jugadores:
                lista.append(linea.strip().split(","))
        lista.pop(0)
        return lista

    def juego_objetos(self):

        lista = []
        with open("juegos.csv" , "r", encoding='utf-8') as juegos:
            for linea in juegos:
                lista.append(linea.strip().split(","))
        lista.pop(0)
        lista_final = []
        for i in lista:

            juego_objeto = Juego(i[0], i[1], i[2], i[3]) 
            lista_final.append(juego_objeto)

        return lista_final

    def bebestible_objetos(self):

        lista = []
        with open("bebestibles.csv" , "r", encoding='utf-8') as bebestibles:
            for linea in bebestibles:
                lista.append(linea.strip().split(","))
        lista.pop(0)
        lista_final = []
        for i in lista:
            if i[1] == "Jugo":
                bebestible_objeto = Jugo(i[0], i[1], i[2])
                lista_final.append(bebestible_objeto) 
            elif i[1] == "Gaseosa":
                bebestible_objeto = Gaseosa(i[0], i[1], i[2])
                lista_final.append(bebestible_objeto) 
            else:
                bebestible_objeto = BrebajeMagico(i[0], i[1], i[2])
                lista_final.append(bebestible_objeto) 
                
        return lista_final
   
    def menu_inicio(self):
        print(" Menu de inicio ".center(30, "*"))
        print("-"*30)
        print("[1] Iniciar partida\n[X] Salir")
        decision_invalida = True
        while decision_invalida:
            decision = input("Escoga una opcion: ")
            if decision == "1":
                decision_invalida = False
                self.menu_opciones_jugador()
            elif decision.capitalize() == "X":
                decision_invalida = False
                print("Saliendo del programa... ")
                None
            else:
                print("\nEscoga una alternativa valida.\n ")
                
    def menu_opciones_jugador(self):
        print(" Opciones de Jugador ".center(30, "*"))
        print("-"*30)
        lista = self.lista_jugadores()
        jug_perso = []
        for i in lista:
            jug_perso.append([i[0],i[1]])
        for i in jug_perso:
            print(
f"[{jug_perso.index(i)+1}] {jug_perso[jug_perso.index(i)][0]}: {jug_perso[jug_perso.index(i)][1]}")
        
        decision_invalida = True
        print(f"[0] Volver\n[{len(jug_perso)+1}] Salir ")

        while decision_invalida:
            decision = input("Escoga una opcion: ")

            if decision.isdigit():

                if 1 <= int(decision) <= len(jug_perso):
                    decision_invalida = False
                    if lista[int(decision)-1][1] == "Ludopata":
                        self.jugador_ingreso = Ludopata(
                        lista[int(decision)-1][0],lista[int(decision)-1][1],
                        lista[int(decision)-1][2],lista[int(decision)-1][3],
                        lista[int(decision)-1][4],lista[int(decision)-1][5],
                        lista[int(decision)-1][6],lista[int(decision)-1][7],
                        lista[int(decision)-1][8],lista[int(decision)-1][9]
                        )
                        self.menu_principal()

                    elif lista[int(decision)-1][1] == "Tacano":
                        self.jugador_ingreso = Tacaño(
                        lista[int(decision)-1][0],lista[int(decision)-1][1],
                        lista[int(decision)-1][2],lista[int(decision)-1][3],
                        lista[int(decision)-1][4],lista[int(decision)-1][5],
                        lista[int(decision)-1][6],lista[int(decision)-1][7],
                        lista[int(decision)-1][8],lista[int(decision)-1][9]
                        )
                        self.menu_principal()

                    elif lista[int(decision)-1][1] == "Bebedor":
                        self.jugador_ingreso = Bebedor(
                        lista[int(decision)-1][0],lista[int(decision)-1][1],
                        lista[int(decision)-1][2],lista[int(decision)-1][3],
                        lista[int(decision)-1][4],lista[int(decision)-1][5],
                        lista[int(decision)-1][6],lista[int(decision)-1][7],
                        lista[int(decision)-1][8],lista[int(decision)-1][9]
                        )
                        self.menu_principal()
                    
                    elif lista[int(decision)-1][1] == "Casual":
                        self.jugador_ingreso = Casual(
                        lista[int(decision)-1][0],lista[int(decision)-1][1],
                        lista[int(decision)-1][2],lista[int(decision)-1][3],
                        lista[int(decision)-1][4],lista[int(decision)-1][5],
                        lista[int(decision)-1][6],lista[int(decision)-1][7],
                        lista[int(decision)-1][8],lista[int(decision)-1][9]
                        )
                        self.menu_principal()
                

                elif int(decision) == 0:
                    decision_invalida = False
                    self.menu_inicio()
            
                elif int(decision) == len(jug_perso) + 1:
                    decision_invalida = False
                    print("\nSaliendo del programa...\n ")
                    None

                else:
                    print("\nEscoga una opcion valida.\n ")
            else:
                print("\nEscoga una opcion valida.\n ")


    def menu_principal(self):

        juegos = self.juego_objetos()
        jugos = self.bebestible_objetos()
        self.casino = Casino(self.jugador_ingreso, jugos, juegos)
        print(" Menu Principal ".center(30, "*"))
        print("-"*30)
        print(
    "[1] Opciones de juegos\n[2] Comprar bebestibles\n[3] Habilidades jugador\n[4] Ver show")
        print("[0] Volver\n[X] Salir")
        decision_invalida = True
        while decision_invalida:
            decision = input("Escoga una opcion: ")

            if decision == "1":
                decision_invalida = False
                self.menu_juegos()
            elif decision == "2":
                decision_invalida = False
                self.menu_bebestibles()
            elif decision == "3":
                decision_invalida = False
                self.stats()
            elif decision == "4":
                decision_invalida = False
                self.ver_show()
            elif decision == "0":
                decision_invalida = False
                self.menu_opciones_jugador()
            elif decision.capitalize() == "X":
                decision_invalida = False
                print("Saliendo del programa... ")

            else:
                print("\nEscoga una opcion valida.\n ")

    def menu_juegos(self):

        print(" Opciones de Juegos ".center(30, "*"))
        print("-"*30)
        dic = {"nombre":None,"esperanza":None,"apuesta_minima":None,"apuesta_maxima":None}

        indx = 0
        for i in self.casino.juegos:
            indx += 1
            print(f'{[indx]} {i.nombre.capitalize()} ')
        print("\n[0] Volver\n[X] Salir ")

        decision_invalida = True
        while decision_invalida:
            decision = input("Escoga una opcion: ")
            if decision.isdigit():

                if 1 <= int(decision) <= len(self.casino.juegos):
                    decision_invalida = False
                    dic["nombre"] = self.casino.juegos[int(decision)-1].nombre
                    dic["esperanza"] = self.casino.juegos[int(decision)-1].esperanza
                    dic["apuesta_minima"] = self.casino.juegos[int(decision)-1].apuesta_minima
                    dic["apuesta_maxima"] = self.casino.juegos[int(decision)-1].apuesta_maxima

                    self.juego_ingreso = Juego(**dic)
                    self.casino.jugar(self.jugador_ingreso,self.juego_ingreso)   

                    if self.jugador_ingreso.ganar == True or self.jugador_ingreso.ganar == False:
                        self.casino.evento_especial()
                        self.jugador_ingreso.ganar = None

                    self.menu_principal()

            if decision == "0":
                decision_invalida = False
                self.menu_principal()

            elif decision.capitalize() == "X":
                decision_invalida = False
                print("Saliendo del programa... ")   

            else:
                print("\nEscoga una opcion valida.\n ")
                    

    def menu_bebestibles(self):
        print(" Bebestibles ".center(30, "*"))
        print("-"*30)
        tabla = []
        dic = {"nombre":None,"tipo":None,"precio":None}
        indx = 0
        for i in self.casino.bebestibles:
            indx += 1
            tabla.append([f"[{indx}]",i.nombre, i.tipo, i.precio])   
        print("\n")
        print(tabulate(tabla,headers=["Opcion","Nombre","Tipo","Precio"]))
        
        print("\n[0] Volver\n[X] Salir ")

        decision_invalida = True
        while decision_invalida:

            decision = input("Escoga una opcion: ")
            if decision.isdigit():

                if 1 <= int(decision) <= len(self.casino.bebestibles):
                    decision_invalida = False
                    dic["nombre"] = self.casino.bebestibles[int(decision)-1].nombre
                    dic["tipo"] = self.casino.bebestibles[int(decision)-1].tipo
                    dic["precio"] = self.casino.bebestibles[int(decision)-1].precio

                    if dic["tipo"] == "Jugo":
                        bebestible_compra = Jugo(**dic)
                        a = self.casino.jugador.comprar_bebestible(self.casino.jugador, bebestible_compra)
                        if a == False:
                            self.menu_bebestibles()
                        else:
                            self.menu_principal()

                    elif dic["tipo"] == "Gaseosa":
                        bebestible_compra = Gaseosa(**dic)
                        a = self.casino.jugador.comprar_bebestible(self.casino.jugador, bebestible_compra)
                        if a == False:
                            self.menu_bebestibles()
                        else:
                            self.menu_principal()

                    elif dic["tipo"] == "Brebaje mágico":
                        bebestible_compra = BrebajeMagico(**dic)
                        a = self.casino.jugador.comprar_bebestible(self.casino.jugador, bebestible_compra)
                        if a == False:
                            self.menu_bebestibles()
                        else:
                            self.menu_principal()

            if decision == "0":
                    decision_invalida = False
                    self.menu_principal()

            elif decision.capitalize() == "X":
                decision_invalida = False
                print("\nSaliendo del programa... \n")
            else:
                print("\nIngrese una opcion valida\n")

            

    def stats(self):
        print(" Estado Jugador ".center(30, "*"))
        print("-"*30)
        print(f"Nombre: {self.jugador_ingreso.nombre}\nPersonalidad: {self.jugador_ingreso.personalidad}")
        print(f"Energia: {self.jugador_ingreso.energia}\nSuerte: {self.jugador_ingreso.suerte}")
        print(f"Dinero: {self.jugador_ingreso.dinero}\nFrustracion: {self.jugador_ingreso.frustracion}")
        print(f"Ego: {self.jugador_ingreso.ego}\nCarisma: {self.jugador_ingreso.carisma}")
        print(f"Confianza: {self.jugador_ingreso.confianza}\nJuego favorito: {self.jugador_ingreso.juego_favorito}")
        print(f"Dinero faltante: {self.casino.dinero_faltante}")

        print("\n[0] Volver\n[X] Salir ")

        decision_invalida = True
        while decision_invalida:
            decision = input("Escoga una opcion: ")
            if decision == "0":
                decision_invalida = False
                self.menu_principal()
            elif decision.capitalize() == "X":
                decision_invalida = False
                print("Saliendo del programa... ")
            else:
                print("Ingrese una opcion valida ")

    def ver_show(self):
        Show.ver_show(self, self.jugador_ingreso)
        self.menu_principal()
        



           

        
        
            
            
        # decision_invalida = True
        # while decision_invalida:

        #     decision = input("Escoga una opcion: ")
        #     if 1 <= int(decision) <= len(self.casino.bebestibles):


        
        
if __name__ == "__main__":
    run_program = Menus()
    run_program.menu_inicio()
