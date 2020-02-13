from src.a_star.calc_state import *
from classes import Coord
from classes import Node

def generate_children(map, current_node, end_node):
    all_children = []
    for new_coord in [[0, -1], [0, 1], [-1, 0], [1, 0], [-1, -1], [-1, 1], [1, -1], [1, 1]]:
        child_coord = Coord.Coord(0, 0)
        child_coord.x = current_node.Coord.x + new_coord[0]
        child_coord.y = current_node.Coord.y + new_coord[1]
        if (verify_coord(map, child_coord)):
            new_child = Node.Node(child_coord, current_node)
            new_child = generate_state(new_child, end_node)
            all_children.append(new_child)
    return (all_children)

def generate_state(child, end_node):
    child.g = calc_gcost(child)
    child.h = calc_hcost(child.Coord, end_node.Coord)
    child.f = child.h + child.g
    return(child)


def verify_coord(map, child_coord):
    if (child_coord.x < 0 or child_coord.y < 0):
        return (0)
    elif (child_coord.y >= len(map)):
        return (0)
    elif (child_coord.x >= len(map[child_coord.y])):
        return (0)
    if (map[child_coord.y][child_coord.x] == "X" or map[child_coord.y][child_coord.x] == "S"):
        return (0)
    return (1)