import networkx as nx

def numberOfPaths(graph, node = "start", path = ["start"], visit_twice = False):
    if(node == "end"):
        return 1
    count = 0
    for neighbour in graph.neighbors(node):
        neighbour_visit_twice = visit_twice
        if(neighbour in path and not neighbour.isupper()):
            if neighbour == "start" or not visit_twice:
                continue
            else:
                neighbour_visit_twice = False
        count += numberOfPaths(graph, neighbour, path + [neighbour], neighbour_visit_twice)
                    
    return count                 

with open("input.txt") as f:
    
    cave_graph = nx.Graph()
    cave_graph.add_edges_from([line.strip().split("-") for line in f.readlines()])

    print(numberOfPaths(cave_graph))
    print(numberOfPaths(cave_graph, visit_twice = True))
        