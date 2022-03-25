from collections import namedtuple
import random
# class Carta:
#     def __init__(self, nombre, ataque, defensa):
#         self.nombre = nombre
#         self.ataque = ataque
#         self.defensa = defensa


class Juego:
 
    def __init__(self, turnos):
        
        self.mazo = []
        self.cartas_j1 = []
        self.cartas_j2 = []
        
        self.read_file()
        self.repartir_cartas()
        self.comenzar_juego(turnos)
    
    def read_file(self):

        tupla = namedtuple("Tupla", ["nombre","ataque","defensa"])

        with open("cards.csv", "r") as archivo:
            archivito = archivo.readlines()
            for linea in archivito[1:]:          
                linea_clean = linea.strip().split(",")
                carta = tupla(linea_clean[0],int(linea_clean[1]),int(linea_clean[2]))
    
                self.mazo.append(carta)
        # print(self.mazo)
          
        # Leer las cartas y guardarlas en una estructura de datos adecuada
        # NOTA: la primera fila del archivo son los atributos de las cartas
        pass
    
    def repartir_cartas(self):
        
        random.shuffle(self.mazo)

        for i in range(5):
            self.cartas_j1.append(self.mazo.pop(0))
            self.cartas_j2.append(self.mazo.pop(0))

        print(self.cartas_j1)

        print(self.cartas_j2)
          
        # Barajar las cartas y repartirlas de a 1
        pass
    
    def atacar(self, atacante, defensa):
    
        ptos_ataque = atacante.ataque
        ptos_defensa = defensa.defensa

        if ptos_ataque > ptos_defensa:
            
            return True

        elif ptos_ataque < ptos_defensa:

            return False
        else:

            return None

        # Rellenar aquí
  
    def comenzar_juego(self, turnos):


        for i in range(1, turnos + 1):
             
             
            random.shuffle(self.cartas_j1)
            random.shuffle(self.cartas_j2)

            print(f"Turno número {i}")
            if i % 2:
                if self.atacar(self.cartas_j1[0],self.cartas_j2[0]) == True:
                    self.cartas_j2.pop(0)
                    print("Gana jugador 1.")

                elif self.atacar(self.cartas_j1[0],self.cartas_j2[0]) == False:
                    print("Fracasa jugador 1.")
                    self.cartas_j1.pop(0)

                else:
                    print("Empate.")

            else:

                if self.atacar(self.cartas_j2[0],self.cartas_j1[0]) == True:
                    self.cartas_j1.pop(0)
                    print("Gana jugador 2.")

                elif self.atacar(self.cartas_j2[0],self.cartas_j1[0]) == False:
                    print("Fracasa jugador 2.")
                    self.cartas_j2.pop(0)

                else:
                    print("Empate.")

            if len(self.cartas_j1) == 0:
                print("XXXX Gana jugador 2 la partida XXXX")
                break
                
            
            elif len(self.cartas_j2) == 0:
                print("XXXX Gana jugador 1 la partida XXXX")
                break
                

            elif i == turnos:
                if len(self.cartas_j1) > len(self.cartas_j2):
                    print("XXXX Gana jugador 1 XXXX")
                    break
            
                elif len(self.cartas_j2) > len(self.cartas_j1):
                    print("XXXX Gana jugador 2 XXXX")
                    break







juego = Juego(10)

