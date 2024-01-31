# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
import unittest

# this heap takes key value pairs, we will assume that the keys are integers
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def buildHeap(self,alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        # print(len(self.heapList), i)
        while (i > 0):
            # print(self.heapList, i)
            self.percDownRec(i)
            i = i - 1
        # print(self.heapList,i)
                        
    def percUpRec(self, i):
        if i//2>0:
            if self.heapList[i]<self.heapList[i//2]:
                tmp=self.heapList[i//2]
                self.heapList[i//2]=self.heapList[i]
                self.heapList[i]=tmp
            i=i//2
            return self.percUpRec(i)
        else:
            return self.heapList
        
        
            
##    def percUp(self,i):
##        while i // 2 > 0:
##            if self.heapList[i] < self.heapList[i//2]:
##               tmp = self.heapList[i // 2]
##               self.heapList[i // 2] = self.heapList[i]
##               self.heapList[i] = tmp
##            i = i // 2
##
 
    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUpRec(self.currentSize)

    def percDownRec(self,i):
        if (i*2)<=self.currentSize:
            mc=self.minChild(i)
            if self.heapList[i]>self.heapList[mc]:
                tmp=self.heapList[i]
                self.heapList[i]=self.heapList[mc]
                self.heapList[mc]=tmp
            i=mc
            return self.percDownRec(i)
        else:
            return self.heapList
            
        
##    def percDown(self,i):
##        while (i * 2) <= self.currentSize:
##            mc = self.minChild(i)
##            if self.heapList[i] > self.heapList[mc]:
##                tmp = self.heapList[i]
##                self.heapList[i] = self.heapList[mc]
##                self.heapList[mc] = tmp
##            i = mc
                
    def minChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDownRec(1)
        return retval
        
    def isEmpty(self):
        if currentSize == 0:
            return True
        else:
            return False

    def size(self):
        return self.currentSize

    def __str__(self):
        return str(self.heapList[1:])

class FooThing:
    def __init__(self,x,y):
        self.key = x
        self.val = y

    def getKey(self):
        return self.key

    def getValue(self):
        return self.val

    def setValue(self, newValue):
        self.val = newValue

    def __eq__(self,other):
        if self.key == other.key:
            return True
        else:
            return False

    def __ne__(self,other):
        if self.key != other.key:
            return True
        else:
            return False

    def __lt__(self,other):
        if self.key < other.key:
            return True
        else:
            return False

    def __le__(self,other):
        if self.key <= other.key:
            return True
        else:
            return False

    def __gt__(self,other):
        if self.key > other.key:
            return True
        else:
            return False
        
    def __ge__(self,other):
        if self.key >= other.key:
            return True
        else:
            return False
        
    def __hash__(self):
        return self.key

class TestBinHeap(unittest.TestCase):
    def setUp(self):
        self.theHeap = BinHeap()
        self.theHeap.insert(FooThing(8,'e'))                               
        self.theHeap.insert(FooThing(7,'f'))                  
        self.theHeap.insert(FooThing(6,'t'))
        self.theHeap.insert(FooThing(10,'s'))                               
        self.theHeap.insert(FooThing(9,'d'))                  
        self.theHeap.insert(FooThing(1,'x'))
        self.theHeap.insert(FooThing(2,'y'))
        self.theHeap.insert(FooThing(3,'z'))

    def testInsert(self):
        assert self.theHeap.currentSize == 8

    def testDelmin(self):
        assert self.theHeap.delMin().getValue() == 'x'
        assert self.theHeap.delMin().getValue()  == 'y'
        assert self.theHeap.delMin().getValue()  == 'z'
        assert self.theHeap.delMin().getValue()  == 't'

    def testMixed(self):
        myHeap = BinHeap()
        myHeap.insert(9)
        myHeap.insert(1)
        myHeap.insert(5)
        myHeap.insert(3)
        myHeap.insert(2)
        myHeap.insert(8)
        assert myHeap.delMin() == 1
        myHeap.insert(2)
        myHeap.insert(7)
        assert myHeap.delMin() == 2
        assert myHeap.delMin() == 2
        assert myHeap.delMin() == 3

    def testDupes(self):
        myHeap = BinHeap()
        myHeap.insert(9)
        myHeap.insert(1)
        myHeap.insert(8)
        myHeap.insert(1)
        assert myHeap.currentSize == 4
        assert myHeap.delMin() == 1
        assert myHeap.delMin() == 1
        assert myHeap.delMin() == 8

    def testBuildHeap(self):
        myHeap = BinHeap()
        myHeap.buildHeap([9,5,6,2,3,7,8,4,10,1,11])
        f = myHeap.delMin()
        # print("f = ", f)
        assert f == 1
        assert myHeap.delMin() == 2
        assert myHeap.delMin() == 3
        assert myHeap.delMin() == 4
        assert myHeap.delMin() == 5                        
        
if __name__ == '__main__':
    suite = unittest.makeSuite(TestBinHeap)
    unittest.TextTestRunner().run(suite)
    
