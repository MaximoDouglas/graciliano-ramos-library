from floors import Floor
from tops import Top
from doors import Door
from chairs import Chair
from walls import Wall
from bookcases import Bookcase
from tables import Table
from structure import Structure


class Coordinates():

    # For doors
    levels = [0, 4, 7]
    centers = [-6.25, -4.75, -3.25, -1.75, 0, 1.75, 3.25, 4.75, 6.25]

    stct = Structure()
    tops =  stct.get_tops()

    doors = []
    for level in levels:
        for center in centers:
            door = Door(level, center)
            doors.append(door.get_door())

    chairs = []
    c_coords = [(0,0,-.35)]
    for cc in c_coords:
        chair = Chair(cc).get_chair()
        chairs.append(chair)

    tables = []
    ct_coords = [(1,0,0)]
    for ct in ct_coords:
        table = Table(ct).get_table()
        tables.append(table)

    bookcases = []
    cbc_coords = [(0,0,0)]
    for cbc in cbc_coords:
        bookcase = Bookcase(cbc).get_bookcase()
        bookcases.append(bookcase)

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
