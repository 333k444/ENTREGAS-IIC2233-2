from parametros import (AFINIDAD_HIT, AFINIDAD_INICIAL, AFINIDAD_PUBLICO_POP,
                        AFINIDAD_STAFF_POP, AFINIDAD_PUBLICO_ROCK,
                        AFINIDAD_STAFF_ROCK, AFINIDAD_PUBLICO_RAP,
                        AFINIDAD_STAFF_RAP, AFINIDAD_PUBLICO_REG,
                        AFINIDAD_STAFF_REG, AFINIDAD_ACCION_POP,
                        AFINIDAD_ACCION_ROCK, AFINIDAD_ACCION_RAP,
                        AFINIDAD_ACCION_REG, AFINIDAD_MIN, AFINIDAD_MAX)


class Artista:
    def __init__(self, nombre, genero, dia_presentacion,
                 hit_del_momento):
        self.nombre = nombre
        self.hit_del_momento = hit_del_momento
        self.genero = genero
        self.dia_presentacion = dia_presentacion
        self._afinidad_con_publico = AFINIDAD_INICIAL
        self._afinidad_con_staff = AFINIDAD_INICIAL

    @property
    def afinidad_con_publico(self):
        return self.__afinidad_con_publico
        # COMPLETAR
        pass
    
    @afinidad_con_publico.setter
    def afinidad_con_publico(self,value):
        if value > 100 or value < 0:
            raise ValueError("El valor de afinidad con el publico no es valido")
        else:
            self.__afinidad_con_publico = value


    @property
    def afinidad_con_staff(self):
        return self.__afinidad_con_staff
        # COMPLETAR
        pass

    @afinidad_con_staff.setter
    def afinidad_con_staff(self,value):
        if value > 100 or value < 0:
            raise ValueError("El valor de afinidad con el publico no es valido")
        else:
            self.__afinidad_con_staff = value

    @property
    def animo(self):
        ponderacion = (self.afinidad_con_publico*0.5)+(self.afinidad_con_staff*0.5)
        return ponderacion
        pass

    # @animo.setter
    # def afinidad_con_publico(self,value):
    #     value = (self.afinidad_con_publico * 0.5) + (self.afinidad_con_staff * 0.5)
        


    def recibir_suministros(self, suministro):

        valor = suministro.valor_de_satisfaccion
        if valor == 1:
            
        # COMPLETAR
        pass

    def cantar_hit(self):
        # COMPLETAR
        pass

    def __str__(self):
        # COMPLETAR
        pass


class ArtistaPop:
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass

    def accion_especial(self):
        # COMPLETAR
        pass

    def animo(self):
        # COMPLETAR
        pass


class ArtistaRock:
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass

    def accion_especial(self):
        # COMPLETAR
        pass

    def animo(self):
        # COMPLETAR
        pass


class ArtistaRap:
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass

    def accion_especial(self):
        # COMPLETAR
        pass

    def animo(self):
        # COMPLETAR
        pass


class ArtistaReggaeton:
    def __init__(self, *args, **kwargs):
        # COMPLETAR
        pass

    def accion_especial(self):
        # COMPLETAR
        pass

    def animo(self):
        # COMPLETAR
        pass
