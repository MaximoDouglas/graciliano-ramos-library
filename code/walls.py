
class Wall:

    def __init__(self):
        self.walls = []
        # 4 triples of vertexes
        self.walls.append((
            (-7, 0, 8),
            (-7, 10, 8),
            (-7, 10, -8),
            (-7, 0, -8)
        ))

        self.walls.append((
            (7, 0, 8),
            (7, 10, 8),
            (7, 10, -8),
            (7, 0, -8)
        ))

        self.walls.append((
            (-7, 0, -8),
            (-7, 10, -8),
            (7, 10, -8),
            (7, 0, -8)
        ))

        self.walls.append((
            (-1, 10, 4),
            (-1, 12, 4),
            (1, 12, 4),
            (1, 10, 4)
        ))

        self.walls.append((
            (-1, 10, 4),
            (-1, 12, 4),
            (-1, 12, 6),
            (-1, 10, 6)
        ))

        self.walls.append((
            (1, 10, 4),
            (1, 12, 4),
            (1, 12, 6),
            (1, 10, 6)
        ))

    def get_walls(self):
        return self.walls

