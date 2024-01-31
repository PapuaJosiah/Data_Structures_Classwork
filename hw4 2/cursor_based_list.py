"""
File: cursor_based_list.py
Description:  Cursor-based list utilizing a header node and a trailer node.
Author:  <PUT YOUR NAME HERE>
"""

# NOTE: Start with getCurrent, __len__, and insertAfter to help see if your code is working

from node2way import Node2Way

class CursorBasedList(object):
    """ Linked implementation of a positional list."""
    
    def __init__(self):
        """ Creates an empty cursor-based list with header and trailer nodes.
            The header and trailer nodes help reduce special cases because all"""
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
            raise AttributeError("Empty list has no previous item.")
        return self._current.getPrevious() != self._header
    
    def first(self):
        """Moves the cursor to the first item
        if there is one.
        Precondition:  the list is not empty."""
        if self._size==0:
            raise AttributeError("No values were found in the list.")
        else:
            self._current=self._header.getNext()
        
    def last(self):
        """Moves the cursor to the last item
        if there is one.
        Precondition:  the list is not empty."""
        if self._size==0:
            raise AttributeError("No values were found in the list.")
        else:
            self._current=self._trailer.getPrevious()

    def next(self):
        """Precondition: hasNext returns True.
        Postcondition: The current item is has moved to the right one item"""
        if self.hasNext()==False:
            raise AttributeError("There is no next item past this one.")
        self._current=self._current.getNext()

    def previous(self):
        """Precondition: hasPrevious returns True.
        Postcondition: The current item is has moved to the left one item"""
        if self.hasPrevious()==False:
            raise AttributeError("There is no item before this one.")
        self._current=self._current.getPrevious()

    def insertAfter(self, item):
        """Inserts item after the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        temp= Node2Way(item)
        if self._size==0:
            self._current= self._header
        temp.setPrevious(self._current)
        temp.setNext(self._current.getNext())
        self._current.setNext(temp)
        self._current=temp.getNext()
        self._current.setPrevious(temp)
        self._current=temp
        self._size+=1
        

    def insertBefore(self, item):
        """Inserts item before the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        if self._size==0:
            self.insertAfter(item)
        else:
            temp= Node2Way(item)
            temp.setPrevious(self._current.getPrevious())
            temp.setNext(self._current)
            self._current.setPrevious(temp)
            self._current=temp.getPrevious()
            self._current.setNext(temp)
            self._current=temp
            self._size+=1

    def getCurrent(self):
        """ Returns the current item without removing it or changing the
        current position.
        Precondition:  the list is not empty"""
        if self.isEmpty():
            raise AttributeError("No current in an empty list.")
        else:
            return self._current.getData()

    def remove(self):
        """Removes and returns the current item. Making the next item
        the current item if one exists; otherwise the tail item in the
        list is the current item.
        Precondition: the list is not empty."""
        if self._size==0:
            raise AttributeError("The list is empty.")
        temp=self._current
        if self.hasNext():
            self._current=temp.getNext()
        elif self.hasPrevious():
            self._current=temp.getPrevious()
        else:
            self._current=None
        tempPrevious=temp.getPrevious()
        tempPrevious.setNext(temp.getNext())
        tempNext=temp.getNext()
        tempNext.setPrevious(temp.getPrevious())
        temp.setNext(None)
        temp.setPrevious(None)
        self._size-=1
        return temp.getData()
        

    def replace(self, newItemValue):
        """Replaces the current item by the newItemValue.
        Precondition: the list is not empty."""
        if self.isEmpty():
            raise AttributeError("There are no values to replace")
        else:
            self._current.setData(newItemValue)

    def isEmpty(self):
        if self._size==0:
            return True
        else:
            return False
            

    def __len__(self):
        """ Returns the number of items in the list (excluding the header and
            trailer nodes).
        """
        return self._size

    def __str__(self):
        """Includes items from first through last. Remember that the
           header and trailer nodes don't contain actual data.
        """
        resultStr = ""
        temp = self._header.getNext()
        while temp != self._trailer: # stop when temp gets to trailer node
            resultStr += str(temp.getData()) + " "
            temp = temp.getNext()
        # replace below
        return resultStr
