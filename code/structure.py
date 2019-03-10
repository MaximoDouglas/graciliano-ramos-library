
class Structure:

    def __init__(self):
        self.tops = []
        self.build_tops()

    def build_tops(self):
        self.tops.append(((-1, 12, 18), (-1, 12, 16), (0, 13, 17)))
        self.tops.append(((-1, 12, 16), (1, 12, 16), (0, 13, 17)))
        self.tops.append(((1, 12, 18), (1, 12, 16), (0, 13, 17)))

    def get_tops(self):
        return self.tops
