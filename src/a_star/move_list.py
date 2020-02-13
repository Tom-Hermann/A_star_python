from classes import Coord
from classes import Node

def move_list1_to_list2(child_node, first_list, second_list):
    for index, node in enumerate(first_list):
        if (node.Coord.x == child_node.Coord.x and node.Coord.y == child_node.Coord.y):
            second_list.append(first_list[index])
            first_list.pop(index)
            return (first_list, second_list)
