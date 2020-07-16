"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare input with value of node
        # if value < node
        if value < self.value:
            # we need left
            # if no left child,             
            if self.left == None:
            # wrap and 'park' val self.left
                self.left = BSTNode(value)
            # else is child
            else:
            # call left child insert method
                self.left.insert(value)
        # elif value >= node,
        else:
            # need right
            # see no right, 
            if self.right == None:
                # wrap and 'park'
                self.right = BSTNode(value)
            # else is child
            # call right child insert method
            else:
                self.right.insert(value)
        # if no node to compare value to, wrap in node and 'park' it


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        
        # check if less/left
        if target < self.value:
            if self.left:
                # recurse to continue to check left for target
                return self.left.contains(target)

        # check if more/right
        else:
            if self.right:
                # recurse to continue to check right for target
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # max would be equivalent to right-most value
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # # Call the function `fn` on the value of each node
    # def for_each(self, fn):
    #     fn(self.value)
    #     if self.left != None:
    #         self.left.for_each(fn)
    #     if self.right != None:
    #         self.right.for_each(fn)

    def for_each(self, fn):
        # DFT: LIFO
        stack = []
        stack.append(self)
        
        # so long as nodes,
        # more to traverse
        while len(stack) > 0:
            # pop top node
            current = stack.pop()
            
            # add current right child first
            if current.right:
                stack.append(current.right)

            # add left
            if current.left:
                stack.append(current.left)

            # call anon funct
            fn(current.value)

    
    def iterative_bft_for_each(self, fn):
        from collections import deque
        # BFT: FIFO 
        # use a queue to facil ordering of elems
        queue = deque()
        queue.append(self)

        while len(queue) > 0:
            current = queue.popleft()
        
        # add left first
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
        fn(current.value)



    # Part 2 ----------------------=========++++++++###########&&&&&&&&&&&&@@@@@@@@@@@@@@

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.left.in_order_print(node.left)
        print(node.value)
        if node.right:
            self.right.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        from collections import deque
        queue = deque()
        queue.append(self)
        while len(queue) > 0:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(self.value)
        if self.left:
            self.left.dft_print(self.left.value)
        if self.right:
            self.right.dft_print(self.right.value)


    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left != None:
            node.left.dft_print(node.left)
        if node.right != None:
            self.right.dft_print(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left != None:
            self.post_order_dft(node.left)
        if node.right != None:
            self.post_order_dft(node.right)
        print(node.value)
