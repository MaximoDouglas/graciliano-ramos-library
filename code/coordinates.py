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
    chair_back_half_height = 0.25
    chair_back_half_width = 0.25
    chair_back_half_depth = 0.05
    chair_back_center = (referente[0] + 0.0, referente[1] + 0.85, referente[2] + 0.0)

    # This vector will store the chairs in the building
    chairs = []

    # This vector will store the four parts - back, sit, legs and the iron stick that holds the back part
    chair = []

    # This vectos will store the six faces of the back of the chair
    chair_back = []

    # a, b, c, d, e and f vertices
    a = (
        referente[0] - chair_back_half_width + chair_back_center[0] ,
        referente[1] + chair_back_center[1] - chair_back_half_height,
        referente[2] + chair_back_half_depth + chair_back_center[2]
    )

    b = (
        referente[0] + chair_back_half_width + chair_back_center[0] ,
        referente[1] + chair_back_center[1] - chair_back_half_height,
        referente[2] + chair_back_half_depth + chair_back_center[2]
    )

    c = (
        referente[0] + chair_back_half_width + chair_back_center[0] ,
        referente[1] + chair_back_center[1] + chair_back_half_height,
        referente[2] + chair_back_half_depth + chair_back_center[2]
    )

    d = (
        referente[0] - chair_back_half_width + chair_back_center[0] ,
        referente[1] + chair_back_center[1] + chair_back_half_height,
        referente[2] + chair_back_half_depth + chair_back_center[2]
    )

    e = (
        referente[0] - chair_back_half_width + chair_back_center[0] ,
        referente[1] + chair_back_center[1] - chair_back_half_height,
        referente[2] - chair_back_half_depth + chair_back_center[2]
    )

    f = (
        referente[0] + chair_back_half_width + chair_back_center[0] ,
        referente[1] + chair_back_center[1] - chair_back_half_height,
        referente[2] - chair_back_half_depth + chair_back_center[2]
    )

    g = (
        referente[0] + chair_back_half_width + chair_back_center[0] ,
        referente[1] + chair_back_center[1] + chair_back_half_height,
        referente[2] - chair_back_half_depth + chair_back_center[2]
    )

    h = (
        referente[0] - chair_back_half_width + chair_back_center[0] ,
        referente[1] + chair_back_center[1] + chair_back_half_height,
        referente[2] - chair_back_half_depth + chair_back_center[2]
    )

    # This vector stores the vertices of the front face of the back part of the chair
    chair_back_front = (a,b,c,d)
    chair_back.append(chair_back_front)


    # This vector stores the vertices of the back face of the back part of the chair
    chair_back_back = (e,f,g,h)
    chair_back.append(chair_back_back)

    # This vector stores the vertices of the right face of the back part of the chair
    chair_back_right = (b,f,g,c)
    chair_back.append(chair_back_right)

    # This vector stores the vertices of the left face of the back part of the chair
    chair_back_left = (e,a,d,h)
    chair_back.append(chair_back_left)

    # This vector stores the vertices of the top face of the back part of the chair
    chair_back_top = (c,g,h,d)
    chair_back.append(chair_back_top)

    # This vector stores the vertices of the bottom face of the back part of the chair
    chair_back_bottom = (a,e,f,b)
    chair_back.append(chair_back_bottom)

    chair.append(chair_back)

    # This vectos will store the six faces of the back of the chair
    chair_column = []
    chair_column_half_height = 0.10
    chair_column_half_width = 0.05
    chair_column_half_depth = 0.025
    chair_column_center = (referente[0] + 0.0, referente[1] + 0.5, referente[2] - 0.025)

    # a, b, c, d, e and f vertices
    a = (
        referente[0] - chair_column_half_width + chair_column_center[0] ,
        referente[1] + chair_column_center[1] - chair_column_half_height,
        referente[2] + chair_column_half_depth + chair_column_center[2]
    )

    b = (
        referente[0] + chair_column_half_width + chair_column_center[0] ,
        referente[1] + chair_column_center[1] - chair_column_half_height,
        referente[2] + chair_column_half_depth + chair_column_center[2]
    )

    c = (
        referente[0] + chair_column_half_width + chair_column_center[0] ,
        referente[1] + chair_column_center[1] + chair_column_half_height,
        referente[2] + chair_column_half_depth + chair_column_center[2]
    )

    d = (
        referente[0] - chair_column_half_width + chair_column_center[0] ,
        referente[1] + chair_column_center[1] + chair_column_half_height,
        referente[2] + chair_column_half_depth + chair_column_center[2]
    )

    e = (
        referente[0] - chair_column_half_width + chair_column_center[0] ,
        referente[1] + chair_column_center[1] - chair_column_half_height,
        referente[2] - chair_column_half_depth + chair_column_center[2]
    )

    f = (
        referente[0] + chair_column_half_width + chair_column_center[0] ,
        referente[1] + chair_column_center[1] - chair_column_half_height,
        referente[2] - chair_column_half_depth + chair_column_center[2]
    )

    g = (
        referente[0] + chair_column_half_width + chair_column_center[0] ,
        referente[1] + chair_column_center[1] + chair_column_half_height,
        referente[2] - chair_column_half_depth + chair_column_center[2]
    )

    h = (
        referente[0] - chair_column_half_width + chair_column_center[0] ,
        referente[1] + chair_column_center[1] + chair_column_half_height,
        referente[2] - chair_column_half_depth + chair_column_center[2]
    )

    # This vector stores the vertices of the front face of the column part of the chair
    chair_column_front = (a,b,c,d)
    chair_column.append(chair_column_front)


    # This vector stores the vertices of the column face of the column part of the chair
    chair_column_back = (e,f,g,h)
    chair_column.append(chair_column_back)

    # This vector stores the vertices of the right face of the column part of the chair
    chair_column_right = (b,f,g,c)
    chair_column.append(chair_column_right)

    # This vector stores the vertices of the left face of the column part of the chair
    chair_column_left = (e,a,d,h)
    chair_column.append(chair_column_left)

    # This vector stores the vertices of the top face of the column part of the chair
    chair_column_top = (c,g,h,d)
    chair_column.append(chair_column_top)

    # This vector stores the vertices of the bottom face of the column part of the chair
    chair_column_bottom = (a,e,f,b)
    chair_column.append(chair_column_bottom)

    chair.append(chair_column)
    chairs.append(chair)
