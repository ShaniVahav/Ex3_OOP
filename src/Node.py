import copy


class Node:

    def __init__(self, node_id, p: tuple):
        self.key = node_id
        self.pos = p
        self.flag = -1

    def copyNode(self):
        return copy.deepcopy(self)

    def toString(self):
        return "key = " + str(self.key) + ", pos = " + str(self.pos)
