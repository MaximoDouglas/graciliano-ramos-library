
class Structure:

    def __init__(self):
        self.tops = []
        self.face = []
        self.build_tops()

    def build_tops(self):
        self.tops.append(((-1, 12, 18), (-1, 12, 16), (0, 13, 17)))
        self.tops.append(((-1, 12, 16), (1, 12, 16), (0, 13, 17)))
        self.tops.append(((1, 12, 18), (1, 12, 16), (0, 13, 17)))
        self.tops.append(((-1, 12, 18), (1, 12, 18), (0, 13, 17)))

    def build_face(self, centers):
        levels = [0.01]
        for y in levels:
            piece = []
            for x in centers:
                if (x == 0 and y == 0.01):
                    piece.append((x-0.75, y, 21))
                    piece.append((x-0.75, y+2, 21))
                    piece.append((x+0.75, y+2, 21))
                    piece.append((x+0.75, y, 21))
                else:
                    if(x == -6.25):
                        piece.append((-6.99, y, 21))

                    piece.append((x-0.5, y, 21))
                    piece.append((x-0.5, y+2, 21))
                    piece.append((x+0.5, y+2, 21))
                    piece.append((x+0.5, y, 21))

                    if(x == 6.25):
                        piece.append((6.99, y, 21))

            if (y == 0.01):
                piece.append((6.99, y+3.79, 21))
                piece.append((-6.99, y+3.79, 21))
            else:
                piece.append((6.99, y+3, 21))
                piece.append((-6.99, y+3, 21))

            self.face.append(piece)

    def get_tops(self):
        return self.tops

    def get_face(self, centers):
        self.build_face(centers)
        return self.face
