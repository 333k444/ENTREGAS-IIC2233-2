from abc import ABC, abstractmethod
from random import random, randint, choice
from parametros import PORCENTAJE_APUESTA_TACANO, BONIFICACION_TACANO, BONIFICACION_SUERTE_CASUAL,\
     CONFIANZA_PERDER, FRUSTRACION_PERDER, EGO_GANAR, CARISMA_GANAR, FRUSTRACION_GANAR,\
    MIN_ENERGIA_BEBESTIBLE, MAX_ENERGIA_BEBESTIBLE, PROBABILIDAD_EVENTO, DEUDA_TOTAL,\
        BONIFICACION_BEBEDOR, DINERO_SHOW, ENERGIA_SHOW, FRUSTRACION_SHOW

class Casino:

    def __init__(self,jugador,bebestibles,juegos):

        self.jugador = jugador
        self.bebestibles = bebestibles
        self.juegos = juegos
        self.dinero_faltante = DEUDA_TOTAL - int(self.jugador.dinero) 

    def evento_especial(self):

        probabilidad = random()
        if probabilidad <= PROBABILIDAD_EVENTO:
            regalo = choice(self.bebestibles)
            print(f"\n----Iniciando evento especial, ¡el jugador {self.jugador.nombre} adquiere {regalo.nombre} gratis!----\n")
            regalo.consumir(self.jugador)
        else:
            print("\nNo hay evento especial en esta ocasion :c\n ")
        
    def jugar(self, jugador, juego):
        self.jugador.apostar(jugador, juego)


class Jugador(ABC):
    def __init__(
    self,nombre,personalidad, energia, suerte, dinero, frustracion, ego, carisma, confianza, juego_favorito):
        self.nombre = nombre
        self.personalidad = personalidad
        self.__energia = int(energia)
        self.__suerte = int(suerte)
        self.dinero = int(dinero)
        self.__frustracion = int(frustracion)
        self.__ego = int(ego)
        self.__carisma = int(carisma)
        self.__confianza = int(confianza)
        self.juego_favorito = juego_favorito
        self.juegos_jugados = []
        self.ganar = None

########################################
    @property
    def energia(self):
        return self.__energia

    @energia.setter
    def energia(self,value):
        if value >= 100:
            self.__energia = 100
        elif value <= 0:
            self.__energia = 0
        else:
            self.__energia = value

    @property
    def suerte(self):
        return self.__suerte

    @suerte.setter
    def suerte(self,value):
        if value >= 50:
            self.__suerte = 50
        elif value <= 0:
            self.__suerte = 0
        else:
            self.__suerte = value
    @property
    def frustracion(self):
        return self.__frustracion

    @frustracion.setter
    def frustracion(self,value):
        if value >= 100:
            self.__frustracion = 100
        elif value <= 0:
            self.__frustracion = 0
        else:
            self.__frustracion = value 
    @property
    def ego(self):
        return self.__ego

    @ego.setter
    def ego(self,value):
        if value >= 15:
            self.__ego = 15
        elif value <= 0:
            self.__ego = 0
        else:
            self.__ego = value
    @property
    def carisma(self):
        return self.__carisma

    @carisma.setter
    def carisma(self,value):
        if value >= 50:
            self.__carisma = 50
        elif value <= 0:
            self.__carisma = 0
        else:
            self.__carisma = value
    @property
    def confianza(self):
        return self.__confianza

    @confianza.setter
    def confianza(self,value):
        if value >= 30:
            self.__confianza = 30
        elif value <= 0:
            self.__confianza = 0
        else:
            self.__confianza = value
    
#######################################

    def comprar_bebestible(self, jugador, bebestible_ob):
        
        if bebestible_ob.precio <= self.dinero:
            print(f"\n{bebestible_ob.nombre} fue adquirido por {bebestible_ob.precio}\n ")
            self.dinero -= int(bebestible_ob.precio)
            bebestible_ob.consumir(jugador)
            print("\nGracias por su compra!\n ")
        else:
            print(f"\nNo se puede costear el bebestible {bebestible_ob.nombre}\n ")
            return False

    @abstractmethod
    def apostar(self,jugador,juego):

        if self.energia >= round((self.ego + self.frustracion)*0.15):
            print(f"¡Bienvenido a {juego.nombre}!")
            self.apuesta = int(input("Ingrese el dinero que desea apostar: "))
            if self.apuesta <= self.dinero:

                if self.juego_favorito == juego.nombre:
                    favorito = 1
                else:
                    favorito = 0

                self.energia -= round((self.ego + self.frustracion)*0.15)

                self.probabilidad_ganar_jugador = min(1,max(0,(
                int(self.suerte)*15-int(self.apuesta)*0.4+
                int(self.confianza)*3*int(favorito)+int(self.carisma)*2)/1000))

                juego.probabilidad_de_ganar(self.apuesta, self.probabilidad_ganar_jugador, jugador, favorito)
            else:
                print("\nNo se tiene el dinero suficiente para esta apuesta.\n ")
        else:
            print("\nNo tienes suficiente energia! Compra un bebestible para recuperarte\n")

