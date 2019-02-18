import math
class Coordinates():

    DEG2RAD = 3.14159/180;
    walls = []

    walls.append((
        (-7, 0, 8),
        (-7, 10, 8),
        (-7, 10, -8),
        (-7, 0, -8)
    ))

    walls.append((
        (7, 0, 8),
        (7, 10, 8),
        (7, 10, -8),
        (7, 0, -8)
    ))

    walls.append((
        (-7, 0, -8),
        (-7, 10, -8),
        (7, 10, -8),
        (7, 0, -8)
    ))

    doors = []
    centers = [-6.25, -4.75, -3.25, -1.75, 0, 1.75, 3.25, 4.75, 6.25]
    for center in centers:

        if (center == 0):
            door = []
            # --- LEFT
            door.append((-0.75, 2, 8))
            door.append((-0.75, 0, 8))
            door.append((0, 0, 8))
            door.append((0, 2, 8))
            for i in range(90, 181):
                degInRad = i*(DEG2RAD)
                door.append((math.cos(degInRad)*(0.75), 2 + math.sin(degInRad)*(0.75), 8))

            # --- RIGHT
            door.append((0, 2, 8))
            door.append((0, 0, 8))
            door.append((0.75, 0, 8))
            door.append((0.75, 2, 8))
            for i in range(0, 91):
                degInRad = i*(DEG2RAD)
                door.append((math.cos(degInRad)*(0.75), 2 + math.sin(degInRad)*(0.75), 8))

            doors.append(door)
        else:
            door = []
            # --- LEFT
            door.append((center - 0.5, 2, 8))
            door.append((center - 0.5, 0, 8))
            door.append((center, 0, 8))
            door.append((center, 2, 8))
            for i in range(90, 181):
                degInRad = i*(DEG2RAD)
                door.append((center + math.cos(degInRad)*(0.5), 2 + math.sin(degInRad)*(0.5), 8))

            # --- RIGHT
            door.append((center, 2, 8))
            door.append((center, 0, 8))
            door.append((center + 0.5, 0, 8))
            door.append((center + 0.5, 2, 8))
            for i in range(0, 91):
                degInRad = i*(DEG2RAD)
                door.append((center + math.cos(degInRad)*(0.5), 2 + math.sin(degInRad)*(0.5), 8))

            doors.append(door)

    ground0 = (
        (-10, 0, 10),
        (10, 0, 10),
        (10, 0, -10),
        (-10, 0, -10)
    )
