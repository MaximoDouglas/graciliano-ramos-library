
class Structure:

    def __init__(self):
        self.walls = []
        self.floors = []
        self.tops = []

        self.build_walls()
        self.build_floors()
        self.build_tops()

    def build_walls(self):
        self.walls.append((
            (-7, 0, 8), (-7, 10, 8),
            (-7, 10, -8), (-7, 0, -8)
        ))

        self.walls.append((
            (7, 0, 8), (7, 10, 8),
            (7, 10, -8), (7, 0, -8)
        ))

        self.walls.append((
            (-7, 0, -8), (-7, 10, -8),
            (7, 10, -8), (7, 0, -8)
        ))

        self.walls.append((
            (-1, 10, 4), (-1, 12, 4),
            (1, 12, 4), (1, 10, 4)
        ))

        self.walls.append((
            (-1, 10, 4), (-1, 12, 4),
            (-1, 12, 6), (-1, 10, 6)
        ))

        self.walls.append((
            (1, 10, 4), (1, 12, 4),
            (1, 12, 6), (1, 10, 6)
        ))

    def build_floors(self):
        self.floors.append((
            (-10, 0, 10), (10, 0, 10),
            (10, 0, -10), (-10, 0, -10)
        ))

        self.floors.append((
            (-7, 4, 8), (7, 4, 8),
            (7, 4, -8), (-7, 4, -8)
        ))

        self.floors.append((
            (-7, 7, 8), (7, 7, 8),
            (7, 7, -8), (-7, 7, -8)
        ))

        self.floors.append((
            (-7, 10, 8), (7, 10, 8),
            (7, 10, -8), (-7, 10, -8)
        ))

    def build_tops(self):
        self.tops.append(((-1, 12, 6), (-1, 12, 4), (0, 13, 5)))
        self.tops.append(((-1, 12, 4), (1, 12, 4), (0, 13, 5)))
        self.tops.append(((1, 12, 6), (1, 12, 4), (0, 13, 5)))

    def get_walls(self):
        return self.walls

    def get_floors(self):
        return self.floors

    def get_tops(self):
        return self.tops
