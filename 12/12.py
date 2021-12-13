import networkx as nx


def numberOfPaths(node = "start", path = ["start"], time = False):
    if(node == "end"):
        return 1
    count = 0
    for neighbour in G.neighbors(node):
        path_time = time
        if(neighbour in path and not neighbour.isupper()):
            if neighbour == "start" or not time:
                continue
            else:
                path_time = False
        count += numberOfPaths(neighbour, path + [neighbour], path_time)
                    
    return count                 

with open("input.txt") as f:
    
    G = nx.Graph()
    G.add_edges_from([a.strip().split("-") for a in f.readlines()])

    print(numberOfPaths())
    print(numberOfPaths(time = True))
        
    

    
