class KnightMoveNode:
    def __init__(self, position, move_number):
        self.position = position  # (fila, columna)
        self.move_number = move_number  # Número del movimiento
        self.next = None  # Para enlace tipo lista

    def __repr__(self):
        return f"Movimiento {self.move_number}: {self.position}"
