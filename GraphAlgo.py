import copy
import heapq
import json
import sys
from random import uniform, random
import random
from typing import List

import matplotlib.pyplot as plt

from src import GraphInterface
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface


def checkMinMax(Xs, Ys, node_id, xScale, yScale):
    x = Xs.get(str(node_id))
    y = Ys.get(str(node_id))
    if x < xScale[0]:
        xScale[0] = x
    else:
        if x > xScale[1]:
            xScale[1] = x
    if y < yScale[0]:
        yScale[0] = y
    else:
        if y > yScale[1]:
            yScale[1] = y

    # ******************************************************************************#


class GraphAlgo(GraphAlgoInterface):
    graphName = ""

    def __init__(self, otherGraph=None):
        if otherGraph is not None:
            self.graph = otherGraph
        else:
            self.graph = DiGraph()

    def get_graph(self) -> GraphInterface:
        return self.graph

    # ******************************************************************************#
    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, "r") as f:
                data = json.load(f)

            Edges = data['Edges']  # a dict
            Nodes = data['Nodes']  # a dict

            counterNode = 0
            counterEdge = 0

            for n in Nodes:
                if 'pos' not in n:
                    pos = None
                else:
                    p = n['pos'].split(',')
                    pos = (float(p[0]), float(p[1]), float(p[2]))
                self.graph.add_node(n['id'], pos)
                counterNode += 1

            for e in Edges:
                self.graph.add_edge(e['src'], e['dest'], e['w'])
                counterEdge += 1

            self.graph.numberOfNodes = counterNode
            self.graph.numberOfEdges = counterEdge
            self.graphName = file_name
            return True
        except NotImplementedError:
            return False

    # ******************************************************************************#
    def save_to_json(self, file_name: str) -> bool:
        try:
            graph = self.get_graph()
            dict = {"Edges": [], "Nodes": []}
            for node in graph.get_all_v().values():
                if node.pos is None:
                    dict["Nodes"].append({"id": str(node.key)})
                else:
                    dict["Nodes"].append(
                        {"pos": str(node.pos[0]) + "," + str(node.pos[1]) + "," + str(node.pos[2]),
                         "id": str(node.key)})

                for edge in graph.edges.get(str(node.key)).values():  # (str(node_out), weight)
                    dict["Edges"].append({"src": node.key, "w": edge[1], "dest": edge[0]})
            with open(file_name, 'w') as f:
                json.dump(dict, f, indent=2)
            return True
        except NotImplementedError:
            return False

    # ***********************<< Auxiliary Functions >>******************************#
    def dijkstra(self, id1):
        if self.graph.nodes.get(str(id1)) is None:
            return None
        maximumDistance = -sys.maxsize
        size = self.graph.largestIndex + 1
        boolList = [False] * size
        distanceList = [sys.maxsize] * size
        distanceList[id1] = 0
        pq = []
        heapq.heappush(pq, (distanceList[id1], id1))
        while not pq.__eq__([]):
            currentTouple = heapq.heappop(pq)
            currentIdsrc = currentTouple[1]
            boolList[currentIdsrc] = True  # (4, (1,2,3))
            for edge in self.graph.all_out_edges_of_node(currentIdsrc).values():
                if boolList[edge[0]] is False:
                    currentDestId = edge[0]  # (id2,weight)
                    currentW = edge[1]
                    if distanceList[currentDestId] > distanceList[currentIdsrc] + currentW:  # dis from id1
                        distanceList[currentDestId] = distanceList[currentIdsrc] + currentW
                        heapq.heappush(pq, (distanceList[currentDestId], currentDestId))
                        if distanceList[currentDestId] > maximumDistance:
                            maximumDistance = distanceList[currentDestId]
        return maximumDistance, distanceList

    def minimumFromGivenList(self, distance: List[float], node_lst):
        lowestValue = sys.maxsize
        ansNodeKey = -1
        for nodeId in node_lst:
            node = self.graph.get_all_v().get(str(nodeId))  # node - > node data for knowing tag
            if distance[nodeId] < lowestValue and node.flag is False:
                lowestValue = distance[nodeId]
                ansNodeKey = nodeId
        ansNode = self.graph.get_all_v().get(str(ansNodeKey))
        ansNode.flag = True
        return lowestValue, ansNodeKey

    # ******************************************************************************#
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if (self.graph.nodes.get(str(id1)) is None) or (self.graph.nodes.get(str(id2)) is None):
            return float('inf'), []
        if self.graph.all_out_edges_of_node(id1).get(str(id2)) is not None:
            return float('inf'), []
        size = self.graph.largestIndex + 1  # we want the represent of all the keys in the list
        prevList = [-1] * size
        boolList = [False] * size
        distanceList = [sys.maxsize] * size
        distanceList[id1] = 0
        pq = []
        heapq.heappush(pq, (distanceList[id1], id1))
        while not pq.__eq__([]):
            currentTouple = heapq.heappop(pq)
            currentIdsrc = currentTouple[1]
            boolList[currentIdsrc] = True  # (4, (1,2,3))
            for edge in self.graph.all_out_edges_of_node(currentIdsrc).values():
                if boolList[edge[0]] is False:
                    currentDestId = edge[0]  # (id2,weight)
                    currentW = edge[1]
                    if distanceList[currentDestId] > distanceList[currentIdsrc] + currentW:  # dis from id1
                        distanceList[currentDestId] = distanceList[currentIdsrc] + currentW
                        prevList[currentDestId] = currentIdsrc
                        heapq.heappush(pq, (distanceList[currentDestId], currentDestId))
        listAns = []
        current = id2
        while prevList[current] != -1:
            tempList = [prevList[current]]
            listAns = tempList + listAns
            current = prevList[current]
        if prevList[id2] == -1:
            return float('inf'), []
        listAns = listAns + [id2]
        return distanceList[id2], listAns

    # ******************************************************************************#
    def TSP(self, node_lst: List[int]) -> (List[int], float):
        choosenNodeIndex = -1
        copyList = copy.deepcopy(node_lst)
        ansList = []
        finalSum = sys.maxsize
        for times in range(min(20, len(node_lst))):
            tempSum = 0
            tempList = []
            for nodeId in node_lst:
                nodeFromList = self.graph.nodes.get(str(nodeId))
                nodeFromList.flag = False
            if len(copyList) != 0:
                choosenNodeIndex = random.choice(copyList)
                print(choosenNodeIndex)
                copyList.remove(choosenNodeIndex)
            listDistance = self.dijkstra(choosenNodeIndex)[1]
            choosenNode = self.graph.get_all_v().get(str(choosenNodeIndex))
            choosenNode.flag = True
            tempList.append(choosenNodeIndex)
            for i in range(1, len(node_lst)):
                tuple = self.minimumFromGivenList(listDistance, node_lst)  # (lowestValue,ansNodeKey)
                lowestValue = tuple[0]
                idlowestNode = tuple[1]
                tempSum += lowestValue
                tempList.append(idlowestNode)
                listDistance = self.dijkstra(idlowestNode)[1]
            if tempSum < finalSum:
                finalSum = tempSum
                ansList = tempList
        return ansList, finalSum

    # ******************************************************************************#
    def centerPoint(self) -> (int, float):
        ans = ()
        minimum = sys.maxsize
        for nodeId in self.graph.get_all_v().keys():
            tuple = self.dijkstra(int(nodeId))  # return (maximumDistance,listDistance)
            if tuple[0] < minimum:
                minimum = tuple[0]
                ans = (int(nodeId), tuple[0])
        return ans

    # ******************************************************************************#
    def plot_graph(self) -> None:
        graph = self.get_graph()
        if graph.numberOfNodes == 0:
            return

        Xs = {}
        Ys = {}
        xScale = [sys.float_info.max, sys.float_info.min]
        yScale = [sys.float_info.max, sys.float_info.min]
        nodes = graph.get_all_v()
        for node in nodes.values():
            if node.pos is not None:
                Xs[str(node.key)] = node.pos[0]
                Ys[str(node.key)] = node.pos[1]
                checkMinMax(Xs, Ys, node.key, xScale, yScale)

            else:
                xdata = uniform(35.212111165456015, 32.10788938151261)
                ydata = uniform(35.212111165456015, 32.10788938151261)
                Xs[str(node.key)] = xdata
                Ys[str(node.key)] = ydata
                checkMinMax(Xs, Ys, node.key, xScale, yScale)

        x_bigest_dist = xScale[1] - xScale[0]
        y_bigest_dist = yScale[1] - yScale[0]
        bigestDist = max(x_bigest_dist, y_bigest_dist)

        """
        paint the nodes
        """
        for i in Xs:
            x = Xs.get(i)
            y = Ys.get(i)
            plt.plot(x, y, color='r', marker='.')
            plt.text(x, y, str(i), color='r')

        """
        paint the edges with the right direction
        """
        edges = self.graph.edges
        for node_in in edges.keys():
            n_in = self.graph.get_all_v().get(node_in)
            X1 = Xs.get(str(n_in.key))
            Y1 = Ys.get(str(n_in.key))
            for node_out in edges.get(node_in).keys():
                n_out = self.graph.get_all_v().get(node_out)
                X2 = Xs.get(str(n_out.key))
                Y2 = Ys.get(str(n_out.key))

                dx = X2 - X1
                dy = Y2 - Y1

                plt.arrow(X1, Y1, dx, dy, width=.001 * bigestDist, head_width=.01 * bigestDist,
                          length_includes_head=True)

        plt.title(self.graphName, color='r')
        plt.show()
