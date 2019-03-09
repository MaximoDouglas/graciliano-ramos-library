
class Top:

    def __init__(self):
        self.tops = []

        self.tops.append((
            (-1, 12, 6),
            (-1, 12, 4),
            (0, 13, 5)
        ))

        self.tops.append((
            (-1, 12, 4),
            (1, 12, 4),
            (0, 13, 5)
        ))

        self.tops.append((
            (1, 12, 6),
            (1, 12, 4),
            (0, 13, 5)
        ))

    def get_tops(self):
        return self.tops
