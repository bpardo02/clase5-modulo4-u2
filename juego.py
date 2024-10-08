"""  
Este script implementa un juego simple llamado "Gran Fantasía",   
donde el jugador crea un personaje y se enfrenta a un orco.   
El juego calcula la probabilidad de ganar y permite al jugador   
decidir si atacar o huir, mostrando los resultados de cada combate.  
"""
from personaje import Personaje # corregir importacion
import random # Corregir importacion
import os # importar os

print("¡Bienvenido a Gran Fantasía!")
nombre = input(
    "Por favor indique el nombre de su personaje:\n" # Cambiar orco por personaje
)

p = Personaje(nombre)
print(p.estado)

print(
    "\n¡Oh no!, ¡Ha aparecido un Orco!" # Corregir mensaje
)
o = Personaje("Orco")
probabilidad_ganar = p.get_probabilidad_ganar(o) # Corregir llamado a metodo

opcion_orco = o.mostrar_dialogo_opcion(probabilidad_ganar) # Corregir llamado

while opcion_orco == 1:
    resultado = (
        "G" if random.uniform(0, 1) >= probabilidad_ganar else "P" # Cerrar String cambiar signo
    )

    if resultado == "G": # Corregir condicion
        print(
            "\n¡Le has ganado al orco, felicidades!\n"
            "¡Recibirás 50 puntos de experiencia!\n" # Corregir mensaje
        )
        p.estado = 50 # Correccion numeros
        o.estado = -30 # Correccion numeros
        os.system("cls") # Limpiar pantalla

    else:
        print(
            "\n¡Oh no! ¡El orco te ha ganado!\n"
            "¡Has perdido 30 puntos de experiencia!\n" # Correccion print
        )
        p.estado = -30 # Correccion numeros
        o.estado = 50 # Correccion numeros
        os.system("cls") # Limpiar pantalla

    
    print(p.estado)
    print(o.estado) # Corregir print de estado

   
    probabilidad_ganar = p.get_probabilidad_ganar(o) # Corregir llamado a metodo    
    opcion_orco = Personaje.mostrar_dialogo_opcion(probabilidad_ganar) # Corregir llamado a metodo

    
if opcion_orco == 2:
    print(
        "\n¡Has decidido huir del orco!\n"
        "¡Hasta la próxima aventura!\n"
    )
   
    
