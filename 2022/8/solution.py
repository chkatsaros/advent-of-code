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

def is_visible(visibility):
    if visibility["left"] or visibility["right"] or visibility["top"] or visibility["bottom"]:
        return True
    return False
    

def visible_from(map, row, col):
    visibility = {
        "top": True,
        "bottom": True,
        "left": True,
        "right": True
    }
    
    for i in range(len(map)):
        if map[row][col] <= map[row][i] and (visibility['left'] or visibility["right"]):
                if col > i:
                    visibility["left"] = False
                elif col < i:
                    visibility["right"] = False
        
        if map[row][col] <= map[i][col] and (visibility['top'] or visibility["bottom"]):
                if row > i:
                    visibility["top"] = False
                elif row < i:
                    visibility["bottom"] = False
                    
    return visibility 

def calculate_view_score(map, row, col):
    score = {
        "top": 0,
        "bottom": 0,
        "left": 0,
        "right": 0
    }
    
    # left
    for i in range(col - 1, -1, -1):
        score["left"] += 1
        if map[row][i] >= map[row][col]:
            break
    
    # right
    for i in range(col + 1, len(map)):
        score["right"] += 1
        if map[row][i] >= map[row][col]:
            break
        
    # top
    for i in range(row - 1, -1, -1):
        score["top"] += 1
        if map[i][col] >= map[row][col]:
            break
        
    # bottom
    for i in range(row + 1, len(map[0])):
        score["bottom"] += 1
        if map[i][col] >= map[row][col]:
            break
            
    return (score["top"] * score["bottom"] * score["left"] * score["right"])

input = open(sys.argv[1], 'r')
lines = input.readlines()

trees = build_tree_map(lines)

view_scores = []
visible_trees = 0

for i in range(len(trees)):
    for j in range(len(trees[0])):
        tree_visibility = visible_from(trees, i, j)
        if is_visible(tree_visibility):
            visible_trees += 1
        view_scores.append(calculate_view_score(trees, i, j))
            
print(visible_trees)
print(max(view_scores))

input.close()