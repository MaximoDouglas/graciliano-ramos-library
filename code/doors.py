import math

DEG2RAD = math.pi/180

class Door:

    def __init__(self, levels, centers):
        self.doors = []

        for level in levels:
            for center in centers:
                door = []

                extra = 0
                if center == level:
                    extra = 0.25

                dl = self.door_left(center, level, extra)
                dr = self.door_right(center, level, extra)

                door.extend(dl)
                door.extend(dr)

                self.doors.append(door)

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
        start_angle = 0
        if direction == 'left':
            start_angle = 90

        for i in range(0 + start_angle, 91 + start_angle, 5):
            degInRad = i * (DEG2RAD)
            x = center + math.cos(degInRad) * (0.5 + extra)
            y = level + 2 + math.sin(degInRad) * (0.5 + extra)
            z = 8
            door.append((x, y, z))

        return door

    def get_doors(self):
        return self.doors

