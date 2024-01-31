"""
File: list_dictionary2.py
Description:  Dictionary implemented using a Python list, but without
try-except.
"""

from entry import Entry

class ListDict(object):
    """Dictionary implemented using a Python list."""

    def __init__(self):
        self._table = []

    def __getitem__(self, key):
        """Returns the value associated with key or
        returns None if key does not exist."""
        for entry in self._table:
            if entry.getKey() == key:
                return entry.getValue()
        return None

    def __delitem__(self, key):
        """Removes the entry associated with key."""
        index = 0
        for entry in self._table:
            if entry.getKey() == key:
                self._table.pop(index)
            index += 1

    def __setitem__(self, key, value):
        """Inserts an entry with key/value if key does
           not exist or replaces the existing value
           with value if key exists."""
        for entry in self._table:
            if entry.getKey() == key:
                entry.setValue(value)
                return
        entry = Entry(key, value)
        self._table.append(entry)

    def __contains__(self, key):
        """Return True if key is in the dictionary; return
           False otherwise"""
        for entry in self._table:
            if entry.getKey() == key:
                return True
        return False

    def __len__(self):
        """Returns number of items in the dictionary"""
        return len(self._table)

    def __str__(self):
        """Returns string representation of the dictionary"""
        if len(self._table) == 0:
            return "{}"
        resultStr = "{"
        for item in self._table:
            resultStr += str(item) + ", "
        return resultStr[:-2] + "}"

    def __iter__(self):
        """Iterates over the keys of the dictionary"""
        for item in self._table:
            yield item.getKey()
        
        

def main():
    d = ListDict()
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


