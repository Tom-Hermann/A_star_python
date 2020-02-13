from classes import Coord
from classes import Node

def def_important_node(map, sign):
    coord = def_important_coord(map, sign)
    node = Node.Node(coord, None)
    return (node)

def def_important_coord(map, sign):
    x = 0
    y = 0
    while (map[y][x] != sign):
        x += 1
        if (x == len(map[y])):
            x = 0
            y += 1
    start_coord = Coord.Coord(x, y)
    return (start_coord)
