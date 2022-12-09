import sys

def print_tree_map(map, x, y):
    for i in range(len(map)):
        line = ""
        for j in range(len(map[0])):
            if (x == i and y == j):
                line += "[" + map[i][j] + "]"
            else: 
                 line += " " + map[i][j] + " "
        print(line)

def build_tree_map(lines):
    map = []
    for i in range(len(lines)):
        map.append([])

    i = 0
    for line in lines: 
        for char in line.strip():
            map[i].append(char)
        i += 1
    return map

def is_edge_tree(map, row, col):
    if (row == 0) or (row == len(map) - 1) or (col == 0) or (col == len(map[0]) - 1):
        return True
    return False

def is_visible(visibility):
    if visibility["left"] or visibility["right"] or visibility["top"] or visibility["bottom"]:
        return True
    return False
    

def visible_from(map, row, col):
    # print_tree_map(map, row, col)
    visibility = {
        "top": True,
        "bottom": True,
        "left": True,
        "right": True
    }
    
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[row][col] <= map[i][j] and (visibility['left'] or visibility["right"]) and i == row:
                if col > j:
                    # print('this tree', map[row][col], 'is not visible from', 'left', map[i][j])
                    visibility["left"] = False
                elif col < j:
                    # print('this tree', map[row][col], 'is not visible from', 'right', map[i][j])
                    visibility["right"] = False

            if map[row][col] <= map[j][i] and (visibility['top'] or visibility["bottom"]) and i == col:
                if row > j:
                    # print('this tree', map[row][col], 'is not visible from', 'top', map[j][i])
                    visibility["top"] = False
                elif row < j:
                    # print('this tree', map[row][col], 'is not visible from', 'bottom', map[j][i])
                    visibility["bottom"] = False
     
    # print(visibility)
    # print()
    return visibility             

input = open(sys.argv[1], 'r')
lines = input.readlines()

trees = build_tree_map(lines)

visible_trees = 0
for i in range(len(trees)):
    for j in range(len(trees[0])):
        if is_edge_tree(trees, i, j):
            visible_trees += 1
        else:
            tree_visibility = visible_from(trees, i, j)
            if is_visible(tree_visibility):
                visible_trees += 1
            
print(visible_trees)

input.close()