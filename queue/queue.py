"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

## Python list/array implementation:::

# class Queue:
#     # first in - first out 
#     def __init__(self):
#         self.size = 0
#         # self.storage = ?
#         self.storage = []
    
#     def __len__(self):
#         # returns num of elements in the queue
#         return self.size

#     def enqueue(self, value):
#         # adds an element to the back of the queue
#         self.storage.append(value)
#         self.size += 1

#     def dequeue(self):
#         # removes and returns the element at the front of the queue
#         if self.size > 0:
#             self.size -= 1
#            return self.storage.pop(0)

import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'singly_linked_list'))  # what
from singly_linked_list import *

# LinkedList() implementation
#from singly_linked_list import Node, LinkedList

class Queue:
    # first in - first out 
    def __init__(self):
        self.size = 0
        # self.storage = ?
        self.storage = LinkedList()
    
    def __len__(self):
        # returns num of elements in the queue
        return self.size

    def enqueue(self, value):
        # adds an element to the back of the queue
        
        # initialize instance of storage/LinkedList();
        #     call 'add_to_tail' method to enqueue 'value' defined in params
        self.storage.add_to_tail(value)
        self.size += 1

    def dequeue(self):
        # removes and returns the element at the front of the queue

        # initialize instance of 
        if self.size > 0:
            self.size -= 1
        return self.storage.remove_head()