# Startup “Juegos por comida” 
# Codificación de clases con métodos constructores, accesadores, mutadores y sobrecarga en Python.
## Descripción

La startup Juegos por comida solicitó desarrollar el algoritmo de la primera escena de su próximo juego “Gran Fantasía”.
El prototipo se desarrolla utilizando una aplicación de consola escrita en Python.
Cuenta con un script principal que ejecuta el juego, y una clase que permite crear personajes,
y es importada en el script principal. Las opciones de juego del usuario, así como el
nombre de su personaje, se solicitan mediante input.

Es un juego de texto interactivo donde los jugadores asumen el papel de un personaje que se enfrenta a un orco en combates por experiencia y niveles. Los jugadores pueden elegir entre atacar o huir, y el resultado de cada enfrentamiento se determina por la experiencia y nivel de los personajes involucrados.

## Características
Sistema de Niveles y Experiencia: Los personajes ganan o pierden experiencia según el resultado de los combates, lo que afecta su nivel.

Interacción Dinámica: Los jugadores toman decisiones estratégicas que influyen en el desarrollo del juego.

Comparación de Personajes: Se implementan métodos para comparar la experiencia entre personajes y calcular probabilidades de ganar.

## Cómo Jugar
Ejecuta el juego y proporciona el nombre de tu personaje.
Enfréntate a un orco y elige entre atacar o huir.
Observa cómo tus decisiones afectan la experiencia y el nivel de tu personaje

El protopipo cuenta con dos archivos los cuales han sido provistos y se requiere
realizar  correcciones para correcto funcionamiento.

### 01 - personaje.py

### 02 - juego.py

## Prerrequisitos o Dependencias

Sistema Operativo Windows, Linux, MacOS
Lenguaje de programación Python 3.12

## Instalación del Proyecto

Clonar el repositorio:

```bash
# git@github.com:vanemn/clase5-modulo4-u2.git
```

Ingresar a la carpeta del proyecto:

```bash
# clase5-modulo4-u2
```

## Informe de errores

Al revisar el código entregado, este contenía una serie de errores que no permitían que el programa funcionara de forma optima al analizar se le hicieron las correcciones correspondiente para su correcto funcionamiento, a continuación se detallan las correcciones sugeridas.

Se agregan docstrings faltantes al proyecto, por lo tanto el detalle informado esta realizado con el conteo de lineas del proyecto original 

Se importa al archivo juego.py el modulo import os  para  poder limpiar la terminal donde el jugador ejecuta el juego para una mejor lectura.

### personaje.py 

#### Linea 6: La experiencia inicial del personaje debe ser 0 (estaba indicada como 10)

Antes 
```bash
self.experiencia = (
        10
    )
```
Ahora 
```bash
self.experiencia = 0 
```

#### Linea 10: Se corrige llamado de atributo EXP:{self.experiencia} antes estaba llamado como {self.nivel}

Antes 
```bash
 @property
    def estado(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.nivel}"
```
Ahora 
```bash
@property
    def estado(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}"
```

#### Linea 16: Se corrige condicion debe ser 99 (Sale como 100)
#### Linea 17: Correccion de nivel (debe sumar 1)

Antes 
```bash
while tmp_exp >= 100:
            self.nivel += (
                2
            )
            tmp_exp -= 90
```
Ahora 
```bash
while tmp_exp >= 99: 
            self.nivel += 1
            tmp_exp -= 90
```

#### Linea 23: Correccion de nivel (debe restar 1)
#### Linea 25:Correccion de exp (debe ser 0 al ser nivel 1)
Antes 
```bash
while tmp_exp < 0:
            if self.nivel > 1:
                tmp_exp = 100 + tmp_exp
                self.nivel -= (
                    2
                )
            else:
                tmp_exp = (
                    -1
                )
```
Ahora 
```bash
while tmp_exp < 0:
            if self.nivel > 1:
                tmp_exp = 100 + tmp_exp
                self.nivel -= 1 
            else:
                tmp_exp = 0 
```

#### Linea 45: Cambio de signos
#### Linea 49: Cambio de signos
#### Linea 54: Correccion de retorno

Antes 
```bash
def get_probabilidad_ganar(self, other):
        if self < other:
            return (
                0.66
            )
        elif self > other:
            return (
                0.33
            )
        else:
            return 0.75
```
Ahora 
```bash
def get_probabilidad_ganar(self, other):
        if self > other: 
            return (
                0.66
            )
        elif self < other: 
            return (
                0.33
            )
        else:
            return 0.5
```

