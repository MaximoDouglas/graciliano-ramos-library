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
    c_coords = [(-2.75,0,5), (-1,0,3), (-2.75,2,5), (-1,3.5,3)]
    for cc in c_coords:
        chair = Chair(cc).get_chair()
        chairs.append(chair)

    chairs2 = []
    c2_coords = [(2.75,0,3.25), (2.75,2,3.25), (2.75,3.5,3.25)]
    for cc2 in c2_coords:
        chair = Chair2(cc2).get_chair()
        chairs2.append(chair)

    tables = []
    ct_coords = [(-2.75,0,5.5), (-1,0,3.5), (-2.75,2,5.5), (-1,3.5,3.5)]
    for ct in ct_coords:
        table = Table(ct).get_table()
        tables.append(table)

    bookcases = []
    cbc_coords = [(1.2,0,5), (1.2,2,5)]
    for cbc in cbc_coords:
        bookcase = Bookcase(cbc).get_bookcase()
        bookcases.append(bookcase)

    bookcases2 = []
    cbc2_coords = [(1.5,0,4), (1.5,3.5,4)]
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
