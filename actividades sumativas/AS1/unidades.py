from abc import ABC, abstractmethod
from parametros import PROB_REVIVIR, PROB_CRITICO_GUERRERO, \
                    PROB_CRITICO_MAGO, PROB_CRITICO_MAGO_GUERRERO
import random
import math


# Recuerda que es una clase abstracta
class Persona(ABC):

    def __init__(self, xp, stamina, **kwargs):
        # No modificar
        super().__init__(**kwargs)
        self.xp = xp
        self.stamina = stamina
        self.asignar_parametros()

    @property
    def stamina(self):
        # No modificar
        return self._stamina

    @stamina.setter
    def stamina(self, value):
        # No modificar
        if value <= 0:
            if not self.revivir():
                print("F")
        else:
            self._stamina = value

    def revivir(self):
        # No modificar
        if PROB_REVIVIR > random.random():
            self.stamina += 3
            return True
        else:
            return False

    # ---------------
    @abstractmethod
    def asignar_parametros(self):
        pass


    @abstractmethod
    def accion(self):
        pass
    

    @abstractmethod
    def __str__(self):
        pass
    # Completar los métodos abstractos aquí

    # ---------------


# Recuerda completar la herencia
class Guerrero(Persona):

    def __init__(self, armado, **kwargs):
        self.armado = armado
        super().__init__(**kwargs)
        # Completar
        pass

    # ---------------
    def asignar_parametros(self):
        pond = 5*(math.pi)*(self.xp)*(1/2)

        self.ataque = round(pond)
        if self.armado == True:
            self.ataque = self.ataque*2        
    
    def accion(self):
        probabilidad = random.random()
        if probabilidad < PROB_CRITICO_GUERRERO:
            return round(1.5*self.ataque)
        else:
            return self.ataque

    def __str__(self):

        if self.armado == True:
            return f'Guerrero Armado con {self.ataque} pts de ataque'
        else:
            return f'Guerrero con {self.ataque} pts de ataque'

    # ---------------


# Recuerda completar la herencia
class Mago(Persona):

    def __init__(self, bendito, **kwargs):
        self.bendito = bendito
        super().__init__(**kwargs)

        # Completar
        pass

    # ---------------
    def asignar_parametros(self):
        pond = 1.618*(math.pi)*(self.xp)*(1/2)

        self.curacion = round(pond)
        if self.bendito == True:
            self.curacion = self.curacion*2        
    
    def accion(self):
        probabilidad = random.random()
        if probabilidad < PROB_CRITICO_MAGO:
            return round(1.5*self.curacion)
        else:
            return self.curacion

    def __str__(self):

        if self.bendito == True:
            return f'Mago BENDITO con {self.curacion} pts de curación'
        else:
            return f'Mago con {self.curacion} pts de curación'

    # ---------------


# Recuerda completar la herencia
class MagoGuerrero(Mago, Guerrero):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Completar
        pass

    # ---------------
    def asignar_parametros(self):

        Mago.asignar_parametros(self)
        Guerrero.asignar_parametros(self)
        
    def accion(self):

        tupla_a_c = (self.ataque,self.curacion)
        return tupla_a_c

    # ---------------

    def __str__(self):
        # No modificar
        if self.armado and self.bendito:
            return f"MagoGuerrero BENDITO y ARMADO con {self.curacion}" \
                   + f" pts de curación y {self.ataque} pts de ataque."
        else:
            return f"MagoGuerrero con {self.curacion} pts de curación" \
                + f" y {self.ataque} pts de ataque."


if __name__ == "__main__":
    # ---------------
    # En esta sección puedes probar tu codigo
    # ---------------
    pass


#129 DUDAS
#141 DUDAS