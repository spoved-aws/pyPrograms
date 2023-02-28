class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class regularList():

    def __init__(self, r = None):
        self.root = r
        self.size = 0

    def __add__(self, item):
        new_node = Node(item, self.root)
