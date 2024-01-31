""" File:  openAddrHashDictTester.py
    Author:  Mark Fienup
    Description:  Simple test program to see if the modified OpenAddrHashDict
    class is able to perform like the built-in Python dictionary with respect to
    iterating and printing entries in the order added.
"""

from random import randint
from open_addr_hash_dictionary import OpenAddrHashDict

def main():
    # Create Python dictionary and modified OpenAddrHashDict for comparison
    aDict = {}
    myDict = OpenAddrHashDict(2000)

    # Randomly add (calls __setitem__) 1000 times, but some might be duplicates
    for i in range(1000):
        key = randint(1, 1000)
        aDict[key] = key
        myDict[key] = key

    # Quick check to see if the sizes match
    print("len(aDict)", len(aDict))
    print("len(myDict)", len(myDict))

    # Match lists of keys from each dictionary -- should call __iter__ to make these
    match = True
    aDictKeyList = list(aDict)
    myDictKeyList = list(myDict)

    # Compare lists to see if their __iter__ order completely match
    for index in range(len(aDictKeyList)):
        if aDictKeyList[index] != myDictKeyList[index] or aDict[aDictKeyList[index]] != myDict[myDictKeyList[index]]:
            match = False
            print("Mismatch at index", index, 'on key', aDictKeyList[index])
            break
    if match:
        print("Both dictionaries __iter__ orders match after adds")

    # Randomly delete some items and re-compare dictionaries
    deleteCnt = 0
    for i in range(500):
        key = randint(1, 1000)
        if key in aDict:
            del aDict[key]
            del myDict[key]
            deleteCnt += 1
    print("\n", "="*50)
    print("After", deleteCnt, "deletes.")
    
    print("len(aDict)", len(aDict))
    print("len(myDict)", len(myDict))
    match = True
    aDictKeyList = list(aDict)
    myDictKeyList = list(myDict)
    for index in range(len(aDictKeyList)):
        if aDictKeyList[index] != myDictKeyList[index] or aDict[aDictKeyList[index]] != myDict[myDictKeyList[index]]:
            match = False
            print("Mismatch at index", index, 'on key', aDictKeyList[index])
            break
    if match:
        print("Both dictionaries __iter__ orders match after deletes")
    
main()  # start program running...
