#!/usr/bin/python3

from sys import argv, exit
from src.error import error_argv, error_map, error_lab
from src.coord import creat_coord_map
from src.usefull import print_map
from src.def_important_node import def_important_node
from src.a_star.a_star import a_star
from src.creat_reslove_way import resolve_map
from src.constante import *
from classes import Coord
from classes import Node

def main():
    map = error_argv(argv)
    error_map(map)

    map = creat_coord_map(map)
    print("Orginial map:")
    print_map(map)

    start_node = def_important_node(map, "S")
    end_node = def_important_node(map, "E")

    current_node = a_star(map, start_node, end_node)

    if (current_node == EXIT_FAILURE):
        error_lab()

    current_node = current_node.parent
    map = resolve_map(map, current_node, start_node)

    print("\nMap resolve:")
    print_map(map)

if __name__ == '__main__':
    main()
    exit (EXIT_SUCCESS)