class Ludopata(Jugador):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def apostar(self,jugador,juego):
        super().apostar(jugador,juego)
        if self.ganar == True or self.ganar == False:
            self.ludopatia()

    def ludopatia(self):
        print("\nRealizando ludopatía...\n ")
        print("\nSe aumenta el ego y la suerte...\n ")
        
        self.ego += 2
        self.suerte += 3
        if self.ganar == False:
            self.frustracion += 5
            
class Tacaño(Jugador):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
    def apostar(self,jugador,juego):
        super().apostar(jugador,juego)
        if self.ganar == True:
            self.tacano_maximo()

    def tacano_maximo(self):
        print("\nRealizando accion tacaño maximo...\n ")
        porcentaje_apuesta = self.apuesta*100/self.dinero
        if porcentaje_apuesta < PORCENTAJE_APUESTA_TACANO and self.ganar == True:
            self.dinero += BONIFICACION_TACANO
            print(f"¡\n{self.nombre} gana una bonificacion de {BONIFICACION_TACANO} pesos por accion tacaña!\n ")
        
class Bebedor(Jugador):

    def __init__(self,*args,**kwargs):

        super().__init__(*args,**kwargs)

    def apostar(self,jugador,juego):
        super().apostar(jugador,juego)


class Casual(Jugador):
    def __init__(self,*args,**kwargs):

        super().__init__(*args,**kwargs)

    def apostar(self,jugador,juego):
        super().apostar(jugador,juego)
        if self.ganar == True or self.ganar == False:
            print(f"¡{self.nombre} recibe suerte de principiante! ")
            self.suerte_principiante()

    def suerte_principiante(self):
        unica_vez = 0
        if unica_vez == 0:
            unica_vez += 1
            self.suerte += BONIFICACION_SUERTE_CASUAL
            print("\nObteniendo suerte de principiante...\n ")
            print("\nSuerte aumentada\n ")

class Juego:
    def __init__(
        self, nombre, esperanza, apuesta_minima, apuesta_maxima):

        self.nombre = nombre
        self.esperanza = esperanza
        self.apuesta_minima = apuesta_minima
        self.apuesta_maxima = apuesta_maxima

    def entregar_resultados(self, apuesta, probabilidad_de_ganar, jugador):

        roll = random()
        if roll <= probabilidad_de_ganar:
            jugador.ego += EGO_GANAR
            jugador.carisma += CARISMA_GANAR
            jugador.frustracion -= FRUSTRACION_GANAR
            jugador.ganar = True
            jugador.dinero += apuesta*2
            print(f"\n¡{jugador.nombre} gana la apuesta! ")
            print(f"Ganancias totales: {apuesta*2}\n")
            
        else:
            jugador.frustracion -= FRUSTRACION_PERDER
            jugador.confianza -= CONFIANZA_PERDER
            jugador.ganar = False
            jugador.dinero -= apuesta
            print(f"\n¡{jugador.nombre} pierde la apuesta! ")
            print(f"Perdidas totales: {apuesta}\n")
            
    def probabilidad_de_ganar(self, apuesta, probabilidad_ganar_jugador, jugador, favorito):

        print(f"\nLa apuesta minima para {self.nombre} es {self.apuesta_minima} ")
        print(f"La apuesta maxima para {self.nombre} es {self.apuesta_maxima}\n ")

        if int(self.apuesta_minima) <= (apuesta) <= int(self.apuesta_maxima):
            probabilidad_de_ganar = (min(1, probabilidad_ganar_jugador - ((apuesta-(favorito*50-(int(self.esperanza)*30))))/10000))

            print(f"\nLa probabilidad de ganar es: {probabilidad_de_ganar}\n ")

            self.entregar_resultados(apuesta, probabilidad_de_ganar, jugador)

        else:
            print("\nLa apuesta ingresada no cumple con los requisitos.\n ")
            
class Bebestibles(ABC):
    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = int(precio)

    @abstractmethod
    def consumir(self):
        pass

