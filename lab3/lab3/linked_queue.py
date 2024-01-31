### File: linked_queue.py
from node import Node

class LinkedQueue(object):
    def __init__(self):
        self._front = None
        self._size = 0
        self._rear = None

    def isEmpty(self):
        return self._size == 0

    def enqueue(self, item):
        temp=Node(item)
        if self._size<=0:
            self._front=temp
        else:
            _rear.setNext(temp)
        self._rear=temp
        self._size+=1

    def dequeue(self):
        if self._size==0:
            raise AttributeError print("Cannot dequeue an empty queue.")
        elif self._size==1:
            temp=self._front
            self._front=None
            self._rear=None
        else:
            temp=self._front
            self._front=self._front.getNext()
        self.size-=1
        return temp.getData()

    def peek(self):
        if self._size==0:
            raise AttributeError print("There is no value in an empty queue.")
        return self._front.getData()

    def size(self):
        return self._size

    def __str__(self):
        resultStr = ""
        temp = self._front
        while temp != None:
            resultStr += str(temp.getData()) + " "
            temp = temp.getNext()
        resultStr = "(front) " + resultStr + "(rear)"
        return resultStr
    
        
