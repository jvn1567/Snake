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

    def peekBack(self):
        if self.size == 0:
            raise Exception('No items in list.')
        return (self.back.x, self.back.y)

class Snake:
    def __init__(self):
        self.coords = PointList() # front of list is back of snake
        self.reset()

    def eat(self, x, y):
        self.coords.push(x, y)
    
    def move(self, x, y):
        self.coords.push(x,y)
        self.coords.pop()

    def head(self):
        return self.coords.peekBack()

    def reset(self):
        while self.coords.size > 0:
            self.coords.pop()

    def contains(self, x, y):
        curr = self.coords.front
        while curr != None:
            if (x == curr.x and y == curr.y):
                return True
            curr = curr.next
        return False