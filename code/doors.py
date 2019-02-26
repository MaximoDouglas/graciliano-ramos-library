import math

DEG2RAD = math.pi/180

class Door:

    def __init__(self, levels, centers):
        self.doors = []

        for level in levels:
            for center in centers:
                if (center == 0 and level == 0):
                    door = []
                    # --- LEFT
                    door.append((-0.75, 2, 8))
                    door.append((-0.75, 0, 8))
                    door.append((0, 0, 8))
                    door.append((0, 2, 8))
                    for i in range(90, 181, 5):
                        degInRad = i*(DEG2RAD)
                        door.append((math.cos(degInRad)*(0.75), 2 + math.sin(degInRad)*(0.75), 8))

                    # --- RIGHT
                    door.append((0, 2, 8))
                    door.append((0, 0, 8))
                    door.append((0.75, 0, 8))
                    door.append((0.75, 2, 8))
                    for i in range(0, 91, 5):
                        degInRad = i*(DEG2RAD)
                        door.append((math.cos(degInRad)*(0.75), 2 + math.sin(degInRad)*(0.75), 8))

                    self.doors.append(door)
                else:
                    door = []
                    # --- LEFT
                    door.append((center - 0.5, level + 2, 8))
                    door.append((center - 0.5, level, 8))
                    door.append((center, level, 8))
                    door.append((center, level + 2, 8))
                    for i in range(90, 181, 5):
                        degInRad = i*(DEG2RAD)
                        door.append((center + math.cos(degInRad)*(0.5), level + 2 + math.sin(degInRad)*(0.5), 8))

                    # --- RIGHT
                    door.append((center, level + 2, 8))
                    door.append((center, level, 8))
                    door.append((center + 0.5, level, 8))
                    door.append((center + 0.5, level + 2, 8))
                    for i in range(0, 91, 5):
                        degInRad = i*(DEG2RAD)
                        door.append((center + math.cos(degInRad)*(0.5), level + 2 + math.sin(degInRad)*(0.5), 8))

                    self.doors.append(door)

    def get_doors(self):
        return self.doors

