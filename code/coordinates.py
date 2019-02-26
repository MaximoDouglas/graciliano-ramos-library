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

    walls.append((
        (-1, 10, 4),
        (-1, 12, 4),
        (1, 12, 4),
        (1, 10, 4)
    ))

    walls.append((
        (-1, 10, 4),
        (-1, 12, 4),
        (-1, 12, 6),
        (-1, 10, 6)
    ))

    walls.append((
        (1, 10, 4),
        (1, 12, 4),
        (1, 12, 6),
        (1, 10, 6)
    ))

    doors = []
    centers = [-6.25, -4.75, -3.25, -1.75, 0, 1.75, 3.25, 4.75, 6.25]
    levels = [0, 4, 7]

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

                doors.append(door)
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

                doors.append(door)

    floors = []
    floors.append((
        (-10, 0, 10),
        (10, 0, 10),
        (10, 0, -10),
        (-10, 0, -10)
    ))

    floors.append((
        (-7, 4, 8),
        (7, 4, 8),
        (7, 4, -8),
        (-7, 4, -8)
    ))

    floors.append((
        (-7, 7, 8),
        (7, 7, 8),
        (7, 7, -8),
        (-7, 7, -8)
    ))

    floors.append((
        (-7, 10, 8),
        (7, 10, 8),
        (7, 10, -8),
        (-7, 10, -8)
    ))

    tops = []
    tops.append((
        (-1, 12, 6),
        (-1, 12, 4),
        (0, 13, 5)
    ))

    tops.append((
        (-1, 12, 4),
        (1, 12, 4),
        (0, 13, 5)
    ))

    tops.append((
        (1, 12, 6),
        (1, 12, 4),
        (0, 13, 5)
    ))

    # CHAIR coordinates
    referente = [0, 0, 0] #x, y and z of the floor
    # This vector will store the chairs in the building
    chairs = []

    # ------- Here will begin the for or function to make more than one chair

    # This vector will store the four parts - back, sit, legs and the iron stick that holds the back part
    chair = []

    #A for iteration for each one of the seven parts that compose the chair
    new_part_half_width = [0.25, 0.05, 0.25]
    new_part_half_height = [0.25, 0.10, 0.05]
    new_part_half_depth = [0.05, 0.025, 0.25]
    new_part_center = [
                    (referente[0] + 0.0, referente[1] + 0.85, referente[2] + 0.0),
                    (referente[0] + 0.0, referente[1] + 0.5, referente[2] - 0.025),
                    (referente[0] + 0.0, referente[1] + 0.45, referente[2] + 0.25)
                    ]

    # For loop to generate all the coordinates of the chair parts
    for i in range(len(new_part_half_height)):
        new_part = []

        # a, b, c, d, e and f vertices
        a = (
            referente[0] - new_part_half_width[i] + new_part_center[i][0] ,
            referente[1] + new_part_center[i][1] - new_part_half_height[i],
            referente[2] + new_part_half_depth[i] + new_part_center[i][2]
        )

        b = (
            referente[0] + new_part_half_width[i] + new_part_center[i][0],
            referente[1] + new_part_center[i][1] - new_part_half_height[i],
            referente[2] + new_part_half_depth[i] + new_part_center[i][2]
        )

        c = (
            referente[0] + new_part_half_width[i] + new_part_center[i][0] ,
            referente[1] + new_part_center[i][1] + new_part_half_height[i],
            referente[2] + new_part_half_depth[i] + new_part_center[i][2]
        )

        d = (
            referente[0] - new_part_half_width[i] + new_part_center[i][0] ,
            referente[1] + new_part_center[i][1] + new_part_half_height[i],
            referente[2] + new_part_half_depth[i] + new_part_center[i][2]
        )

        e = (
            referente[0] - new_part_half_width[i] + new_part_center[i][0] ,
            referente[1] + new_part_center[i][1] - new_part_half_height[i],
            referente[2] - new_part_half_depth[i] + new_part_center[i][2]
        )

        f = (
            referente[0] + new_part_half_width[i] + new_part_center[i][0] ,
            referente[1] + new_part_center[i][1] - new_part_half_height[i],
            referente[2] - new_part_half_depth[i] + new_part_center[i][2]
        )

        g = (
            referente[0] + new_part_half_width[i] + new_part_center[i][0] ,
            referente[1] + new_part_center[i][1] + new_part_half_height[i],
            referente[2] - new_part_half_depth[i] + new_part_center[i][2]
        )

        h = (
            referente[0] - new_part_half_width[i] + new_part_center[i][0] ,
            referente[1] + new_part_center[i][1] + new_part_half_height[i],
            referente[2] - new_part_half_depth[i] + new_part_center[i][2]
        )

        # This vector stores the vertices of the front face of the new_part part of the chair
        new_part_front = (a,b,c,d)
        new_part.append(new_part_front)


        # This vector stores the vertices of the new_part face of the new_part part of the chair
        new_part_back = (e,f,g,h)
        new_part.append(new_part_back)

        # This vector stores the vertices of the right face of the new_part part of the chair
        new_part_right = (b,f,g,c)
        new_part.append(new_part_right)

        # This vector stores the vertices of the left face of the new_part part of the chair
        new_part_left = (e,a,d,h)
        new_part.append(new_part_left)

        # This vector stores the vertices of the top face of the new_part part of the chair
        new_part_top = (c,g,h,d)
        new_part.append(new_part_top)

        # This vector stores the vertices of the bottom face of the new_part part of the chair
        new_part_bottom = (a,e,f,b)
        new_part.append(new_part_bottom)

        chair.append(new_part)

    chairs.append(chair)
