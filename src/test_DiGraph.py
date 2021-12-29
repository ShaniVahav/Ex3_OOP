from unittest import TestCase

from src.DiGraph import DiGraph


class TestDiGraph(TestCase):

    def test_all_out_edges_of_node(self):
        graphA = DiGraph()
        graphA.add_node(1)
        graphA.add_node(2)
        graphA.add_edge(1, 2, 5)
        self.assertTrue(graphA.all_out_edges_of_node(1).keys().__len__() > 0)

    def test_all_in_edges_of_node(self):
        graphA = DiGraph()
        graphA.add_node(1)
        graphA.add_node(2)
        graphA.add_edge(1, 2, 5)
        self.assertTrue(graphA.all_in_edges_of_node(2).keys().__len__() > 0)

    def test_get_all_v(self):
        graphA = DiGraph()
        graphA.add_node(1)
        self.assertTrue(graphA.get_all_v().keys().__len__() > 0)

    def test_v_size(self):
        graphA = DiGraph()
        graphA.add_node(1)
        self.assertTrue(graphA.v_size() > 0)

    def test_get_mc(self):
        graphA = DiGraph()
        graphA.add_node(1)
        graphA.add_node(2)
        self.assertTrue(graphA.get_mc() == 2)

    def test_add_edge(self):
        graphA = DiGraph()
        graphA.add_node(1)
        graphA.add_node(2)
        graphA.add_edge(1, 2, 5)
        self.assertTrue(graphA.edges.keys().__len__() > 0)

    def test_add_node(self):
        graphA = DiGraph()
        graphA.add_node(1)
        graphA.add_node(2)
        graphA.add_edge(1, 2, 5)
        self.assertTrue(graphA.nodes.keys().__len__() > 0)

    def test_remove_node(self):
        graphA = DiGraph()
        graphA.add_node(2)
        graphA.remove_node(2)
        self.assertTrue(graphA.nodes.keys().__len__() == 0)

    def test_remove_edge(self):
        graphA = DiGraph()
        graphA.add_node(1)
        graphA.add_node(2)
        graphA.add_edge(1, 2, 5)
        graphA.remove_edge(1, 2)
        self.assertTrue(graphA.edges.keys().__len__() > 0)
