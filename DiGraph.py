from abc import ABC

from src.GraphInterface import GraphInterface
from src.Node import Node


class DiGraph(GraphInterface):

    def __init__(self):
        self.mc = 0
        self.nodes = {}
        self.edges = {}
        self.oposite = {}
        self.largestIndex = -1
        self.numberOfNodes = 0
        self.numberOfEdges = 0

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.edges[str(id1)]

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.oposite[str(id1)]

    def get_all_v(self) -> dict:
        return self.nodes

    def v_size(self) -> int:
        return self.numberOfNodes

    def e_size(self) -> int:
        return self.numberOfEdges

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        try:
            if (self.nodes.get(str(id1)) is None) or (self.nodes.get(str(id2)) is None):
                raise NotImplementedError
            if self.all_out_edges_of_node(id1).get(str(id2)) is not None:
                raise NotImplementedError
            self.edges[str(id1)][str(id2)] = (id2, weight)
            self.oposite[str(id2)][str(id1)] = (id2, weight)
            self.numberOfEdges += 1
            self.mc += 1
            return True
        except NotImplementedError:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        try:
            if self.nodes.get(str(node_id)) is None:
                self.nodes[str(node_id)] = Node(node_id, pos)
                self.edges[str(node_id)] = {}
                self.oposite[str(node_id)] = {}
                self.numberOfNodes += 1
                self.mc += 1
                if node_id > self.largestIndex:
                    self.largestIndex = node_id
                return True
            else:
                raise NotImplementedError
        except NotImplementedError:
            return False

    def remove_node(self, node_id: int) -> bool:
        try:
            del (self.nodes[str(node_id)])
            IteratorDict2 = self.all_in_edges_of_node(node_id)
            IteratorDict = self.all_out_edges_of_node(node_id)
            for id_Dest in IteratorDict:
                del (self.oposite[id_Dest][str(node_id)])
            for node_in in IteratorDict2:
                del (self.edges[node_in][str(node_id)])
            del (self.oposite[str(node_id)])
            del (self.edges[str(node_id)])
            if self.largestIndex == node_id:
                max = 0
                for nodeId in self.get_all_v():
                    if (nodeId > max):
                        max = nodeId
                self.largestIndex = max
                self.numberOfNodes -= 1
                self.mc += 1
            return True
        except KeyError:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        try:
            del self.edges[str(node_id1)][str(node_id2)]
            del self.oposite[str(node_id2)][str(node_id1)]
            self.numberOfEdges -= 1
            self.mc += 1
            return True
        except KeyError:
            return False
