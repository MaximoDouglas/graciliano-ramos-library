import math

DEG2RAD = math.pi/180

class Door:

    def __init__(self, level, center):
        self.door = []
        self.left_door = []
        self.right_door = []
        self.level = level
        self.center = center
        self.max_height = None
        self.min_height = None
        self.max_width = None
        self.min_width = None

        self.build_door()

    def build_door(self):

        extra = 0.25 if self.center == self.level else 0

        dl = self.door_left(self.center, self.level, extra)
        dr = self.door_right(self.center, self.level, extra)

        self.door.extend(dl)
        self.door.extend(dr)

    def door_left(self, center, level, extra):

        door = []

        door.append((center - 0.5 - extra, level + 2, 20))
        door.append((center - 0.5 - extra, level, 20))
        door.append((center, level, 20))
        door.append((center, level + 2, 20))

        ds = self.door_sup(center, level, extra, 'left')
        door.extend(ds)

        self.max_height = max([vertex[1] for vertex in door])
        self.min_height = min([vertex[1] for vertex in door])
        self.min_width = min([vertex[0] for vertex in door])
        self.max_width = max([vertex[0] for vertex in door])
        self.center_point = ((self.max_width + self.min_width)/2.0,
                (self.max_height + self.min_height)/2.0)

        self.left_door.extend(door)

        return door

    def door_right(self, center, level, extra):

        door = []

        door.append((center, level + 2, 20))
        door.append((center, level, 20))
        door.append((center + 0.5 + extra, level, 20))
        door.append((center + 0.5 + extra, level + 2, 20))

        ds = self.door_sup(center, level, extra, 'right')
        door.extend(ds)

        self.right_door.extend(door)

        return door

    def door_sup(self, center, level, extra, direction):

        door = []
        start_angle = 0 if direction == 'right' else 90

        for i in range(0 + start_angle, 91 + start_angle, 10):
            degInRad = i * (DEG2RAD)
            x = center + math.cos(degInRad) * (0.5 + extra)
            y = level + 2 + math.sin(degInRad) * (0.5 + extra)
            z = 20
            door.append((x, y, z))

        return door

    def get_door(self):
        return self.door

    def get_left_door(self):
        return self.left_door

    def get_right_door(self):
        return self.right_door
