# Tarea 0: DCCorreos :school_satchel:


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
#### Menú de Inicio (18pts) (18%)
##### ✅ Requisitos <explicacion\ Cumple con los requisitos. >
##### ✅ Iniciar sesión <explicacion\ Consta de dos funciones, autentificar_usuario y autentificar_contrasena.Ambas revisan el archivo users para verificar que el usuario este registrado>
##### ✅ Ingresar como administrador <explicacion\ Se verifica que la clave sea identica al parametro CONTRASENA_ADMIN>
##### ✅ Registrar usuario <explicacion\ Consta de una funcion registrar_usuario que verifica que el nombre sea valido y unico. Al igual que la contraseña>
##### ✅ Salir <explicacion\>
#### Flujo del programa (31pts) (31%) 
##### ✅ Menú de Usuario <explicacion\ Consta de una funcion menu_usuario que se encarga que se desplieguen 5 opciones a elegir despues de iniciar sesion o registrarse como usuario>
##### ✅ Menú de Administrador <explicacion\ Consta de una funcion menu_administrador que se encarga que se desplieguen 3 opciones a elegir despues de iniciar sesion como administrador>
#### Entidades 15pts (15%)
##### ✅ Usuarios <explicacion\ Almacenados en usuarios.csv. Se agrega al final del archivo cuando se llama a la funcion registrar_usuario >
##### ✅ Encomiendas <explicacion\ Almacenadas en encomiendas.csv. Se agrega al final del archivo una nueva cuando se llama a la funcion ingresar_encomienda.>
##### ✅ Reclamos <explicacion\ Almacenadas en encomiendasc.csv. Se agrega al final del archivo un reclamo nuevo cuando se llama a la funcion realizar_reclamo.>
#### Archivos: 15 pts (15%)
##### 🟠 Manejo de Archivos <explicacion\ Mi manejo en el uso de archivos (tanto en write, read o append) no fue el optimo.
>
#### General: 21 pts (21%)
##### ✅ Menús <explicacion\ Funciona con fluidez. Para cada opcion que elige el usuario se llama a una funcion determinada. Al terminar la funcion se ofrece volver al menu inicial>
##### ✅ Parámetros <explicacion\ Utilice los parametros dados.>
##### ✅ Módulos <explicacion\ Importe lo justo y necesario. Date, Datetime para poder registrar la fecha exacta cuando se hace una encomienda.>
##### 🟠 PEP8 <explicacion\ Mi estilo de programacion no fue el mas eficiente ni el mas bonito para esta entrega. Me costo aflojar la mano y sentirme comodo programando algo tan largo>
## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. 

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```libreria_1```: ```función(datetime) / datetime```
2. ```librería_2```: ```función(date) / datetime``` 
3. ...

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```funciones```,contiene funciones para la funcionalidad del programa.

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:


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
1. \<link stackoverflow.com>:  y está implementado en el archivo <funciones> en las líneas <número 124> y hace que que obtenga la fecha actual.



## Descuentos
La guía de descuentos se encuentra [link](https://github.com/IIC2233/syllabus/blob/main/Tareas/Descuentos.md).
