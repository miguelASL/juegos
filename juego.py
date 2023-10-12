import random
import tkinter as tk

# Función para jugar
def jugar():
    opciones = ['piedra', 'papel', 'tijera']
    
    seleccion_usuario = seleccion.get()
    seleccion_ordenador = random.choice(opciones)
    
    if seleccion_usuario == seleccion_ordenador:
        resultado.set("Empate")
    elif ganar(seleccion_usuario, seleccion_ordenador):
        resultado.set("¡Has ganado!")
    else:
        resultado.set("Has perdido :(")

# Función para determinar el ganador
def ganar(jugador, oponente):
    if (jugador == 'piedra' and oponente == 'tijera') or (jugador == 'tijera' and oponente == 'papel') or (jugador == 'papel' and oponente == 'piedra'):
        return True
    else:
        return False

# Crear ventana
ventana = tk.Tk()
ventana.title("Piedra, papel o tijeras")

# Crear etiqueta de selección
etiqueta_seleccion = tk.Label(ventana, text="Selecciona una opción:")
etiqueta_seleccion.pack()

# Crear variable de selección
seleccion = tk.StringVar()

# Crear botones de selección
boton_piedra = tk.Radiobutton(ventana, text="Piedra", variable=seleccion, value="piedra")
boton_piedra.pack()

boton_papel = tk.Radiobutton(ventana, text="Papel", variable=seleccion, value="papel")
boton_papel.pack()

boton_tijera = tk.Radiobutton(ventana, text="Tijera", variable=seleccion, value="tijera")
boton_tijera.pack()

# Crear botón de jugar
boton_jugar = tk.Button(ventana, text="Jugar", command=jugar)
boton_jugar.pack()

# Crear etiqueta de resultado
resultado = tk.StringVar()
etiqueta_resultado_titulo = tk.Label(ventana, text="Resultado:")
etiqueta_resultado_titulo.pack()
etiqueta_resultado = tk.Label(ventana, textvariable=resultado)
etiqueta_resultado.pack()

# Crear botón de salir
boton_salir = tk.Button(ventana, text="Salir", command=ventana.quit)
boton_salir.pack()

# Iniciar ventana
ventana.mainloop()