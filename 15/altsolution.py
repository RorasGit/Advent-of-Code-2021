import os
import networkx as nx

adjecant =  [(1,0),(-1,0), (0,1), (0,-1)]

def lowest_risk_path_length(start, width, height, weight):
    graph = nx.DiGraph()
    edges = get_edges(width, height, weight)
    graph.add_weighted_edges_from(edges)
    return nx.dijkstra_path_length(graph, start, (width-1, height-1))

def get_edges(width, height, weight):
    return list(((a,b),(a,b+1), weight[a,b+1]) for a in range(width) for b in range(height-1)) + \
           list(((a,b),(a+1, b), weight[a+1,b]) for a in range(width-1) for b in range(height))+ \
           list(((a,b),(a,b-1), weight[a,b-1]) for a in range(width) for b in range(1,height)) + \
           list(((a,b),(a-1, b), weight[a-1,b]) for a in range(1,width) for b in range(height))

def get_edges2(width, height, weight):
    return [x for a,b in adjecant for x in list_of_weight_in_dir(width, height, weight, a, b) ]

def list_of_weight_in_dir(width, height, weight, right, down):
    return (((a,b),(a+right, b+down), weight[a+right,b+down])
    for a in range(width)[-min(right, 0):width-max(right, 0)]
    for b in range(height)[-min(down, 0):height-max(down, 0)])

def main():
    with open(os.path.join(os.path.dirname(__file__),"input.txt"), encoding="utf-8") as file:

        lines = file.read().splitlines()
        width = len(lines[0])
        height = len(lines)
        start = (0,0)
        weight = {}
        for i in range(height*5) :
            for j in range(width*5):
                weight[i,j] = (int(lines[i%height][j%width])+(i//width)+(j//height)-1)% 9 + 1

        print(lowest_risk_path_length(start, width, height, weight))
        print(lowest_risk_path_length(start, width*5, height*5, weight))

if __name__ == '__main__':
    main()
