from floors import Floor
from tops import Top
from doors import Door
from chairs import Chair
from chairs2 import Chair2
from walls import Wall
from bookcases import Bookcase
from bookcases2 import Bookcase2
from tables import Table
from structure import Structure
from front import Front


class Coordinates():

    # For doors
    levels = [0, 4, 7]
    centers = [-6.25, -4.75, -3.25, -1.75, 0, 1.75, 3.25, 4.75, 6.25]

    stct = Structure()
    tops = stct.get_tops()
    front = Front().get_front()

    doors_objects = {0: {}, 4: {}, 7: {}}
    doors = []
    left_doors = []
    for level in levels:
        for center in centers:
            door = Door(level, center)
            doors_objects[level][center] = door
            doors.append(door.get_door())
            left_doors.append(door.get_left_door())

    chairs = []
    c_coordsT = [(-5.5,0,9.3),
                (-4, 0, -15.7), (0, 0, -15.7), (4, 0, -15.7), (-2, 0, -12.7), (2, 0, -12.7), # 0 degrees
                (-4.7, 0, -15), (-0.7, 0, -15), (3.3, 0, -15), (-2.7, 0, -12), (1.3, 0, -12), # 90 degrees
                (-3.3, 0, -15), (0.7, 0, -15), (4.7, 0, -15), (-1.3, 0, -12), (2.7, 0, -12), # -90 degrees
                (-4, 0, -14.3), (0, 0, -14.3), (4, 0, -14.3), (-2, 0, -11.3), (2, 0, -11.3)] # 180 degrees

    c_coords = [(0, 0, 0)]*21
    for cc in c_coords:
        chair = Chair(cc).get_chair()
        chairs.append(chair)

    chairs2 = []
    c2_coordsT = [(5.5,0,6),
                (-5.5, 0, -6), (-5, 0, -6),
                (-4, 0, -6), (-3.5, 0, -6),
                (-2.5, 0, -6), (-2, 0, -6),
                (1.5, 0, -6), (2.5, 0, -6), (3.5, 0, -6), (4.5, 0, -6), (5.5, 0, -6)]
    c2_coords = [(0, 0, 0)]*12
    for cc2 in c2_coords:
        chair = Chair2(cc2).get_chair()
        chairs2.append(chair)

    tables = []
    ct_coordsT = [(-5.5,0,10), (-4, 0, -15), (0, 0, -15), (4, 0, -15), (-2, 0, -12), (2, 0, -12)]
    ct_coords = [(0, 0, 0)]*6
    for ct in ct_coords:
        table = Table(ct).get_table()
        tables.append(table)

    bookcases = []
    cbc_coordsT = [(3.5,0,3), (3.5,4,3), (-6.6, 0, -6.5), (-6.6, 0, -9.5),
                    (-6.6, 0, -12.5), (-6.6, 0, -15.5), (6.6, 0, -6.5),
                    (6.6, 0, -9.5), (6.6, 0, -12.5), (6.6, 0, -15.5),
                    (-1.5, 0, -19), (1.5, 0, -19)]
    cbc_coords = [(0, 0, 0)]*12
    for cbc in cbc_coords:
        bookcase = Bookcase(cbc).get_bookcase()
        bookcases.append(bookcase)

    bookcases2 = []
    cbc2_coordsT = [(3.5,0,1), (3.5,4,1), (-5.5, 0, -19), (6.5, 0, -19),
                    (-3.5, 0, -19), (4.5, 0, -19)]
    cbc2_coords = [(0, 0, 0)]*6
    for cbc2 in cbc2_coords:
        bookcase2 = Bookcase2(cbc2).get_bookcase()
        bookcases2.append(bookcase2)

    walls = []
    cw_coords = [(0,0,0)]
    for cw in cw_coords:
        wall = Wall(cw).get_wall()
        walls.append(wall)

    floors = []
    cf_coords = [(0,0,0)]
    for cf in cf_coords:
        floor = Floor(cf).get_floor()
        floors.append(floor)