#### Linea 62: Cerrar string de input
#### Linea 65: Correccion orden de opciones
#### Linea 66: Correccion orden de opciones
Antes 
```bash
@staticmethod
    def mostrar_dialogo_opcion(probabilidad_ganar):
        return int(
            input(
                f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100}% "
                "de probabilidades de perder contra el Orco.\n"
                "\nSi ganas, ganarás 30 puntos de experiencia y el orco perderá 50. \n
                "Si pierdes, perderás 50 puntos de experiencia y el orco ganará 30.\n"
                "\n¿Qué deseas hacer?\n"
                "1. Huir\n"
                "2. Atacar\n"
            )
        )
```
Ahora 
```bash
@staticmethod
    def mostrar_dialogo_opcion(probabilidad_ganar):
        return int(
            input(
                f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100}% "
                "de probabilidades de perder contra el Orco.\n"
                "\nSi ganas, ganarás 30 puntos de experiencia y el orco perderá 50. \n" 
                "Si pierdes, perderás 50 puntos de experiencia y el orco ganará 30.\n"
                "\n¿Qué deseas hacer?\n"
                "1. Atacar\n"
                "2. Huir\n"
            )
        )
```

### juego.py

#### Linea 1 y 2 : corregir importacion (Palabras mal escritas)

```bash
from persomaje import Personaje
import ramdon
```
Ahora 
```bash
from personaje import Personaje
import random 
```
#### Linea 4: Se cambia nombre del juego.
#### Linea 6: Se cambia nombre "orco" por "personaje"

Antes 
```bash
print("¡Bienvenido a Gran Realidad!")
nombre = input(
    "Por favor indique el nombre de su orco:\n"
)
```
Ahora 
```bash
print("¡Bienvenido a Gran Fantasía!")
nombre = input(
    "Por favor indique el nombre de su personaje:\n" 
)
```

#### Linea 13: Se cambia nombre "Elfo" por "Orco"
#### Linea 16-17: Se corrige llamado a metodo (o)
#### Linea 20: Se corrige llamado a metodo como o.mostrar_dialogo_opcion
Antes 
```bash
print(
    "\n¡Oh no!, ¡Ha aparecido un Elfo!"
)
o = Personaje("Orco")
probabilidad_ganar = p.get_probabilidad_ganar(
    p
)

opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)

```
Ahora 
```bash
print(
    "\n¡Oh no!, ¡Ha aparecido un Orco!" 
)
o = Personaje("Orco")
probabilidad_ganar = p.get_probabilidad_ganar(o) 

opcion_orco = o.mostrar_dialogo_opcion(probabilidad_ganar) 
```
#### Linea 24: Cerrar String cambiar signo
#### Linea 27: Se corrige condicion
#### Linea 30,32,33,38,40.41: se cambian los numeros invertidos 
#### Linea 44: Corregir print de estado

Antes 
```bash
while opcion_orco == 1:
    resultado = (
        "G" if random.uniform(0, 1) > probabilidad_ganar else "P
    )

    if resultado == "P":
        print(
            "\n¡Le has ganado al orco, felicidades!\n"
            "¡Recibirás 30 puntos de experiencia!\n"
        )
        p.estado = -30
        o.estado = 50

    else:
        print(
            "\n¡Oh no! ¡El orco te ha ganado!\n"
            "¡Has perdido 50 puntos de experiencia!\n"
        )
        p.estado = 50
        o.estado = -30

    print(p.estado)
    primt(o.estado)
```
Ahora 
```bash
while opcion_orco == 1:
    resultado = (
        "G" if random.uniform(0, 1) >= probabilidad_ganar else "P" )

    if resultado == "G": 
        print(
            "\n¡Le has ganado al orco, felicidades!\n"
            "¡Recibirás 50 puntos de experiencia!\n" )

        p.estado = 50
        o.estado = -30 
        os.system("cls") 

    else:
        print(
            "\n¡Oh no! ¡El orco te ha ganado!\n"
            "¡Has perdido 30 puntos de experiencia!\n" 
        )
        p.estado = -30 
        o.estado = 50 
        os.system("cls") 

    print(p.estado)
    print(o.estado)
```
#### Linea 46,47: Se corrige llamado a metodo en ambos 
Antes
```bash
    probabilidad_ganar = p.get_probabilidad_ganar(0)
    opcion_orco = Personaje.mostrar_dialogo_opcion(provabilidad_ganar)
```

Ahora 
```bash
    probabilidad_ganar = p.get_probabilidad_ganar(o)  
    opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar)
```

Autor

- [Vanessa Morales](https://github.com/vanemn)
- [Benjamín Pardo](https://github.com/bpardo02)
- [Nicole Pinilla](https://github.com/Npinilla19)
