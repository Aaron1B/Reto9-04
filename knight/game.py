from .node import KnightMoveNode

class KnightTour:
    def __init__(self):
        self.N = 8
        self.board = [[-1 for _ in range(self.N)] for _ in range(self.N)]
        self.moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
        self.moves_y = [1, 2, 2, 1, -1, -2, -2, -1]
        self.move_count = 0
        self.head = None  # Nodo inicial
        self.tail = None  # Nodo final
        self.path_nodes = []  # Vector paralelo para acceder fácilmente

    def solve(self):
        # Empezamos en (0, 0)
        self.board[0][0] = 0
        self._add_node((0, 0), 0)
        if self._solve_util(0, 0, 1):
            return True
        else:
            print("No se encontró solución.")
            return False

    def _solve_util(self, x, y, movei):
        if movei == self.N * self.N:
            return True

        for i in range(8):
            next_x = x + self.moves_x[i]
            next_y = y + self.moves_y[i]
            if self._is_safe(next_x, next_y):
                self.board[next_x][next_y] = movei
                self._add_node((next_x, next_y), movei)
                if self._solve_util(next_x, next_y, movei + 1):
                    return True
                # Backtracking
                self.board[next_x][next_y] = -1
                self._remove_last_node()
        return False

    def _is_safe(self, x, y):
        return 0 <= x < self.N and 0 <= y < self.N and self.board[x][y] == -1

    def _add_node(self, position, move_number):
        node = KnightMoveNode(position, move_number)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.path_nodes.append(node)
        self.move_count += 1

    def _remove_last_node(self):
        if self.path_nodes:
            self.path_nodes.pop()
            self.move_count -= 1
            # Volver a enlazar tail
            if self.path_nodes:
                self.tail = self.path_nodes[-1]
                self.tail.next = None
            else:
                self.head = self.tail = None

    def get_move_list(self):
        return [f"{node}" for node in self.path_nodes]

    def get_move_count(self):
        return self.move_count

    def get_board(self):
        return self.board
