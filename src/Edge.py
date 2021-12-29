class Edge:

    def __init__(self):
        self.src_node = None
        self.dst_node = None
        self.weight = 0

    def Edge(self, node_in, node_out, w):
        self.src_node = node_in
        self.dst_node = node_out
        self.weight = w


