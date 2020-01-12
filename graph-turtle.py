from math import *
from turtle import *

# Creating an oriented graph graph type
class Graph:

    #  Initilizing infinite value
    INF = 10**10

    #  Initilizing self
    def __init__(self):
        self.vertices = {}
        self.vertices_count = 0
        self.matrix = []

    #  Determening the ammount of vertices in a graph
    def vertices_amount(self):
        return self.vertices_count

    #  Adding vertex to a graph
    def add_vertex(self, vertex):
        self.vertices_count += 1
        self.vertices[vertex] = self.vertices_count - 1
        #  Expanding matrix
        for i in self.matrix:
            i.append(self.INF)
        self.matrix.append([self.INF]*self.vertices_count)

    #  Removing vertex from a graph
    def remove_vertex(self, vertex):
        #  Checking if vertex is in graph
        if vertex not in self.vertices:
            pass

        del self.matrix[self.vertices[vertex]]
        for i in self.matrix:
            del i[self.vertices[vertex]]
        vertex_val = self.vertices[vertex]
        for key in self.vertices:
            if self.vertices[key] > vertex_val:
                self.vertices[key] -= 1
        del self.vertices[vertex]
        self.vertices_count -= 1


    #  Setting edge value
    def set_edge_value(self, x, y, v):
        # Doing it twice, since graph is non-oriented
        self.matrix[self.vertices[y]][self.vertices[x]] = v
        self.matrix[self.vertices[x]][self.vertices[y]] = v

    #  Removing edge from graph
    def remove_edge(self, x, y):
        # Doing it twice, since graph is non-oriented
        self.matrix[self.vertices[y]][self.vertices[x]] = self.INF
        self.matrix[self.vertices[x]][self.vertices[y]] = self.INF

    #  Getting edge value
    def get_edge_value(self, x, y):
        return self.matrix[self.vertices[y]][self.vertices[x]]

    #  Determing if two vericies are adjacent
    def adjacent(self, x, y):
        return self.matrix[self.vertices[y]][self.vertices[x]] != self.INF

    #  Creating a list of all adjecnt vertecies to a vertex
    def neighbours(self, x):
        lst = []
        for y in range(self.vertices_count):
            if self.matrix[y][self.vertices[x]] != self.INF:
                lst.append(y)
        neighb = []
        for i in lst:
            for vertex, value in self.vertices.items():
                if value == i:
                    neighb.append(vertex)
        return neighb

    def __str__(self):
        output = ""
        for j in self.matrix:
           output += ' '.join([str(i) for i in j]) + '\n'
        return output

