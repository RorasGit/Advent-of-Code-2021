import networkx as nx


def findEnd(node, travel, visited = True):
    if(node == "end"):
        return 1
    count = 0
    for e in G.neighbors(node):
        if(e == "start"):
            continue
        v = visited
        if(travel.count(e) > 0 and not e.isupper()):
            if(visited):
                continue
            v = True
    
        t = travel.copy()
        t.append(e)
        count += findEnd(e, t, v)
                    
    return count                 
    

    

with open("input.txt") as f:
    
    edges = [a.strip().split("-") for a in f.readlines()]

    G = nx.Graph()
    G.add_edges_from(edges)
    print(findEnd("start", ["start"]))
    print(findEnd("start", ["start"], False))
        
    

    
