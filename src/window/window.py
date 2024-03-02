import tkinter as tk
import json
from PIL import Image, ImageTk
from tools.graph import *

DEFAULT_HEIGHT = 600
DEFAULT_WIDTH = 800

class GraphWindow:
    def __init__(self, height=DEFAULT_HEIGHT, width=DEFAULT_WIDTH):
        self.current_graph = '__DEFAULT__'
        self.graphs = { '__DEFAULT__': Graph() }
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
        self.canvas.bind("<Double-Button-1>", self.on_double_click)
        self.canvas.bind("<MouseWheel>", self.on_wheel_motion)
        self.canvas.bind("<Motion>", self.on_mouse_motion)


    def add_graph(self, name, graph: Graph):
        self.graphs[name] = graph

    def draw_graph(self):
        self.canvas.delete("all")
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
        pass

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

    def on_wheel_motion(self, event):
        print(event)
        pass

    def on_mouse_motion(self, event):
        print(event.x, event.y)
        pass

    def get_node_at(self, x, y):
        g = self.graphs[self.current_graph]
        for node in g.nodes:
            if node.point_is_inside(x, y):
                return node
        return None

    def get_edge_at(self, x, y):
        # TODO : get edge
        pass

    def run(self):
        self.root.mainloop()