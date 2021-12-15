import os
import networkx as nx

def lowest_risk_path_length(start, width, height, weight):
    graph = nx.DiGraph()
    edges = get_edges(width, height, weight)
    graph.add_weighted_edges_from(edges)
    return nx.dijkstra_path_length(graph, start, (width-1, height-1))

def get_edges(width, height, weight):
    return list(((a,b),(a,b+1), weight[a,b+1]) for a in range(width) for b in range(height-1)) + \
           list(((a,b),(a+1, b), weight[a+1,b]) for a in range(width-1) for b in range(height))

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
