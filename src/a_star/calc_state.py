from classes import Coord
from classes import Node

def calc_gcost(node):
    mv_cost = 0
    if (node.Coord.x - node.parent.Coord.x == 0 or node.Coord.y - node.parent.Coord.y == 0):
        mv_cost = 10
    else:
        mv_cost = 14
    return (node.parent.g + mv_cost)

def calc_hcost(current_node_coord, end_node_Coord):
    hcost = 0
    range = Coord.Coord(abs(current_node_coord.x - end_node_Coord.x),
            abs(current_node_coord.y - end_node_Coord.y))
    while (range.x != 0 and range.y != 0):
        hcost =+ 14
        range.x -= 1
        range.y -= 1
    while (range.x != 0):
        hcost += 10
        range.x -= 1
    while (range.y != 0):
        hcost += 10
        range.y -= 1
    return (hcost)