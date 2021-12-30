import unittest
from unittest import TestCase

from src import main
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):

    @staticmethod
    def main():
        main.check()
        main.check0()
        main.check1()
        main.check2()
        main.check3()

    def test_get_graph(self):
        GraphA = DiGraph()
        GraphA.add_node(1)
        graphAlgo = GraphAlgo(GraphA)
        self.assertEqual(graphAlgo.get_graph().get_all_v().get(str(1)), GraphA.get_all_v().get(str(1)))

    def test_load_from_json(self):
        graphAlgo = GraphAlgo()
        graphAlgo.load_from_json("../data/A4.json")
        self.assertTrue(graphAlgo.get_graph().get_all_v().keys().__len__() > 0)

    def test_save_to_json(self):
        graphAlgo = GraphAlgo()
        graphAlgo.load_from_json("../data/A4.json")
        b = graphAlgo.save_to_json("../data/A6.json")
        self.assertTrue(b == True)

    def test_shortest_path(self):
        graphAlgo = GraphAlgo()
        graphAlgo.load_from_json("../data/A4.json")
        graphAlgo.get_graph().remove_node(2)
        graphAlgo.get_graph().remove_node(5)
        graphAlgo.get_graph().remove_node(7)
        graphAlgo.get_graph().remove_edge(13, 14)
        graphAlgo.get_graph().remove_edge(18, 67)
        graphAlgo.get_graph().remove_edge(120, 22)
        graphAlgo.get_graph().remove_edge(16, 15)
        tuple = graphAlgo.shortest_path(0, 9)
        self.assertTrue((tuple[0]) != float("inf"))

    def test_tsp(self):
        graphAlgo = GraphAlgo()
        graphAlgo.load_from_json("../data/A4.json")
        graphAlgo.get_graph().remove_node(2)
        graphAlgo.get_graph().remove_node(5)
        graphAlgo.get_graph().remove_node(7)
        graphAlgo.get_graph().remove_edge(13, 14)
        graphAlgo.get_graph().remove_edge(18, 67)
        graphAlgo.get_graph().remove_edge(120, 22)
        graphAlgo.get_graph().remove_edge(16, 15)
        tuple = graphAlgo.TSP([8, 9, 10])
        self.assertTrue(tuple is not None)

    def test_center_point(self):
        graphAlgo = GraphAlgo()
        graphAlgo.load_from_json("../data/A5.json")
        tuple = graphAlgo.centerPoint()
        self.assertTrue(tuple[0] == 40)
