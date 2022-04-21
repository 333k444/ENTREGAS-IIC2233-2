from collections import deque
from entidades import Cocinero, Mesero
from time import sleep
from random import randint


class Cocina:

    def __init__(self, bodega, recetas):
        super().__init__()
        self.cola_pedidos = deque()
        self.cola_pedidos_listos = deque()
        self.cocineros = []
        self.meseros = []
        self.bodega = bodega
        self.recetas = recetas
        self.abierta = True

    def initialize_threads(self):

        for cocinero in self.cocineros:
            cocinero.start()
        for mesero in self.meseros:
            mesero.start()
        
        # Completar
        pass

    def asignar_cocinero(self):
        while self.abierta:
            sleep(1)
            if len(self.cola_pedidos) > 0:
                for cocinero in self.cocineros:
                    if cocinero.disponible == True:
                        cocinero.evento_plato_asignado.set()

        # Completar
        pass

    def asignar_mesero(self):
        while self.abierta:
            sleep(1)
            if len(self.cola_pedidos) > 0:
                for mesero in self.meseros:
                    if mesero.disponible == True:
                        mesero.evento_manejar_pedido.set()
                        mesero.entregar_pedido(self)

        self.finalizar_jornada_laboral()
        # Completar
        pass

    def finalizar_jornada_laboral(self):
        for mesero in self.meseros:
            mesero.trabajando = False

        for cocinero in self.cocineros:
            cocinero.trabajando = False
