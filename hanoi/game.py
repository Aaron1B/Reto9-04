from .models import HanoiMoveNode, session

class HanoiGame:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.moves = []
        self.head = None  # Nodo inicial
        self.tail = None  # Nodo final

    def solve(self):
        self._move(self.num_disks, 'A', 'C', 'B')

    def _move(self, n, from_peg, to_peg, aux_peg):
        if n == 1:
            self._store_move(from_peg, to_peg)
        else:
            self._move(n - 1, from_peg, aux_peg, to_peg)
            self._store_move(from_peg, to_peg)
            self._move(n - 1, aux_peg, to_peg, from_peg)

    def _store_move(self, from_peg, to_peg):
        move_number = len(self.moves) + 1
        new_move = HanoiMoveNode(from_peg=from_peg, to_peg=to_peg, move_number=move_number)

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

    def get_moves(self):
        return self.moves

    def get_all_moves_from_db(self):
        return session.query(HanoiMoveNode).all()
