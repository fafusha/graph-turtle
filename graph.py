class Graph(object):
    ""
    vertices: set
    edges: set
    ""

    # A Graph type object'''
    def __init__(self, vertices, edges, directed=False):
        # A new graph with given vertices and sets
        if not isinstance(vertices, set):
            raise TypeError("vertices must be a set")  # fix err msg
        # A copy of this is in add_edges KEEP TRACK OF CHANGES {
        if not isinstance(edges, set):
            raise TypeError("edges must be a set")  # fix err msg
        for edge in edges:
            if not isinstance(edge, tuple):
                raise TypeError("each edge must be a tuple")  # fix err msg
            # if len(edge) != 2:
            # ^^^^^^^^^ is python smart ?
            l_tester = len(edge) != 2
            if l_tester:
                raise TypeError("each edge only 2 elements")  # fix err msg
        # }
        if not isinstance(directed, bool):
            raise TypeError("directed must be bool")  # fix err msg

        self.vertices = vertices
        self.edges = edges
        self.directed = directed
        self.adj_l = {}  # adjacency list

        self.add_edges(edges)
        # add a map of every element to its index, for simplicity?
        # tbh i think this is dumb...
        # figure out a way to do an ass map in a list
        # do this with adjacency lists
        # also add numpy on top of this
        # Add type checking for vertices edges and directed have to be set()
        # raise TypeError

    # fix
    # def __str__(self):
    #   # add a print statement do so its prints edges and vertices
    #  pass
    # fix
    # def __eq__(self, ):
        # ???
        # do equality based on vertices names and paths, look into this
        # if graphs have same vertices names and paths..., but keep in ind issue of indexing of whatever t
        # e name is, like i wanted to do a map or some shit'''
        # ???
    #   pass

    def add_vertices(self, vertices):
        # fix name func
        # a set() can be passed or a single variable
        # catch type errors
        # RAISE ERR IF VERTEX EXISTS?????
        if isinstance(vertices, set):
            for v in vertices:
                self.vertices.add(v)
        else:
            self.vertices.add(vertices)

    def add_edges(self, edges):
        # fix name func
        # a set() can be passed on or a single variable
        # add error message if sug path exists? (optional)
        # Code taken form__int__KEEPTR ACK OF CHANGES {
        if isinstance(edges, set):
            for edge in edges:
                # possibly combine two if statements together, review later
                # decided not to change because errors are different ???
                if not isinstance(edge, tuple):
                    raise TypeError("each edge must be a tuple")  # fix err msg
                if len(edge) != 2:
                    raise TypeError("each edge must have only beg and the end")  # fix err msg
                v1, v2 = edge
                if v1 not in self.vertices:
                    raise NameError("v1 does nto belong to a graph")  # fix err msg
                if v2 not in self.vertices:
                    raise NameError("v2 does nto belong to a graph")  # fix err msg
                if v1 not in self.adj_l:
                    self.adj_l[v1] = {v2}
                else:
                    self.adj_l[v1].add(v2)
                if not self.directed:
                    if v2 not in self.adj_l:
                        self.adj_l[v2] = {v1}
                    else:
                        self.adj_l[v2].add(v1)
        elif isinstance(edges, tuple):
            if len(edges) != 2:
                raise TypeError("each edge must have only beg and the end")  # fix err msg
            v1, v2 = edges
            if v1 not in self.vertices:
                raise NameError("v1 does nto belong to a graph")  # fix err msg
            if v2 not in self.vertices:
                raise NameError("v2 does nto belong to a graph")  # fix err msg
            if v1 not in self.adj_l:
                self.adj_l[v1] = {v2}
            else:
                self.adj_l[v1].add(v2)
            if not self.directed:
                if v2 not in self.adj_l:
                    self.adj_l[v2] = {v1}
                else:
                    self.adj_l[v2].add(v1)
        # think about ifs
        elif not isinstance(edges, tuple):
            raise TypeError("edge must be set or single variable")  # fix err msg

    def is_vertex(self, vertex):
        # fix name func
        return vertex in self.vertices

    def is_edge(self, edg):
        # fix name func
        # !!! think about err checking, maybe a write a a very nice func that catches all these...
        # def check(params)...
        # def check(params)..!!!
        # params ex: edges = Trues, vertices = False, etc...
        if not isinstance(edg, tuple):
            raise TypeError("edge must a tuple")  # fix err msg
        if len(edg) != 2:
            raise TypeError("edge must be a tuple of length 2 ")  # fix err msg
        return edg in self.edges

    def is_adjacent(self, v1, v2):
        # one line solution may cause bugs for dir and undirected graphs look into it
        return v2 in self.adj_l[v1]

# DRY don't repeat yourself
# also add type checking when inputting
# Add an edge type checker function
# edge_correct_input? or something
# For doc string use ""  quotes operator

