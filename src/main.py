#!/bin/python3.12
from tools.graph import Graph, Node

def main():
    g = Graph()
    g.add_nodes([Node(1, 10, 10), Node(2, 20, 20), Node(3, 30, 30)])
    g.add_edges({(g.get_node_id(1), g.get_node_id(2)): 10, (g.get_node_id(2), g.get_node_id(3)): 30})
    print(g)
    g.export_json()
    g2 = Graph()
    g2.import_json()
    print(g2)

if __name__ == "__main__":
    main()