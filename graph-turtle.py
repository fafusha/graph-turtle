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

#  Generating vertices of n-polygon
def coordinate_generation(graph, r,  xo = 0, yo  = 0):
    out = []
    xc = [xo + r*cos(2*pi*i/graph.vertices_amount()) for i in range(graph.vertices_amount())]
    yc = [yo + r*sin(2*pi*i/graph.vertices_amount()) for i in range(graph.vertices_amount())]
    for i in range(graph.vertices_amount()):
        out.append([xc[i], yc[i]])
    return out

#  Intitlazing turtle

bob = Turtle()
bob.hideturtle()
bob.penup()
bob.shape("circle")
bob.speed("fast")
#  Drawing graph
def draw_graph(graph):
    #  Determening coordinates of vertices
    vertcord =  coordinate_generation(graph, 200, xo = 0, yo  = 0)
    #  Drawing vertices
    for i in vertcord:
        bob.setpos(i[0], i[1])
        bob.stamp()
    #  Drawing edges
    for key1 in graph.vertices:
        for key2 in graph.vertices:
            if graph.adjacent(key1, key2):
                bob.setpos(vertcord[graph.vertices[key1]])
                bob.pendown()
                bob.setpos(vertcord[graph.vertices[key2]])
                bob.penup()


def dijkstra(graph, start, end):
    INF = graph.INF
    n = graph.vertices_amount()

    #  Creating a list of distances to all verticies
    dist = [INF]*n

    #  Setting distance to starting position to 0
    dist[graph.vertices[start]] = 0

    #  Intilizaing visited verticies
    used = [False] * n
    min_dist = 0;
    min_vertex = start
    while min_dist < INF:
        i = graph.vertices[min_vertex]
        used[i] = True

        #  Iterating through all vertices
        for k in graph.vertices:
            j = graph.vertices[k]
            if dist[i] + graph.matrix[i][j] < dist[j]:
                dist[j] = dist[i] + graph.matrix[i][j]
        min_dist = INF

        #  Determening the minimum distance
        for k in graph.vertices:
            j = graph.vertices[k]
            if not used[j] and dist[j] < min_dist:
                min_dist = dist[j]
                min_vertex = k

    if dist[graph.vertices[end]] != INF:
        return dist[graph.vertices[end]]
    else:
        return -1

graph = Graph()
graph.add_vertex("1")
graph.add_vertex("2")
graph.add_vertex("3")
graph.add_vertex("4")
graph.add_vertex("5")
graph.add_vertex("6")
graph.add_vertex("7")
graph.add_vertex("8")
graph.add_vertex("9")


graph.set_edge_value("1", "2", 5)
graph.set_edge_value("1", "5", 6)
graph.set_edge_value("7", "9", 12)
graph.set_edge_value("1", "9", 18)
graph.set_edge_value("1", "7", 1)
#graph.add_vertex("Hello")
#graph.set_edge_value("Hello", "8", 1)
#graph.remove_vertex("7")
#graph.add_vertex("7")

draw_graph(graph)
print(dijkstra(graph, "1", "9"))
#  Interacting with user
a = ""
while a != "0":
    a = input()
    eval(a)
    bob.clear()
    draw_graph(graph)
#graph.add_vertex("11")
#graph.set_edge_value("5", "11", 12)
