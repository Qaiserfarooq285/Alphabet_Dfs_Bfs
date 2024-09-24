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
    "U" : [],
    "S" : []}
def dfs_traversal(graph,start,goal):
    opened = [start]
    closed = []
    while opened:
        node=opened.pop(0)
        if node is goal:
            closed.append(node)
            return closed
        else:
            opened = [item for item in graph[node] if item not in opened and item not in closed] +opened
            closed.append(node)
    return "Goal not founde "

dfspath = dfs_traversal(graph,'A','R')
print(dfspath)
