class Hanoi:
    def __init__(self, num_disks=3):
        self.num_disks = num_disks
        self.towers = [list(reversed(range(1, num_disks + 1))), [], []]
        self.moves = 0
        self.history = []

    def solve(self):
        self._move(self.num_disks, 0, 2, 1)

    def _move(self, n, source, target, auxiliary):
        if n == 1:
            self._apply_move(source, target)
        else:
            self._move(n - 1, source, auxiliary, target)
            self._apply_move(source, target)
            self._move(n - 1, auxiliary, target, source)

    def _apply_move(self, from_tower, to_tower):
        disk = self.towers[from_tower].pop()
        self.towers[to_tower].append(disk)
        self.moves += 1
        self.history.append(f"Movimiento {self.moves}: de {from_tower} a {to_tower}")

    def get_state(self):
        return [list(tower) for tower in self.towers]

    def get_history(self):
        return self.history

    def get_move_count(self):
        return self.moves
