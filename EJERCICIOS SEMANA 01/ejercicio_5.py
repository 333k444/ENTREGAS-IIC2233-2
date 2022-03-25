from random import choice, randint
from collections import namedtuple, defaultdict # Puedes usar defaultdict si lo deseas


paises = ['Argentina', 'Bolivia', 'Chile', 'Perú']
Persona = namedtuple('Persona', 'edad nacionalidad')

personas = []
for i in range(100):
    nueva_persona = Persona(randint(0, 100), choice(paises))
    personas.append(nueva_persona)

print(personas)


personas_por_nacionalidad = {}
for i in range(len(personas)):
    personas_por_nacionalidad(        )                

# Completa