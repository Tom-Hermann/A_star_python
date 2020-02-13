# -*-coding:Utf-8 -*

import sys
from src.constante import *

def error_argv(argv):
    if (len(argv) == 2 and (argv[1] == '-h' or argv[1] == '--help')):
        print_usage()
    if (len(argv) != 2):
        print("Error: invalid number of agruments")
        exit (EXIT_FAILURE)
    try:
        fd = open(argv[1], "r")
    except FileNotFoundError:
        print("File no exist")
        exit(EXIT_FAILURE)
    map = fd.read()
    return (map)

def error_map(map):
    nb_s = 0
    nb_e = 0
    i = 0
    while (i != len(map)):
        if (map[i] == '\n' and (map[i - 1] == '\n' or i == 0)):
            print("File error: empty line")
            exit (EXIT_FAILURE)
        if (map[i] == "S" or map[i] == "s"):
            nb_s += 1
        elif (map[i] == "E" or map[i] == "e"):
            nb_e += 1
        elif (map[i] != " " and map[i] != "X" and map[i] != "x" and map[i] != '\n'):
            print("File error: unknow character: " + map[i])
            exit (EXIT_FAILURE)
        i += 1
    if (nb_e != 1):
        print("File error: end number")
        exit (EXIT_FAILURE)
    if (nb_s != 1):
        print("File error: start number")
        exit (EXIT_FAILURE)

def error_lab():
    print("Error: no answer possible")
    exit (EXIT_FAILURE)

def print_usage():
    print("USAGE:\n\t\t./resolve file_name")
    print("DESCRIPTION:\n\t\tThe file must contain a maze with:")
    print("\t\t-space for way")
    print("\t\t-X for wall")
    print("\t\t-S for the start")
    print("\t\t-E for the end")
    print("\nThe program whill creat a way of ""°"" who solve the maze")
    print("THe program return:\n\t0 if no error\n\t84 if the programme fails")
    exit (EXIT_SUCCESS)
