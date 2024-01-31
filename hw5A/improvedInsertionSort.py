'''
    Programmer:  <PUT YOUR NAME HERE>
    File:  improvedimprovedInsertionSort.py
    Description:  Sorts myList in ascending order using an improved insertion sort
    that decouples the finding of the correct spot from making room to insert by:
    1) finding the right spot in the sorted part for the item to be inserted by doing
       a "modified" binary-search of the sorted part, then
    2) make room to insert at the right spot and insert the itemToInsert by using
       a loop to shift the right-side of the sorted part up one index to make room
       for the itemToInsert (NOTE: Don't use list pop and insert Python list methods)
'''

def improvedInsertionSort(myList):
    """Rearranges the items in myList so they are in ascending order"""
    ### ADD YOUR CODE HERE

    
import random

def shuffle(myList):
    for fromIndex in range(len(myList)):
        toIndex = random.randint(0,len(myList)-1)
        temp = myList[fromIndex]
        myList[fromIndex] = myList[toIndex]
        myList[toIndex] = temp
    

import time

print("improvedInsertionSort Timings")            
aList = list(range(15000,0,-1))
print( "\nBefore sorting list: ",end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
start = time.perf_counter()
improvedInsertionSort(aList)
end = time.perf_counter()
print( "sorted list:", end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
print( "Time to sort",end - start,"seconds")

print( "\nBefore sorting list: ", end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
start = time.perf_counter()
improvedInsertionSort(aList)
end = time.perf_counter()
print( "sorted list:", end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
print( "Time to sort",end - start,"seconds")

aList = list(range(15000,0,-1))
shuffle(aList)
print( "\nBefore sorting (random) list: ",end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
start = time.perf_counter()
improvedInsertionSort(aList)
end = time.perf_counter()
print( "sorted list:",end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
print( "Time to sort",end - start,"seconds")

aList = list(range(15000,0,-1))
shuffle(aList)
print( "\nBefore sorting (random) list: ",end='')
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
start = time.perf_counter()
improvedInsertionSort(aList)
end = time.perf_counter()
print( "sorted list:",end="")
print( aList[0],aList[1],aList[2], '...',aList[-3], aList[-2],aList[-1])
print( "Time to sort",end - start,"seconds")

input("Hit <Enter>-key to end")
