from classes import Coord

class Node:
    def __init__ (self, Coord, parent):
        self.g = 0
        self.h = 0
        self.f = 0

        self.Coord = Coord
        self.parent = parent