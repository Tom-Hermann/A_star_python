
def print_map(map):
    i = 0
    y = 0
    while (i != len(map)):
        y = 0
        while (y != len(map[i])):
            print(map[i][y], end = '')
            y += 1
        print('')
        i += 1

def print_all_coord(current_list):
    print("[", end = '')
    for node in current_list:
        print(node.Coord.x, node.Coord.y, "( f=", node.f, ")", end = ", ")
    print("]")


def print_node(node):
    print("Coord: [", node.Coord.x, node.Coord.y, " ], f =", node.f, "h = ", node.h, "g = ", node.g)