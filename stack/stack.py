"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# # Python list/array implementation

# class Stack:
#     # first in - last out
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         # returns num of elements in the stack
#         return self.size

#     def push(self, value):
#         # adds item to the top of the stack
#         self.storage.append(value)
#         self.size += 1

#     def pop(self):
#         # removes and returns element at top of stack
#         if self.size > 0:
#             self.size -= 1
#             return self.storage.pop()

# LinkedList implementation

from singly_linked_list import Node, LinkedList

class Stack:
    # first in - last out
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        # returns num of elements in the stack
        return self.size

    def push(self, value):
        # adds item to the top of the stack
        self.storage.add_to_tail(value)
        self.size += 1

    def pop(self):
        # removes and returns element at top of stack
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_tail()
