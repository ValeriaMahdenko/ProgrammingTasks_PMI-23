class List_Node:
    def __init__(self, value=None, next=None, prev=None):
        self._value = value
        self._next = next
        self._prev = prev

class Double_List:
    def __init__(self):
        #Constructor for the doubly-linked list.
        self._head = List_Node()
        self._tail = List_Node()
        self._head._next = self._tail
        self._tail._prev = self._head

    def __len__(self):
        #Size of list
        current = self._head._next
        count = 0
        while current != self._tail:
            count += 1
            current = current._next
        return count

    def insert(self, value, index):
        #Insert value into list.
        if type(index) != int:
            raise TypeError
        elif index > len(self):
            raise IndexError
        else:
            prev = self._head
            for i in range(index):
                prev = prev._next
            new_node = List_Node(value, prev._next, prev)
            prev._next = new_node
            new_node._next._prev = new_node

    def append(self, value):
        # Add value to end of list
        self.insert(value, len(self))

    def __str__(self):
        #For print
        result = '['
        current = self._head._next
        while current != self._tail:
            result += str(current._value)
            current = current._next
            if current != self._tail:
                result += ', '
        result += ']'
        return result

    def pop(self):
        #Pops the last node out of the list
        old_last_node = self._tail
        el = old_last_node._prev
        old_last_node._prev = None
        old_last_node = None
        self._tail = el

        return old_last_node

    def is_empty(self):
        #Checks if list is empty
        if len(self) == 0:
            return True
        else:
            return False

    def copy(self):
        #Makes a copy of the given list
        dl_copy = Double_List()
        for x in self:
            dl_copy.append(x)
        return dl_copy

    def __setitem__(self, index, value):
        #For modify entry in list, at given index
        if type(index) != int:
            raise TypeError
        elif index < 0 or index >= len(self):
            raise IndexError
        else:
            # index is good. Walk down the list, the correct number of times.
            current = self._head._next
            for i in range(index):
                current = current._next
            current._value = value

    def __getitem__(self, index):
        #For retrieve entry in list at given index
        if type(index) != int:
            raise TypeError
        elif index < 0 or index >= len(self):
            raise IndexError
        else:
            # index is good. Walk down the list, the correct number of times.
            current = self._head._next
            for i in range(index):
                current = current._next
            return current._value

    def remove(self, index):
        # Remove entry in list, at given index
        if type(index) != int:
            raise TypeError
        elif index < 0 or index >= len(self):
            raise IndexError
        else:
            if index == 0:
                element = self._head
                self._head = self._head._next
                del element
            else:
                prev = self._head
                for x in range(index):
                    prev = prev._next
                element = prev._next
                prev._next = element._next
                del element._value

    def __reversed__(self):
        #Reverse iterator for values in list
        current = self._tail._prev
        while current != self._head:
            yield current._value
            current = current._prev
