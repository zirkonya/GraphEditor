# To algorithm of searching
import heapq
import json

# Default node colors
DEFAULT_NODE_FILL_COLOR = "white"
DEFAULT_NODE_TEXT_COLOR = "black"
DEFAULT_NODE_OUTLINE_COLOR = "black"

# Default node size
DEFAULT_NODE_RADIUS = 32
DEFAULT_NODE_OUTLINE_WIDTH = 3

# Default edge color
DEFAULT_EDGE_COLOR = "black"

# Default edge size
DEFAULT_EDGE_WIDTH = 3

def dijkstra(graph, start_node, end_node):
    distances = {node: float('inf') for node in range(len(graph.nodes))}
    predecessors = {node: None for node in range(len(graph.nodes))}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node == end_node:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = predecessors[current_node]
            return path[::-1], distances[end_node]

        if current_distance > distances[current_node]:
            continue

        for neighbour, weight in graph.get_neighbours(current_node):
            distance = current_distance + weight
            if distance < distances[neighbour]:
                distances[neighbour] = distance
                predecessors[neighbour] = current_node
                heapq.heappush(priority_queue, (distance, neighbour))

    return None, None

class Node:
    def __init__(self, value, x, y, radius=DEFAULT_NODE_RADIUS):
        self.value = value
        self.x = x
        self.y = y
        self.radius = radius

    def __str__(self):
        return f"Value: {self.value} x: {self.x} y: {self.y} radius: {self.radius}"

    def __dict__(self):
        return {
            "value": self.value,
            "x": self.x,
            "y": self.y,
            "radius": self.radius
        }

    def set_value(self, value):
        self.value = value

    def set_pos(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def get_pos(self):
        return { "x": self.x, "y": self.y }

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def is_collide(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5 <= self.radius + other.radius

    def point_is_inside(self, x, y, radius=1):
        return ((self.x - x)**2 + (self.y - y)**2)**0.5 <= self.radius + radius

    def display(self, canvas, node_radius=DEFAULT_NODE_RADIUS, node_text_color=DEFAULT_NODE_TEXT_COLOR, node_outline_color=DEFAULT_NODE_OUTLINE_COLOR, node_outline_width=DEFAULT_NODE_OUTLINE_WIDTH, node_fill_color=DEFAULT_NODE_FILL_COLOR):
        canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill=node_fill_color, outline=node_outline_color, width=node_outline_width)
        canvas.create_text(self.x, self.y, text=self.value, fill=node_text_color)

class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def __str__(self):
        return f"Nodes: {', '.join([str(node) for node in self.nodes])} Edges: {self.edges}"

    def __getitem__(self, i):
        # if i is string
        if isinstance(i, str):
            for node in self.nodes:
                if node.value == i:
                    return node
        elif isinstance(i, int):
            return self.nodes[i]
        else:
            raise ValueError("Invalid index")

    def get_node_id(self, node_name):
        for i in range(len(self.nodes)):
            if self.nodes[i].value == node_name:
                return i
        return None

    def add_nodes(self, nodes):
        for node in nodes:
            self.nodes.append(node)

    def remove_nodes(self, nodes):
        for node in nodes:
            if node in self.nodes:
                self.nodes.remove(node)

    
    def add_edges(self, edges):
        # add edges & weight into self.edges dictionary
        for edge in edges:
            self.edges[edge] = edges[edge]

    def remove_edges(self, edges):
        for edge in edges:
            self.edges.remove(edge)

    def get_neighbours(self, node: int):
        neighbours = []
        # TODO : demander la logique attendu des vosins dans un graph dirigé
        for edge, weight in self.edges.items():
            if node in edge:
                neighbour = edge[0] if edge[0] != node else edge[1]
                neighbours.append((neighbour, weight))
        return neighbours

    # ADJACENCY 

    def get_adjacency_matrix(self):
        # TODO : get adjacency matrix
        # NEED : Matrix class
        pass

    def get_adjacency_list(self):
        adjacency_list = {}
        for i in range(len(self.nodes)):
            for j in range(i+1, len(self.nodes)):
                if adjacency_list[i]:
                    adjacency_list[i].append(j)
                else:
                    adjacency_list[i] = [j]
        return adjacency_list

    def shortest_path(self, start, end, algorithm=dijkstra):
        return ([start], 0) if start == end else algorithm(self, start, end)

    def run_algorithm(self, algorithm=dijkstra, visualize=False):
        if visualize:
            # visualize
            pass
        else:
            # No visualization
            pass

    def export_json(self, filename='graph.json'):
        json_nodes = [node.__dict__() for node in self.nodes]
        json_edges = [{'start': edge[0], 'end': edge[1], 'weight': self.edges[edge]} for edge in self.edges]

        with open(filename, 'w') as file:
            json.dump({'nodes': json_nodes, 'edges': json_edges}, fp=file)

    def import_json(filename='graph.json'):
        with open(filename, 'r') as file:
            json_data = json.load(file)
        json_nodes = json_data['nodes']
        json_edges = json_data['edges']
        
        graph = Graph()
        graph.add_nodes([Node(node['value'], node['x'], node['y'], node['radius']) for node in json_nodes])
        graph.add_edges({(edge['start'], edge['end']): edge['weight'] for edge in json_edges})
        return graph

    # Tkinter implementation to display graph
    def display(self, canvas, edge_width=DEFAULT_EDGE_WIDTH, edge_color=DEFAULT_EDGE_COLOR, node_radius=DEFAULT_NODE_RADIUS, node_text_color=DEFAULT_NODE_TEXT_COLOR, node_outline_color=DEFAULT_NODE_OUTLINE_COLOR, node_outline_width=DEFAULT_NODE_OUTLINE_WIDTH, node_fill_color=DEFAULT_NODE_FILL_COLOR):
        for edge in self.edges:
            start_node = self.nodes[edge[0]]
            end_node = self.nodes[edge[1]]
            canvas.create_line(start_node.x, start_node.y, end_node.x, end_node.y, fill=edge_color, width=edge_width)
        for node in self.nodes:
            node.display(canvas, node_radius, node_text_color, node_outline_color, node_outline_width, node_fill_color)