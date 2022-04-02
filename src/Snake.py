class Node:
    def __init__(self, nextNode, x, y):
        self.next = nextNode
        self.x = x
        self.y = y

class PointList:
    def __init__(self):
        self.front = None
        self.back = self.front
        self.size = 0;

    def push(self, x, y):
        if self.back is None:
            self.front = Node(None, x, y)
            self.back = self.front
        else:
            self.back.next = Node(None, x, y)
            self.back = self.back.next
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception('No items in list.')
        self.front = self.front.next
        self.size -= 1

    def peekX(self):
        if self.size == 0:
            raise Exception('No items in list.')
        return self.front.x

    def peekY(self):
        if self.size == 0:
            raise Exception('No items in list.')
        return self.front.y

class Snake:
    def __init__(self):
        self.coords = PointList() # front of list is back of snake

    def eat():
        # add no pop
        a = None
    
    def move():
        # add and pop
        a = None

    def reset():
        # clear all
        a = None

    def head():
        return {1, 1}
