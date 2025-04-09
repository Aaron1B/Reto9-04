from .knight_models import KnightMoveNode, session

from collections import deque

class KnightGame:
    def __init__(self, start_position=(0, 0)):
        self.start_position = start_position
        self.moves = []
        self.board_size = 8  # Tablero de 8x8
        self.possible_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        self.head = None  # Nodo inicial
        self.tail = None  # Nodo final
        self.move_count = 0  # Contador de movimientos

    def solve(self):
        self._move(self.start_position[0], self.start_position[1], set())

    def _move(self, x, y, visited):
        if (x, y) in visited:
            return  # Si ya se visitó esta casilla, no se mueve a ella

        visited.add((x, y))
        self.move_count += 1
        self._store_move(x, y)

        # Obtenemos las posibles posiciones desde esta casilla
        possible_moves = self._get_possible_moves(x, y)

        # Guardamos las posibilidades de movimiento
        for move in possible_moves:
            nx, ny = move
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size:
                self._move(nx, ny, visited)

    def _store_move(self, from_x, from_y):
        move_number = self.move_count
        possible_moves = self._get_possible_moves(from_x, from_y)

        new_move = KnightMoveNode(
            from_x=from_x, from_y=from_y, move_number=move_number,
            possibilities=len(possible_moves)
        )

        # Si es el primer movimiento, asignamos el primer nodo
        if not self.head:
            self.head = new_move
        else:
            self.tail.next_node_id = new_move.id  # Linkeamos el nodo anterior al siguiente
        self.tail = new_move
        
        # Guardar el nodo en la base de datos
        session.add(new_move)
        session.commit()

        # Almacenar el movimiento en la lista
        self.moves.append(new_move)

    def _get_possible_moves(self, x, y):
        """Calcula las posiciones a las que el caballo puede moverse"""
        moves = []
        for dx, dy in self.possible_moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.board_size and 0 <= ny < self.board_size:
                moves.append((nx, ny))
        return moves

    def get_all_moves_from_db(self):
        return session.query(KnightMoveNode).all()

    def get_moves(self):
        return self.moves
