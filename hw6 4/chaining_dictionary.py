"""
File: chaining_dictionary.py
Description:  Dictionary implemented using hashing with chaining
"""

from entry import Entry
from unordered_linked_list import UnorderedList

class ChainingDict(object):
    """Dictionary implemented using hashing with chaining."""

    def __init__(self, capacity = 8):
        self._capacity = capacity
        self._table = []
        for index in range(self._capacity):
            self._table.append(UnorderedList())
        self._size = 0
        self._index = None

    def __contains__(self, key):
        """Returns True if key is in the dictionary or
        False otherwise."""
        self._index = abs(hash(key)) % self._capacity
        entry = Entry(key, None)
        
        return self._table[self._index].search(entry)

    def __getitem__(self, key):
        """Returns the value associated with key or
        returns None if key does not exist."""
        if key in self:
            entry = Entry(key, None)
            entry = self._table[self._index].remove(entry)
            self._table[self._index].add(entry)
            return entry.getValue()
        else:
            return None 

    def __delitem__(self, key):
        """Removes the entry associated with key."""
        entry = Entry(key, None)
        if key in self:
            entry = Entry(key, None)
            entry = self._table[self._index].remove(entry)
            self._size -= 1

    def __setitem__(self, key, value):
        """Inserts an entry with key/value if key
        does not exist or replaces the existing value
        with value if key exists."""
        entry = Entry(key, value)
        if key in self:
            entry = self._table[self._index].remove(entry)
            entry.setValue(value)
        else:
            self._size += 1
        self._table[self._index].add(entry)

    def __len__(self):
        return self._size

    def __str__(self):
        resultStr = "{"
        for myList in self._table:
            for entry in myList:
                resultStr +=  str(entry) + ", "
        if len(resultStr) > 1:
            return resultStr[:-2] + "}"
        else:
            return "{}"

    def __iter__(self):
        """Iterates over the keys of the dictionary"""
        for myList in self._table:
            for entry in myList:
                yield entry.getKey()

                
def main():
    d = ChainingDict(3)
    d["Name"] = "Bob"
    d["Age"] = 26
    d["Color"] = "red"
    print("Items from iterator:")
    for item in d:
        print(item)
    print( d)
    print( "Expect True:", "Name" in d)
    print( "Expect Bob:", d["Name"])
    print( "Expect None:", d["Address"])
    d["Age"] = 27
    print( "Expect 27:", d["Age"])
    del d["Name"]
    del d["Address"]
    print (d)
    print("Items from iterator:")
    for item in d:
        print(item)
    return d

if __name__ == "__main__": d = main()


