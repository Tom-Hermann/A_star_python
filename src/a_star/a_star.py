

from classes import Coord
from classes import Node
from src.a_star.gener_children import generate_children
from src.a_star.calc_state import *
from src.a_star.move_list import *
from src.constante import *


def a_star(map, start_node, end_node):
    open_list = []
    close_list = []

    open_list.append(start_node)
    i = 0
    while (open_list):
        i = take_lowest_fcost(open_list)
        current_node = open_list.pop(i)
        if (current_node.Coord.x == end_node.Coord.x and current_node.Coord.y == end_node.Coord.y):
            return (current_node)
        all_children = generate_children(map, current_node, end_node)
        for child_node in all_children:
            successor_current_cost = calc_gcost(child_node)
            if (child_is_in_list(child_node, open_list)):
                if (child_node.g <= successor_current_cost):
                    continue
            elif (child_is_in_list(child_node, close_list)):
                if (child_node.g <= successor_current_cost):
                    continue
                else:
                    close_list, open_list = move_list1_to_list2(child_node, close_list, open_list)
            else:
                open_list.append(child_node)
        close_list.append(current_node)
    if (current_node.Coord != end_node.Coord):
        return (EXIT_FAILURE)

def child_is_in_list(node, current_list):
    for node_in_list in current_list:
        if (node.Coord.x == node_in_list.Coord.x and node.Coord.y == node_in_list.Coord.y):
            return (1)
    return (0)


def take_lowest_fcost(open_list):
    i = 0
    index_save = 0
    fcost_save = open_list[i].f
    while (i != len(open_list)):
        if (fcost_save >= open_list[i].f):
            fcost_save = open_list[i].f
            index_save = i
        i += 1
    return (index_save)