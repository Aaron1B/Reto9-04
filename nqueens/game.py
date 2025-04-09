from .nqueens_models import QueenMoveNode, session

class NQueensGame:
    def __init__(self, n):
        self.n = n
        self.moves = []
        self.head = None
        self.tail = None

    def solve(self):
        self._place_queens(0, [-1] * self.n)

    def _place_queens(self, row, positions):
        if row == self.n:  # Si hemos colocado todas las reinas
            self._store_move(positions)
            return True

        for col in range(self.n):
            if self._is_safe(row, col, positions):
                positions[row] = col
                if self._place_queens(row + 1, positions):
                    return True
                positions[row] = -1  # Deshacer el movimiento
        return False

    def _is_safe(self, row, col, positions):
        for prev_row in range(row):
            if positions[prev_row] == col or \
               positions[prev_row] - prev_row == col - row or \
               positions[prev_row] + prev_row == col + row:
                return False
        return True

    def _store_move(self, positions):
        move_number = len(self.moves) + 1
        board = self._format_board(positions)
        new_move = QueenMoveNode(move_number=move_number, board=board)

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

    def _format_board(self, positions):
        # Crear una representación visual del tablero
        board = []
        for row in range(self.n):
            row_str = ['Q' if positions[row] == col else '.' for col in range(self.n)]
            board.append("".join(row_str))
        return "\n".join(board)

    def get_moves(self):
        return self.moves

    def get_all_moves_from_db(self):
        return session.query(QueenMoveNode).all()
