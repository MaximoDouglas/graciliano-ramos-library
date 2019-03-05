from walls import Wall
from floors import Floor
from tops import Top
from doors import Door
from chairs import Chair
from tables import Table
from structure import Structure


class Coordinates():

    # For doors
    levels = [0, 4, 7]
    centers = [-6.25, -4.75, -3.25, -1.75, 0, 1.75, 3.25, 4.75, 6.25]

    stct = Structure()

    walls = stct.get_walls()
    floors = stct.get_floors()
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
    ct_coords = [(0,0,0)]
    for ct in ct_coords:
        table = Table(ct).get_table()
        tables.append(table)
