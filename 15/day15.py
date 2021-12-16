import os
import networkx as nx

adjecant =  [(1,0), (0,1)]

def destinations(point, height, width):
    edges = []
    for pos_x, pos_y in adjecant:
        newx, newy = point[0]+pos_x, point[1]+pos_y
        if 0 <= newx < width and 0 <= newy < height:
            edges.append((point, (newx,newy)))
    return edges


def length_of_path(graph, start, width, height):
    for node in graph:
        for edges in destinations(node, height, width):
            graph.add_edge(*edges)
    return nx.dijkstra_path_length(graph, start, (width-1, height-1), weight = lambda u, v, d: graph.nodes[v].get("weight", 1))

def main():
    with open(os.path.join(os.path.dirname(__file__),"input.txt"), encoding="utf-8") as file:

        graph = nx.Graph()
        start = (0,0)
        lines = file.read().splitlines()

        width = len(lines[0])
        height = len(lines)

        for i in range(height*5) :
            for j in range(width*5):
                graph.add_node((i,j), weight=((int(lines[i%height][j%width])+(i//width)+(j//height)-1)%9+1))

        print(length_of_path(graph, start, width, height))
        print(length_of_path(graph, start, width*5, height*5))

if __name__ == '__main__':
    main()
