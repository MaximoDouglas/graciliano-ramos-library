import math

DEG2RAD = math.pi/180

class Door:

    def __init__(self, level, center):
        self.door = []
        self.level = level
        self.center = center

        self.build_door()

    def build_door(self):

        extra = 0 if self.center == self.level else 0.25

        dl = self.door_left(self.center, self.level, extra)
        dr = self.door_right(self.center, self.level, extra)

        self.door.extend(dl)
        self.door.extend(dr)

    def door_left(self, center, level, extra):

        door = []

        door.append((center - 0.5 - extra, level + 2, 8))
        door.append((center - 0.5 - extra, level, 8))
        door.append((center, level, 8))
        door.append((center, level + 2, 8))

        ds = self.door_sup(center, level, extra, 'left')
        door.extend(ds)

        return door

    def door_right(self, center, level, extra):

        door = []

        door.append((center, level + 2, 8))
        door.append((center, level, 8))
        door.append((center + 0.5 + extra, level, 8))
        door.append((center + 0.5 + extra, level + 2, 8))

        ds = self.door_sup(center, level, extra, 'right')
        door.extend(ds)

        return door

    def door_sup(self, center, level, extra, direction):

        door = []
        start_angle = 0 if direction == 'left' else 90

        for i in range(0 + start_angle, 91 + start_angle, 5):
            degInRad = i * (DEG2RAD)
            x = center + math.cos(degInRad) * (0.5 + extra)
            y = level + 2 + math.sin(degInRad) * (0.5 + extra)
            z = 8
            door.append((x, y, z))

        return door

    def get_door(self):
        return self.door

