class MaxHeap:
    def __init__(self, items=[]):
        #super().__init__()
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatup(len(self.heap) - 1)

    def __floatup(self, index):
        print(f"index is {index}")
        #print(self.heap[index])
        parent = index // 2
        if index <= 1:
            return
        elif self.heap[index] > self.heap[parent]:
            self.__swap(index, parent)
            self.__floatup(parent)

    def __swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


m = MaxHeap([3, 21, 44, 1, 45, 77, 95])
print(m.heap)
