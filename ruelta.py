import random
import time

def ruelta_casino():
    opciones = [i for i in range(37)]
    colores = ['rojo, par' if (i > 0 and i % 2 == 0) else 'negro, impar' if (i > 0 and i % 2 == 1) else 'verde' for i in opciones]
    resultado = random.choice(opciones)
    color = colores[resultado]
    return resultado, color


print(" ¡¡¡ Bienvenido a la ruleta de la suerte del casino !!! ")
input("Presiona el 'ENTER' para girar la ruleta.\n ¡¡¡ Suerte !!!")
print(" No va más ")
time.sleep(5)
resultado, color = ruelta_casino()
print(f"El resultado es el numero {resultado} {color} y pasa.")