class Jugo(Bebestibles):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def consumir(self,jugador):
        energia_recuperada = randint(MIN_ENERGIA_BEBESTIBLE,MAX_ENERGIA_BEBESTIBLE)
        jugador.energia += energia_recuperada

        if len(self.nombre) <= 4:
            if jugador.personalidad == "Bebedor":
                print("Aplicando bonificacion por cliente frecuente...")
                jugador.ego += 4*BONIFICACION_BEBEDOR
                print(
                f"\n{jugador.nombre} ha recibido {4*BONIFICACION_BEBEDOR} puntos de ego gracias al bebestible {self.nombre}\n ")
            else:
                jugador.ego += 4
                print(
                f"\n{jugador.nombre} ha recibido 4 puntos de ego gracias al bebestible {self.nombre}\n ")

        elif 5 <= len(self.nombre) <= 7 :

            if jugador.personalidad == "Bebedor":
                print("Aplicando bonificacion por cliente frecuente... ")
                jugador.suerte += 7*BONIFICACION_BEBEDOR

                print(
                f"\n{jugador.nombre} ha recibido {7*BONIFICACION_BEBEDOR} puntos de suerte gracias al bebestible {self.nombre}\n ")

            else:
                jugador.suerte += 7
                print(
                f"\n{jugador.nombre} ha recibido 7 puntos de suerte gracias al bebestible {self.nombre}\n ")

        else:
            if jugador.personalidad == "Bebedor":
                print("Aplicando bonificacion por cliente frecuente... ")
                jugador.frustracion -= 10*BONIFICACION_BEBEDOR
                jugador.ego += 11*BONIFICACION_BEBEDOR

                print(
                f"\n{jugador.nombre} ha disminuido su frustracion en {10*BONIFICACION_BEBEDOR}"
                f" y aumentado su ego en {11*BONIFICACION_BEBEDOR} puntos gracias al bebestible {self.nombre}\n ")
            else:
                jugador.frustracion -= 10
                jugador.ego += 11
                print(
                f"\n{jugador.nombre} ha disminuido su frustracion en 10"
                f" y aumentado su ego en 11 puntos gracias al bebestible {self.nombre}\n ")

class Gaseosa(Bebestibles):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def consumir(self, jugador):
        energia_recuperada = randint(MIN_ENERGIA_BEBESTIBLE,MAX_ENERGIA_BEBESTIBLE)
        jugador.energia += energia_recuperada

        if jugador.personalidad == "Ludopata" or jugador.personalidad == "Tacano":
            jugador.frustracion -= 5
            jugador.ego += 6
            print(f"\n{jugador.nombre} ha aumentado su ego en 6 gracias al bebestible {self.nombre}\n")
            print(
            f"\n{jugador.nombre} ha disminuido 5 puntos de frustracion gracias al bebestible {self.nombre}\n")

        elif jugador.personalidad == "Bebedor" or jugador.personalidad == "Casual":

            if jugador.personalidad == "Bebedor":
                jugador.ego += 6*BONIFICACION_BEBEDOR
                jugador.frustracion += 5*BONIFICACION_BEBEDOR
                print("Aplicando bonificacion por bebedor frecuente... ")
                print(f"\n{jugador.nombre} ha aumentado su ego en {6*BONIFICACION_BEBEDOR} gracias al bebestible {self.nombre}\n ")
                print(
                f"\n{jugador.nombre} ha aumentado {5*BONIFICACION_BEBEDOR} puntos de frustracion gracias al bebestible {self.nombre}\n ")
            
            else:
                jugador.ego += 6
                jugador.frustracion += 5
                print(
                f"\n{jugador.nombre} ha aumentado 6 puntos de ego gracias al bebestible {self.nombre}\n")
                print(
                f"\n{jugador.nombre} ha aumentado 5 puntos de frustracion gracias al bebestible {self.nombre}\n")

class BrebajeMagico(Gaseosa, Jugo):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    def consumir(self, jugador):
        energia_recuperada = randint(MIN_ENERGIA_BEBESTIBLE,MAX_ENERGIA_BEBESTIBLE)
        jugador.energia += energia_recuperada
        Gaseosa.consumir(self,jugador)
        Jugo.consumir(self,jugador)
        if jugador.personalidad == "Bebedor":
            print("Aplicando bonificacion por cliente frecuente... ")
            jugador.carisma =+ 5*BONIFICACION_BEBEDOR
            print(
            f"\n{jugador.nombre} ha aumentado {5*BONIFICACION_BEBEDOR} puntos de carisma gracias al bebestible {self.nombre}\n ")
        else:
            jugador.carisma =+ 5
            print(
            f"\n{jugador.nombre} ha aumentado 5 puntos de carisma gracias al bebestible {self.nombre}\n ")

class Show:
    def ver_show(self, jugador):
        if jugador.dinero >= DINERO_SHOW:
            jugador.dinero -= DINERO_SHOW
            jugador.energia += ENERGIA_SHOW
            jugador.frustracion -= FRUSTRACION_SHOW
            print("Bienvenido al show nocturno! ")
            print("\n")
            print("*"*30)
            print("*"*30)
            print("\n")
            print("  Viendo show  ".center(30, "-"))
            print("\n")
            print("*"*30)
            print("*"*30)
            print("\n")
            print(f"{jugador.nombre} aumenta su energia y disminuye su frustracion en 10 y 6 ")
            print(f"Fin del show! Gracias por asistir. \n ")
        else:
            print("No posees el dinero suficiente ")

    
        


      




    

    



        


            



        





