# Tarea X: Nombre de la tarea :school_satchel:


Un buen ```README.md``` puede marcar una gran diferencia en la facilidad con la que corregimos una tarea, y consecuentemente cómo funciona su programa, por lo en general, entre más ordenado y limpio sea éste, mejor será 

Para nuestra suerte, GitHub soporta el formato [MarkDown](https://es.wikipedia.org/wiki/Markdown), el cual permite utilizar una amplia variedad de estilos de texto, tanto para resaltar cosas importantes como para separar ideas o poner código de manera ordenada ([pueden ver casi todas las funcionalidades que incluye aquí](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet))

Un buen ```README.md``` no tiene por que ser muy extenso tampoco, hay que ser **concisos** (a menos que lo consideren necesario) pero **tampoco pueden** faltar cosas. Lo importante es que sea claro y limpio 

**Dejar claro lo que NO pudieron implementar y lo que no funciona a la perfección. Esto puede sonar innecesario pero permite que el ayudante se enfoque en lo que sí podría subir su puntaje.**

## Consideraciones generales :octocat:

<Descripción de lo que hace y que **_no_** hace la tarea que entregaron junto
con detalles de último minuto y consideraciones como por ejemplo cambiar algo
en cierta línea del código o comentar una función>

### Cosas implementadas y no implementadas :white_check_mark: :x:

Explicación: mantén el emoji correspondiente, de manera honesta, para cada item. Si quieres, también puedes agregarlos a los títulos:
- ❌ si **NO** completaste lo pedido
- ✅ si completaste **correctamente** lo pedido
- 🟠 si el item está **incompleto** o tiene algunos errores

**⚠️⚠️NO BASTA CON SOLO PONER EL COLOR DE LO IMPLEMENTADO**,
SINO QUE SE DEBERÁ EXPLICAR QUÉ SE REALIZO DETALLADAMENTE EN CADA ITEM.
⚠️⚠️
#### Programación Orientada a Objetos: 38 pts (28%)
##### ✅  Diagrama <explicacion\ Diagrama hecho en draw.io el cual cumple con el detalle de las clases y sus relaciones.>
##### ✅ Definición de clases, atributos, métodos y properties <explicacion\ Se utilizaron properties en la clase Jugador para que encapsular los atributos que no quiero que se modifiquen afuera del programa, ademas de establecer su rango valido de valores. >
##### ✅ Relaciones entre clases <explicacion\ La clase jugador tiene 4 subclases, la clase bebestible tiene 3 subclases. >
#### Simulaciones: 10 pts (7%)
##### ✅ Crear partida <explicacion\ Se creo una instancia de la clase Menus y se llamo al metodo menu_de_inicio(), el cual se encarga de desplegar las opciones del primer menu, y en base a eso, llamar a la funcion correspondiente.>
#### Acciones: 35 pts (26%)
##### ✅ Jugador <explicacion\ Es una clase abstracta la cual tiene como metodo abstracto apostar(). Este metodo es heredado por las subclases de Jugador. Tambien, cada subclase de jugador tiene un metodo de su accion especial, la cual se llama despues del metodo apostar en funcion si gano la apuesta. La subclase bebedor es la unica que no cuenta con la funcion de accion especial, dado que esta ejecuta en el metodo consumir de Bebedor.>
##### ✅ Juego <explicacion\ El metodo probabilidad_de_ganar genera la probabilidad de ganar que tiene el jugador, para posteriormente pasarle el valor a la funcion entregar_resultados, la cual se encarga de verificar si el jugador gana o pierde, y aplicar las consecuencias correspondientes. >
##### ✅ Bebestible <explicacion\ Es una clase abstracta la cual tiene el metodo abstracto consumir, el cual recibe el objeto jugador y le suma los atributos correspondientes en funcion del bebestible consumido. Si el jugador es bebedor, los atributos adquiridos son mulitplicados por el parametros BONIFICAICON_BEBEDOR.>
##### ✅ Casino <explicacion\ Es una clase la cual almacena los datos generales. Fue usada para consultar los bebestibles o los juegos como objetos. Ademas, posee el metodo jugar y el metodo evento especial. El metodo jugar llama al metodo apostar para iniciar una apuesta. El metodo evento especial se llama cuando se sabe el resultado de un juego, y escoge mediante un choice() un bebestible al azar de la lista de bebestibles.>
#### Consola: 41 pts (30%)
##### ✅ Menú de Inicio <explicacion\ Si la opcion es 1, se llama al menu de opciones de jugador. Si es X se cierra el programa. >
##### ✅ Opciones de jugador <explicacion\ Se muestran todos los jugadores, los cuales, si son elegidos, se crea su respectiva instancia en la clase Jugador()>
##### ✅ Menú principal <explicacion\ Se muetran las opciones de menu principal, las cuales dependiendo de la eleccion del usuario, se llaman a los metodos correspondientes>
##### ✅ Opciones de juegos <explicacion\ Se muestran las opciones de cada uno de los juegos disponibles para jugar. Al elegir uno se llama el metodo Jugar() de Casino.>
##### ✅ Carta de bebestibles <explicacion\ Se muestran las opciones de cada uno de los bebestibles disponibles para consumir. Al elegir uno se llama el metodo consumir() de Bebestible.>
##### ✅ Ver estado del Jugador <explicacion\ Se muestran todos los atributos del jugador el cual ingreso sesion.>
##### ✅ Robustez <explicacion\ Los menus son a prueba de errores, no se caen con ningun valor ingresado por el usuario. >
#### Manejo de archivos: 13 pts (9%)
##### ✅ Archivos CSV  <explicacion\ Se crearon funciones para leer cada uno de los archivos y guardarlos y convertirlos en una lista de listas.>
##### ✅ parametros.py <explicacion\ Se creo un archivo con todos los parametros, los cuales fueron importados para su uso.>
#### Bonus: 3 décimas máximo
##### ✅ Ver Show <explicacion\ Se puso una opcion adicional en el menu principal, la cual se llama Ver Show. Al ingresar esta opcion, se instancia la clase Show y se llama el metodo ver_show(), el cual recibe un objeto jugador y se encarga de hacer prints y agregarle a jugador los atributos correspondientes. >
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Además se debe crear los siguientes archivos y directorios adicionales:
1. ```archivo.ext``` en ```ubicación```
2. ```directorio``` en ```ubicación```
3. ...


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```librería_1```: ```random() / random, randint, choice```
2. ```librería_2```: ```tabulate() / tabulate``` (se debe instalar)
3. ```librería_3```: ```abc() / ABC, abstractmethod```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```entidades```: Contiene a todas las entidades del programa.
2. ```parametros```: Hecha para <insertar crear los parametros del programa>
3. ...

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. <Descripción/consideración 1 y justificación del por qué es válido/a> 
2. <Descripción/consideración 2 y justificación del por qué es válido/a>
3. ...

PD: <una última consideración (de ser necesaria) o comentario hecho anteriormente que se quiera **recalcar**>


-------



**EXTRA:** si van a explicar qué hace específicamente un método, no lo coloquen en el README mismo. Pueden hacerlo directamente comentando el método en su archivo. Por ejemplo:

```python
class Corrector:

    def __init__(self):
          pass

    # Este método coloca un 6 en las tareas que recibe
    def corregir(self, tarea):
        tarea.nota  = 6
        return tarea
```

Si quieren ser más formales, pueden usar alguna convención de documentación. Google tiene la suya, Python tiene otra y hay muchas más. La de Python es la [PEP287, conocida como reST](https://www.python.org/dev/peps/pep-0287/). Lo más básico es documentar así:

```python
def funcion(argumento):
    """
    Mi función hace X con el argumento
    """
    return argumento_modificado
```
Lo importante es que expliquen qué hace la función y que si saben que alguna parte puede quedar complicada de entender o tienen alguna función mágica usen los comentarios/documentación para que el ayudante entienda sus intenciones.

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
