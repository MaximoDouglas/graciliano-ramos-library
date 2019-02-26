
class Floor:

    def __init__(self):
        self.floors = []

        self.floors.append((
            (-10, 0, 10),
            (10, 0, 10),
            (10, 0, -10),
            (-10, 0, -10)
        ))

        self.floors.append((
            (-7, 4, 8),
            (7, 4, 8),
            (7, 4, -8),
            (-7, 4, -8)
        ))

        self.floors.append((
            (-7, 7, 8),
            (7, 7, 8),
            (7, 7, -8),
            (-7, 7, -8)
        ))

        self.floors.append((
            (-7, 10, 8),
            (7, 10, 8),
            (7, 10, -8),
            (-7, 10, -8)
        ))

    def get_floors(self):
        return self.floors

