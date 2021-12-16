import networkx as nx
import os

def number_of_paths(graph, node, path, visit_twice = False):
    if node == "end":
        return 1
    count = 0
    for neighbour in graph.neighbors(node):
        neighbour_visit_twice = visit_twice
        if neighbour in path and not neighbour.isupper():
            if neighbour == "start" or not visit_twice:
                continue
            neighbour_visit_twice = False
        count += number_of_paths(graph, neighbour, path + [neighbour], neighbour_visit_twice)

    return count
def main():
    with open(os.path.join(os.path.dirname(__file__),"input.txt"), "r", encoding="utf-8") as file:

        cave_graph = nx.Graph()
        cave_graph.add_edges_from([line.strip().split("-") for line in file.readlines()])

        print(number_of_paths(cave_graph, "start", ["start"]))
        print(number_of_paths(cave_graph, "start", ["start"], visit_twice = True))

if __name__ == '__main__':
    main()
    