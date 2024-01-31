""" Heap Sort """
from binheap import BinHeap
# methods: BinHeap(), insert(item), delMin(), isEmpty(), size()

def heapSort(myList):
    # Create an empty heap
    minHeap = BinHeap()

    # Add all list items to minHeap
    for item in range(len(myList)):
        minHeap.insert(item)

    # delMin heap items back to list in sorted order
    for index in range(len(myList)):
        myList[index]=minHeap.delMin()

