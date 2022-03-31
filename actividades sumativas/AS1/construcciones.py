from abc import ABC, abstractmethod
from random import choice, randint, random
import re
from unidades import Guerrero, Mago, MagoGuerrero
from parametros import PROB_CRITICO_MURO, PROB_CRITICO_CATAPULTA, \
                       HP_MUROCATAPULTA, PROB_CRITICO_MURO_CATAPULTA, \
                       HP_BARRACAS, HP_MURO, HP_CATAPULTA


# Recuerda que es una clase abstracta
class Estructura(ABC):

    def __init__(self, edad, *args,**kwargs):
        # No modificar
        super().__init__(*args)
        self.edad = edad
        self.asignar_atributos_segun_edad()

    # ---------------

    @abstractmethod
    def asignar_atributos_segun_edad():
        pass

    @abstractmethod
    def accion(self):
        pass

    @abstractmethod
    def avanzar_edad(self):
        pass

    # ---------------


# Recuerda completar la herencia
class Barracas(Estructura):
    def __init__(self, *args):
        self.hp = HP_BARRACAS
        super().__init__(*args)
        # Completar
        pass

    # ---------------
    def asignar_atributos_segun_edad(self):
        if self.edad == "Media":
            self.unidades = ["Mago","Guerrero"]
        else:
            self.unidades = ["Mago","Guerrero","MagoGuerrero"]
        pass

    def avanzar_edad(self):
        if self.edad == "Media":
            self.edad = "Moderna"
            self.unidades.append("MagoGuerrero")

    
    # ---------------

    def accion(self):
        # No modificar
        elegido = choice(self.unidades)
        suerte = choice((True, False))
        experiencia = choice([1, 2, 3, 4, 5, 6])
        energia = choice([1, 2, 3, 4, 5, 6])
        if elegido == "Guerrero":
            return elegido, Guerrero(suerte, xp=experiencia, stamina=energia)
        elif elegido == "Mago":
            return elegido, Mago(suerte, xp=experiencia, stamina=energia)
        elif elegido == "MagoGuerrero":
            atributos = {"bendito": suerte, "armado": suerte, "xp": experiencia,
                         "stamina": energia}
            return elegido, MagoGuerrero(**atributos)


# Recuerda completar la herencia
class Muro(Estructura):

    def __init__(self, *args):
        self.hp = HP_MURO
        super().__init__(*args)
        # Completar
        pass

    # ---------------
    def asignar_atributos_segun_edad(self):
        if self.edad == "Media":
            self.reparacion = [20,80]
        else:
            self.reparacion = [40,100]
        pass

    def accion(self):

        probabilidad = random()
        reparacion = randint(self.reparacion[0],self.reparacion[1])
        if probabilidad < PROB_CRITICO_MURO:
            return reparacion*2
        else:
            return reparacion


    def avanzar_edad(self):
        if self.edad == "Media":
            self.edad = "Moderna"
            self.reparacion = [40,100]

    # ---------------


# Recuerda completar la herencia
class Catapulta(Estructura):

    def __init__(self, *args):
        self.hp = HP_CATAPULTA
        super().__init__(*args)
        # Completar
        pass

    # ---------------

    def asignar_atributos_segun_edad(self):
        if self.edad == "Media":
            self.ataque = [40,100]
        else:
            self.ataque = [80,140]
        pass

    def accion(self):

        probabilidad = random()
        ataque = randint(self.ataque[0],self.ataque[1])
        if probabilidad < PROB_CRITICO_CATAPULTA:
            return ataque*2
        else:
            return ataque


    def avanzar_edad(self):
        if self.edad == "Media":
            self.edad = "Moderna"
            self.ataque = [80,140]

    # ---------------

# Recuerda completar la herencia
class MuroCatapulta(Muro, Catapulta):

    def __init__(self, *args):
        self.hp = HP_MUROCATAPULTA
        super().__init__(*args)
        # Completar
        pass

    # ---------------
    def asignar_atributos_segun_edad(self):

        Muro.asignar_atributos_segun_edad(self)
        Catapulta.asignar_atributos_segun_edad(self)

    def accion(self):
        reparacion = randint(self.reparacion[0],self.reparacion[1])
        ataque = randint(self.ataque[0],self.ataque[1])
        probabilidad = random()
        if probabilidad < PROB_CRITICO_MURO_CATAPULTA:
            return (round(reparacion*2.5), round(ataque*2.5))
        else:
            return (round(reparacion),round(ataque))

    def avanzar_edad(self):
        if self.edad == "Media":
            self.edad = "Moderna"
            self.reparacion = [40,100]
            self.ataque = [80,140]
        
    # ---------------


if __name__ == "__main__":
    # ---------------
    # En esta sección puedes probar tu codigo
    # ---------------
    pass
