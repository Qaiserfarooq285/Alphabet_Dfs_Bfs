graph = {
    "A" : ["B","C","D"],
    "B" : ["E","F"],
    "C" : ["G","H"],
    "D" : ["I","J"],
    "E" : ["K","L"],
    "F" : ["L","M"],
    "G" : ["N"],
    "H" : ["O","P"],
    "I" : ["P","Q"],
    "J" : ["R"],
    "K" : ["S"],
    "L" : ["T"],
    "M" : [],
    "N" : [],
    "O" : [],
    "P" : ["U"],
    "Q" : [],
    "R" : [],
    "T" : [],
    "U" : []}
def bfs_traversal(graph,start,goal):
    opened = [start]
    closed = []
    while opened:
        node=opened.pop(0)
        if node is goal:
            closed.append(node)
            return closed
        else:
            opened = opened+ [item for item in graph[node] if item  not in opened and item not in closed]
            closed.append(node)
    return "Goal not founde "

bfspath = bfs_traversal(graph ,'A','I')
print(bfspath)
