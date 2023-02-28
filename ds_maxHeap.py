class maxHeap():

    def __init__(self, items=[]):
        self.heap = [0]
        for item in items:
            self.heap.append(item)
            self.__floatUp(len(self.heap) - 1)
    def __str__(self):
        return str(self.heap)

    def push(self, item):
        self.heap.append(item)
        if len(self.heap) > 2 :
            self.__floatUp(len(self.heap) - 1 )

    def __floatUp(self, index):
        parent = index // 2
        if index <= 1:
            return None
        elif self.heap[index] > self.heap[parent]:
            self.swap(index, parent)
            self.__floatUp(parent)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]


    def pop(self):
        if len(self.heap) > 2:
            self.swap(1, len(self.heap) - 1)
            max = self.heap.pop()
            self.__bubbleDown(1)

        elif len(self.heap) == 2:
            max = self.heap.pop()
        else:
            max = False
        return max

    def __bubbleDown(self, index):
        lc = index * 2
        rc = index * 2 + 1
        largest = index

        if len(self.heap) > lc and self.heap[lc] > self.heap[largest]:
            largest = lc
        if len(self.heap) > rc and self.heap[lc] > self.heap[largest]:
            largest = rc
        if largest != index:
            self.swap(index, largest)
            self.__bubbleDown(largest)

x = maxHeap([10, 3, 5, 45, 21, 2, 6])
print(x)
x.push(78)
print(x)
print(x.pop())
print(x)
print(x.pop())