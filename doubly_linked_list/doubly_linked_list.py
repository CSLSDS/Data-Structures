"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.head is None:
            new = ListNode(value)
            self.head = new
            return
        new = ListNode(value)
        new.next = self.head
        self.head.prev = new
        self.head = new
        
        # create node
        new = ListNode(value)
        self.length += 1
        # if list empty set head and tail to new node
        if self.head != None and self.tail != None:
            self.head = new
            self.tail = new
        else:
            # set next to head
            new.next = self.head
            self.head.prev = new
            self.head = new         
            
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.head is None:
            val = None
            return val
        elif self.head is self.tail:
            val = self.head.value
            self.head = None
            self.head = None
        else:
            val = self.head.value
            self.head = self.head.next
            self.head.prev = None
        
        self.length -= 1
        return val

    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.head is None:
            new = ListNode(value)
            self.head = new
            return
        end = self.head
        while end.next is not None:
            end = end.next
        new = ListNode(value)
        end.next = new
        new.prev = end
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.tail:
            val = None
            return None
        elif self.tail is self.head:
            val = self.tail.value
            self.tail = None
            self.head = None
        else:
            val = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return val
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        self.length -= 1

        if self.head == self.tail:
            self.head = None
            self.head = None
        elif node is self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass