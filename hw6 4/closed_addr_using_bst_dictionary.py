""" File:  closed_addr_using_bst_dictionary.py
    Use to implement ClosedAddrUsingBSTDict class which should have a subset of
    dictionary methods: __setitem__, __getitem__, __delitem__, __contains__,
    __iter__, __len__, and __str__.

    Hint:  Model the ClosedAddrUsingBSTDict class off of the ChainingDict class.

    NOTE:  Each hash table (self._table) slot contains a BinarySearchTree object.
    A BinarySearchTree object already stores key and value (payload of TreeNode)
    pairs, unlike a UnorderedList object in the ChainingDict.  Thus, you will not
    need to create Entry objects like we did in the ChainingDict.  Plus, a
    BinarySearchTree object already has a dictionary interface we can use, but
    don't use the double_underscore names (e.g., __setitem__, __getitem__, etc.)
    -- use them as dictionaries (e.g., myDict[k] = value instead of __setitem__, or
    "if k in myDict" instead of __contains__, etc.). 

    Alternatively, you can use the get, put, delete, etc. methods.
"""

from binary_search_tree import BinarySearchTree

class ClosedAddrUsingBSTDict(object):
    """Dictionary implemented using hashing with chaining."""

    def __init__(self, capacity = 8):
        self._capacity = capacity
        self._table = []
        for index in range(self._capacity):
            self._table.append(BinarySearchTree())
        self._size = 0
        self._index = None

    def __contains__(self, key):
        """Returns True if key is in the dictionary or
        False otherwise."""
        # Remember home address of key 
        self._index = abs(hash(key)) % self._capacity

        # calls __contains__ of BinarySearchTree dictionary interface        
        return key in self._table[self._index]

    def __getitem__(self, key):
        """Returns the value associated with key or
        returns None if key does not exist."""
        pass # REPLACE WITH YOUR CODE

    def __delitem__(self, key):
        """Removes the entry associated with key."""
        pass # REPLACE WITH YOUR CODE

    def __setitem__(self, key, value):
        """Inserts an entry with key/value if key
        does not exist or replaces the existing value
        with value if key exists."""
        pass # REPLACE WITH YOUR CODE

    def __len__(self):
        pass # REPLACE WITH YOUR CODE

    def __str__(self):
        pass # REPLACE WITH YOUR CODE

    def __iter__(self):
        """Iterates over the keys of the dictionary"""
        pass # REPLACE WITH YOUR CODE
                
def main():  # Simple test code to see if dictionary working
    d = ClosedAddrUsingBSTDict()
    d["Name"] = "Bob"
    d["Age"] = 26
    d["Color"] = "red"
    print(d)
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
