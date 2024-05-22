from collections import deque

class Robot:
    def __init__(self, rejilla):
        self.rejilla = rejilla
        self.fil = len(rejilla)
        self.col = len(rejilla[0])

    def mov_val(self, r, c):
        return 0 <= r < self.fil and 0 <= c < self.col and self.rejilla[r][c] != 1

    def enc_camino(self):
        if not self.rejilla or self.rejilla[0][0] == 1 or self.rejilla[self.fil - 1][self.col - 1] == 1:
            return None  # No se puede encontrar un camino si la esquina superior izquierda o la esquina inferior derecha están bloqueadas
        
        cola = deque([(0, 0, [])])  # (fila, columna, camino)
        visitado = set()

        while cola:
            r, c, cami = cola.popleft()
            if (r, c) == (self.fil - 1, self.col - 1):
                return cami + [(r, c)]

            if (r, c) in visitado:
                continue
            visitado.add((r, c))

            if self.mov_val(r + 1, c):
                cola.append((r + 1, c, cami + [(r, c)]))
            if self.mov_val(r, c + 1):
                cola.append((r, c + 1, cami + [(r, c)]))

        return None  # No se encontró un camino válido

# Ejemplo
rejilla = [
    #0  #1 #2 #3
    [0, 0, 0, 1], #0
    [1, 1, 0, 0], #1
    [0, 0, 0, 0], #2
    [0, 1, 1, 0]  #3
]

robot = Robot(rejilla)
camino = robot.enc_camino()
if camino:
    print("Camino encontrado:")
    for r, c in camino:
        print(f"({r}, {c})")
else:
    print("No se encontró un camino válido.")
