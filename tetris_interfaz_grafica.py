import tkinter as tk
import random

# Constantes para el tamaño del tablero
TABLERO_ANCHO = 10
TABLERO_ALTO = 20
TAMANO_CUADRO = 30
TIEMPO_CAIDA_PIEZA = 500  # 0.5 segundos en milisegundos

# Colores de las piezas
COLORES_PIEZAS = ["blue", "orange", "green", "red", "purple"]

class TetrisGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tetris creado por Miguel Sarmiento")
        self.canvas = tk.Canvas(root, width=TABLERO_ANCHO * TAMANO_CUADRO, height=TABLERO_ALTO * TAMANO_CUADRO, bg="pink")
        self.canvas.pack()
        self.lineas_eliminadas = 0

        self.tablero = [[0] * TABLERO_ANCHO for _ in range(TABLERO_ALTO)]
        self.pieza_actual = None
        self.juego_terminado = False

        self.root.bind("<Left>", self.mover_izquierda)
        self.root.bind("<Right>", self.mover_derecha)
        self.root.bind("<Down>", self.mover_abajo)
        self.root.bind("<Up>", self.rotar_pieza)
        
        # Comenzar el temporizador de caída automática de la pieza
        self.iniciar_temporizador()
        

    def crear_pieza(self):
        # Generar una pieza aleatoria
        self.pieza_actual = Pieza(random.choice(COLORES_PIEZAS))
        self.pieza_actual.x = TABLERO_ANCHO // 2 - 1
        self.pieza_actual.y = 0

    def mover_pieza(self, dx, dy):
        if self.pieza_actual and not self.juego_terminado:
            if self.pieza_actual.puede_moverse(self.tablero, dx, dy):
                self.pieza_actual.mover(dx, dy)
                self.dibujar()
            else:
                # Si la ficha no puede moverse más abajo, fijarla al tablero
                self.fijar_pieza()
                lineas_eliminadas = self.eliminar_filas_completas()
                self.lineas_eliminadas += lineas_eliminadas
                self.crear_pieza()
                if not self.pieza_actual.puede_moverse(self.tablero, 0, 0):
                    self.juego_terminado = True
                    self.mostrar_mensaje_final(f"¡ Has perdido ! 😢!")

    def mover_izquierda(self, event):
        self.mover_pieza(-1, 0)

    def mover_derecha(self, event):
        self.mover_pieza(1, 0)

    def mover_abajo(self, event):
        self.mover_pieza(0, 1)

    def rotar_pieza(self, event):
        if self.pieza_actual:
            if self.pieza_actual.puede_rotar(self.tablero):
                self.pieza_actual.rotar()
                self.dibujar()

    def iniciar_temporizador(self):
        # Crear una nueva pieza automáticamente cada 0.5 segundos
        self.crear_pieza()
        self.dibujar()
        self.root.after(TIEMPO_CAIDA_PIEZA, self.caer_pieza)

    def caer_pieza(self):
        # Hacer que la pieza caiga automáticamente
        self.mover_pieza(0, 1)
        if not self.juego_terminado:
            self.root.after(TIEMPO_CAIDA_PIEZA, self.caer_pieza)

    def fijar_pieza(self):
        for x, y in self.pieza_actual.coordenadas():
            self.tablero[y][x] = self.pieza_actual.color

    def eliminar_filas_completas(self):
        filas_completas = []
        for y in range(TABLERO_ALTO):
            if all(self.tablero[y]):
                filas_completas.append(y)

        if filas_completas:
            num_lineas_eliminadas = len(filas_completas)
            self.mostrar_mensaje_lineas_eliminadas(num_lineas_eliminadas)

            for y in filas_completas:
                del self.tablero[y]
                self.tablero.insert(0, [0] * TABLERO_ANCHO)
        
        return len(filas_completas)

    def mostrar_mensaje_lineas_eliminadas(self, num_lineas):
        mensaje = f"¡Líneas eliminadas: {num_lineas}!"
        self.canvas.create_text(
            TABLERO_ANCHO * TAMANO_CUADRO // 2,
            TABLERO_ALTO * TAMANO_CUADRO // 2,
            text=mensaje,
            font=("Arial", 24),
            fill="blue"
        )
        return num_lineas

    def dibujar(self):
        self.canvas.delete("all")
        for y, fila in enumerate(self.tablero):
            for x, color in enumerate(fila):
                if color:
                    self.canvas.create_rectangle(
                        x * TAMANO_CUADRO,
                        y * TAMANO_CUADRO,
                        (x + 1) * TAMANO_CUADRO,
                        (y + 1) * TAMANO_CUADRO,
                        fill=color, outline="black"
                    )

        if self.pieza_actual:
            for x, y in self.pieza_actual.coordenadas():
                self.canvas.create_rectangle(
                    x * TAMANO_CUADRO,
                    y * TAMANO_CUADRO,
                    (x + 1) * TAMANO_CUADRO,
                    (y + 1) * TAMANO_CUADRO,
                    fill=self.pieza_actual.color, outline="black"
                )

    def mostrar_mensaje_final(self, mensaje):
        self.canvas.create_text(
            TABLERO_ANCHO * TAMANO_CUADRO // 2,
            TABLERO_ALTO * TAMANO_CUADRO // 2,
            text=mensaje,
            font=("Arial", 24),
            fill="red"
        )
class Pieza:
    def __init__(self, color):
        self.color = color
        self.forma = random.choice([I, J, L, O, S, T, Z])
        self.x = 0
        self.y = 0

    def coordenadas(self):
        for y, fila in enumerate(self.forma):
            for x, ocupado in enumerate(fila):
                if ocupado:
                    yield (self.x + x, self.y + y)

    def mover(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotar(self):
        self.forma = list(zip(*reversed(self.forma)))

    def puede_moverse(self, tablero, dx, dy):
        for x, y in self.coordenadas():
            if x + dx < 0 or x + dx >= TABLERO_ANCHO or y + dy >= TABLERO_ALTO or tablero[y + dy][x + dx]:
                return False
        return True

    def puede_rotar(self, tablero):
        for x, y in self.coordenadas():
            if x < 0 or x >= TABLERO_ANCHO or y >= TABLERO_ALTO or tablero[y][x]:
                return False
        return True

# Formas de piezas
I = [[1, 1, 1, 1]]
J = [[0, 0, 1],
     [1, 1, 1]]
L = [[1, 0, 0],
     [1, 1, 1]]
O = [[1, 1],
     [1, 1]]
S = [[0, 1, 1],
     [1, 1, 0]]
T = [[0, 1, 0],
     [1, 1, 1]]
Z = [[1, 1, 0],
     [0, 1, 1]]

if __name__ == "__main__":
    root = tk.Tk()
    game = TetrisGame(root)
    root.mainloop()
