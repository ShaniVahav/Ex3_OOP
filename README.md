# Ex3_OOP
Same as Ex2_OOP just in Python
## About the project.
Given a json file, which contains values of vertices and directed weighted edges, we construct a directed and weighted graph.
There are several editing options on the graph, such as adding / subtracting a vertex or edge, creating a new edge or a new vertex.
In addition to all the edits, various algorithms can be performed on the graph, such as finding the middle vertex,
the shortest path between two vertices, and even the traveling salesman problem (ie: https://en.wikipedia.org/wiki/Travelling_salesman_problem).

## Literature review.
In our project we mainly based on **Ex2_OOP project**, in which we used several sources, some of which are:
1. https://www.youtube.com/watch?v=EFg3u_E6eHU
2. https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/
3. https://docs.oracle.com/javase/tutorial/uiswing/components/frame.html

## Main Functions.
### save\load_from_json(file_name):
Saves\loads the graph in JSON format to a file.

### shortest_path(A,B):
Returns the shortest path from node A to node B using Dijkstra's Algorithm.  
(Dijkstra's Algorithm info: https://en.wikipedia.org/wiki/Dijkstra's_algorithm)

### TSP(nodes):
Finds the shortest path that visits all the nodes in the list 'nodes'.

### centerPoint:
Finds the node that has the shortest distance to it's farthest node.

### plot_graph:
Plots the graph.
If the nodes have a position, the nodes will be placed there.
Otherwise, they will be placed in a random but elegant manner.


## Class diagram.
![image](https://user-images.githubusercontent.com/92265738/147703008-dce8e5fe-6ab3-46e3-afc8-f80b934c03e4.png)

