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
    #door = Door(levels, centers)

    walls = wall.get_walls()
    floors = floor.get_floors()
    tops = top.get_tops()

    doors = []
    for i in range(3):
        door = Door(levels[i], 0)
        doors.append(door.get_door())

    chairs = [Chair([0,0,0]).get_chair(),
              Chair([1,0,0]).get_chair(),
              Chair([0,0,1]).get_chair()]

