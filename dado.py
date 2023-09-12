import random
import time
def obtener_numero_aleatorio():
    return random.randint(1, 6)

if __name__=="__main__":
    numero = obtener_numero_aleatorio()
    print("El numero aleatorio es ... ")
    time.sleep(1)
    print("Cargando numero ...")
    time.sleep(3)
    print("Es el ",obtener_numero_aleatorio())