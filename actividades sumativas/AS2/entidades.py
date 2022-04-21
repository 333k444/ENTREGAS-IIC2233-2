from abc import ABC, abstractmethod
from random import randint
from threading import Thread, Lock, Event, Timer
from time import sleep


class Persona(ABC, Thread):

    # Completar
    lock_bodega = Lock()
    lock_cola_pedidos = Lock()
    lock_cola_pedidos_listos = Lock()

    def __init__(self, nombre):
        super().__init__()
        self.nombre = nombre
        self.disponible = True
        self.trabajando = True
        self.daemon = True

    @abstractmethod
    def run(self):
        pass


class Cocinero(Persona):

    def __init__(self, nombre, cocina):
        super().__init__(nombre)
        self.lugar_trabajo = cocina
        # Completar
        self.evento_plato_asignado = Event()

    def run(self):
        while self.trabajando:
            self.evento_plato_asignado.wait()
            sleep(randint(1, 3))
            self.cocinar()

        # Completar
        pass

    def cocinar(self):
        self.disponible = False
        plato = self.sacar_plato()
        print(f"El cocinero {self.nombre} esta tabajando en el plato {plato[1]}... ")
        self.buscar_ingredientes(plato, self.lugar_trabajo.bodega, self.lugar_trabajo.recetas)
        sleep(randint(1, 3))
        self.agregar_plato(plato)
        self.evento_plato_asignado.clear()
        self.disponible = True
        # Completar
        pass

    def sacar_plato(self):
        with self.lock_cola_pedidos:
            primer_pedido = self.lugar_trabajo.cola_pedidos.popleft()
            return primer_pedido
        # Completar
        pass

    def buscar_ingredientes(self, plato, bodega, recetas):
        with self.lock_bodega:
        # Formato de los dicts entregados:
        # bodega = {
        #     "alimento_1": int cantidad_alimento_1,
        #     "alimento_2": int cantidad_alimento_2,
        # }
        # recetas = {
        #     "nombre_plato_1": [("ingrediente_1", "cantidad_ingrediente_1"),
        #                        ("ingrediente_2", "cantidad_ingrediente_2")],
        #     "nombre_plato_2": [("ingrediente_1", "cantidad_ingrediente_1"), 
        #                        ("ingrediente_2", "cantidad_ingrediente_2")]
        # }

        # Completar
            print(f"El cocinero {self.nombre} esta buscando ingredientes para {plato[1]}... ")
            ingredientes_necesarios = recetas[plato[1]]
            for tupla in ingredientes_necesarios:
                bodega[tupla[0]] -= int(tupla[1])

        pass

    def agregar_plato(self, plato):
        with self.lock_cola_pedidos_listos:

            self.lugar_trabajo.cola_pedidos_listos.append(plato)

        # Completar
        pass


class Mesero(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)
        self.evento_manejar_pedido = Event()
        # Completar

    def run(self):
        while self.trabajando:
            self.evento_manejar_pedido.set()
        # Completar
        pass

    def agregar_pedido(self, pedido, cocina):
        with self.lock_cola_pedidos:
            self.evento_manejar_pedido.clear()
            sleep(randint(1, 2))

            cocina.cola_pedidos.append(pedido)
            self.evento_manejar_pedido.set()

        # Completar
        pass

    def entregar_pedido(self, cocina):
        with self.lock_cola_pedidos_listos:
            self.evento_manejar_pedido.clear()
            sleep(randint(1, 3))
            pedido_listo = cocina.cola_pedidos_listos.popleft()
            self.pedido_entregado(pedido_listo)
            print(f"El mesero {self.nombre} va a entregar un pedido a la mesa {pedido_listo[0]}")
        # Completar
        pass

    def pedido_entregado(self, pedido):
        print(f"El plato {pedido[1]} fue entregado a la mesa {pedido[0]}! ")
        self.evento_manejar_pedido.set()
        # Completar
        pass
