"""
File: cursor_based_list.py
Description:  Cursor-based list utilizing a header node and a trailer node.
Author:  <PUT YOUR NAME HERE>
"""

from node2way import Node2Way

class CursorBasedList(object):
    """ Linked implementation of a positional list."""
    
    def __init__(self):
        """ Creates an empty cursor-based list."""
        self._header = Node2Way(None)
        self._trailer = Node2Way(None)
        self._trailer.setPrevious(self._header)
        self._header.setNext(self._trailer)
        self._current = None
        self._size = 0

    def hasNext(self):
        """ Returns True if the current item has a next item.
            Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no next item")
        return self._current.getNext() != self._trailer

    def hasPrevious(self):
        """ Returns True if the current item has a previous item.
            Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no previous item")
        return self._current.getPrevious() != self._header
    
    def first(self):
        """Moves the cursor to the first item
        if there is one.
        Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no first item")
        self._current = self._header.getNext()
        
    def last(self):
        """Moves the cursor to the last item
        if there is one.
        Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no last item")
        self._current = self._trailer.getPrevious()

    def next(self):
        """Precondition: hasNext returns True.
        Postcondition: The current item is has moved to the right one item"""
        if not self.hasNext():
            raise AttributeError("No Next item")
        self._current = self._current.getNext()

    def previous(self):
        """Precondition: hasPrevious returns True.
        Postcondition: The current item is has moved to the left one iten"""
        if not self.hasPrevious():
            raise AttributeError("No Previous item")
        self._current = self._current.getPrevious()

    def insertAfter(self, item):
        """Inserts item after the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        if self._size == 0:
            self._current = self._header
        temp = Node2Way(item)
        temp.setPrevious(self._current)
        temp.setNext(self._current.getNext())
        self._current.getNext().setPrevious(temp)
        self._current.setNext(temp)
        self._size += 1
        self._current = temp

    def insertBefore(self, item):
        """Inserts item before the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        if self._size > 0:
            self._current =  self._current.getPrevious()
        self.insertAfter(item)

    def getCurrent(self):
        """ Returns the current item without removing it or changing the
        current position.
        Precondition:  the list is not empty"""
        if self.isEmpty():
            raise AttributeError("Empty list has no current item")
        return self._current.getData()

    def remove(self):
        """Removes and returns the current item. Making the next item
        the current item if one exists; otherwise the tail item in the
        list is the current item.
        Precondition: the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no current item to remove")
        temp = self._current
        temp.getPrevious().setNext(temp.getNext())
        temp.getNext().setPrevious(temp.getPrevious())
        if temp.getNext() == self._trailer:
            self._current = temp.getPrevious()
        else:
            self._current = temp.getNext()
        self._size -= 1
        if self._size == 0:
            self._current = None
        return temp.getData()

    def replace(self, newItemValue):
        """Replaces the current item by the newItemValue.
        Precondition: the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no current item to replace")
        self._current.setData(newItemValue)

    def isEmpty(self):
        return self._size == 0            

    def __len__(self):
        """ Returns the number of items in the list."""
        return self._size

    def __str__(self):
        """Includes items from first through last."""
        strResult = ""
        current = self._header.getNext()
        while current != self._trailer:
            strResult += str(current.getData()) + " "
            current = current.getNext()
        return strResult
