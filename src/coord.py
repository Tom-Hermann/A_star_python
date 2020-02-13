

def creat_coord_map(map):
    nb_line = compt_line(map)
    frame_map = format_map(nb_line)
    frame_map = creat_map(map, frame_map)
    return (frame_map)

def creat_map(map, frame_map):
    y = 0
    i = 0
    while (i != len(map)):
        if (map[i] == '\n'):
            y += 1
            i += 1
        else:
            frame_map[y].append(map[i])
            i += 1
    return (frame_map)


def format_map(nb_line):
    i = 0
    map_line = []
    while (i != nb_line):
        map_line.append([])
        i += 1
    return map_line

def compt_line(map):
    i = 0
    nb_line = 1
    while (i != len(map)):
        if (map[i] == '\n'):
            nb_line += 1
        i += 1
    return (nb_line)