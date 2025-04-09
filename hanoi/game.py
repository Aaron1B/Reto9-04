class Hanoi:
    def __init__(self, num_disks=3):
        self.num_disks = num_disks
        self.towers = [list(reversed(range(1, num_disks + 1))), [], []]
        self.moves = 0

    def move(self, from_tower, to_tower):
        if not self.towers[from_tower]:
            return False, "Torre de origen vacía."
        if self.towers[to_tower] and self.towers[from_tower][-1] > self.towers[to_tower][-1]:
            return False, "Movimiento inválido. Disco más grande sobre uno más pequeño."
        
        disk = self.towers[from_tower].pop()
        self.towers[to_tower].append(disk)
        self.moves += 1
        return True, f"Movimiento válido. Has movido el disco {disk}."

    def is_completed(self):
        return len(self.towers[2]) == self.num_disks

    def get_state(self):
        return [list(tower) for tower in self.towers]
