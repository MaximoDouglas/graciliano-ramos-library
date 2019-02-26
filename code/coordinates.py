from walls import Wall
from floors import Floor
from tops import Top
from doors import Door
from chairs import Chair

class Coordinates():

    # For doors
    levels = [0, 4, 7]
    centers = [-6.25, -4.75, -3.25, -1.75, 0, 1.75, 3.25, 4.75, 6.25]

    wall = Wall()
    floor = Floor()
    top = Top()
    door = Door(levels, centers)
    chair = Chair()

    walls = wall.get_walls()
    floors = floor.get_floors()
    tops = top.get_tops()
    doors = door.get_doors()
    chairs = chair.get_chairs()

