import tkinter as tk
from tools.graph import Graph

DEFAULT_HEIGHT = 600
DEFAULT_WIDTH = 800

class GraphWindow:
    def __init__(self, height=DEFAULT_HEIGHT, width=DEFAULT_WIDTH):
        print('INIT')
        self.selected_node = None
        self.current_graph = '__DEFAULT__'
        self.graphs = { '__DEFAULT__': Graph.import_json() }
        self.root = tk.Tk()
        self.root.title("GraphEditor")
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.export_button = tk.Button(self.root, text="Export Graph", command=self)
        self.export_button.pack()
        self.import_button = tk.Button(self.root, text="Import Graph", command=self)
        self.import_button.pack()
        self.canvas.bind("<Button-3>", self.on_right_click)

        self.canvas.bind("<Button-1>", self.on_left_click)
        self.canvas.bind("<ButtonRelease-1>", self.on_left_release)
        self.canvas.bind("<Double-Button-1>", self.on_double_click)
        self.canvas.bind("<B1-Motion>", self.on_mouse_motion)
        self.root.after(100, self.update)

    def mainloop(self):
        self.root.mainloop()

    def add_graph(self, name, graph):
        self.graphs[name] = graph

    def draw_graph(self):
        self.graphs[self.current_graph].display(self.canvas)

    def on_right_click(self, event):
        x, y = event.x, event.y
        node = self.get_node_at(x, y)
        if node:
            # display menu item with nodes properties & buttons to remove it; to add edge
            pass
        edge = self.get_edge_at(x, y)
        if edge:
            # display menu item with edge properties & buttons to remove it
            pass
        # display menu item to add nodes
        pass

    def on_left_click(self, event):
        x, y = event.x, event.y
        node = self.get_node_at(x, y)
        if node:
            self.selected_node = node

    def on_left_release(self, event):
        self.selected_node = None

    def on_double_click(self, event):
        x, y = event.x, event.y
        node = self.get_node_at(x, y)
        if node:
            # rename node
            pass
        edge = self.get_edge_at(x, y)
        if edge:
            # change weight
            pass
        pass

    def on_mouse_motion(self, event):
        if self.selected_node:
            self.selected_node.x = event.x
            self.selected_node.y = event.y

    def get_node_at(self, x, y):
        g = self.graphs[self.current_graph]
        for node in g.nodes:
            if node.point_is_inside(x, y):
                return node
        return None

    def get_edge_at(self, x, y):
        # TODO : get edge
        pass

    def update(self):
        print('RUN')
        self.canvas.delete('all')
        self.draw_graph()
        self.root.after(16, self.update)