class Node():

    def __init__(self, d, n, p):
        self.data = d
        self.next_node = n
        self.prev_node = p

    def __str__(self):
        return str(self.data)