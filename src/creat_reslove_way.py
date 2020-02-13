
from classes import Coord
from classes import Node

def resolve_map(map, current_node, start_node):
    while (current_node.Coord.x != start_node.Coord.x or current_node.Coord.y != start_node.Coord.y):
        map[current_node.Coord.y][current_node.Coord.x] = "°"
        current_node = current_node.parent
    return (map)