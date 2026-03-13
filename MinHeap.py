class MinHeap:
    '''Class that implements a Min-Heap data structure.'''
    
    def __init__(self):
        self._array = []
        
    #Methods to extract index of nodes
    def _getParentIndex(self, index):
        '''Method that takes in input the index of an element into the heap and return the index of its parent.'''
        return (index - 1) // 2
        
    def _getLeftChildIndex(self, index):
        '''Method that takes in input the index of an element into the heap and return the index of its LEFT child.'''
        return 2*index + 1
    
    def _getRightChildIndex(self, index):
        '''Method that takes in input the index of an element into the heap and return the index of its RIGHT child.'''
        return 2*index + 2
        
    #Method to extract elements
    def _getParent(self, index):
        '''Method that takes in input the index of an element into the heap and return its parent.'''
        return self._array[self._getParentIndex(index)]
    
    def _getLeftChild(self, index):
        '''Method that takes in input the index of an element into the heap and return its LEFT child.'''
        return self._array[self._getLeftChildIndex(index)]
    
    def _getRightChild(self, index):
        '''Method that takes in input the index of an element into the heap and return its RIGHT child.'''
        return self._array[self._getRightChildIndex(index)]
        
    #Method to check nodes
    def _checkParent(self, index):
        ''' Method that takes in input the index of an element into the heap and return True iff it have a parent.'''
        return self._getParentIndex(index) >= 0
    
    def _checkLeftChild(self, index):
        ''' Method that takes in input the index of an element into the heap and return True iff it have a LEFT child.'''
        return self._getLeftChildIndex(index) < len(self._array)

            
    def _checkRightChild(self, index):
        ''' Method that takes in input the index of an element into the heap and return True iff it have a RIGHT child.'''
        return self._getRightChildIndex(index) < len(self._array)
            
    def _swapElements(self, idx1, idx2):
        '''Method that takes in input two indecies and execute the swap between the two elements identifed by the indicies.'''
        self._array[idx1], self._array[idx2] = self._array[idx2], self._array[idx1]
    
    def add(self, element):
        '''Method that takes in input a new element and add it at its correct position into the heap.'''
        self._array.append(element) #first: push the new element at the end
        
        index = len(self._array)-1 #last index of the heap
        while self._checkParent(index) and (self._array[index] < self._getParent(index)): #iff it has a parent and the last-one is smaller then its parent
            parent_index = self._getParentIndex(index)
            self._swapElements(index, parent_index) #execute the swap
            index = parent_index #new index for the while-loop
            
    def pop(self):
        '''Method that return the minimum element into the heap (root element) and reorganize the heap.'''
        if len(self._array)!=0: #check if the heap is empty
            root = self._array[0]
        else:
            return None
        
        if len(self._array)>1: #iff the heap has more than one element
            self._array[0] = self._array.pop() #swap and remove the last-one
        else:
            # if there is only one element, remove it simply from the array
            self._array.pop()
            
        index = 0
        while self._checkLeftChild(index): #untill it have child
            small = self._getLeftChildIndex(index)
            if self._checkRightChild(index):
                right = self._getRightChildIndex(index)
                if self._array[right] < self._array[small]: #if it has the right child and this one is smaller then the left-one
                    small = right #right-one become the small
            if self._array[small] < self._array[index]: #iff the element in small index is smaller then its parent
                self._swapElements(index, small) #execute the swap
                index = small #the new index for the while-loop
            else:
                break
            
        return root
    
    def describeHeap(self):
        '''Method that show for each node its child and parent (if they exists).'''
        if not self._array:
            print("(empty heap)")
            return
        
        n = len(self._array)
        
        for i in range(n):
            node = self._array[i]
            
            parent = None
            if i > 0:
                parent = self._array[(i-1)//2]
                
            left = None
            if 2*i + 1 < n:
                left = self._array[2*i + 1]
                
            right = None
            if 2*i + 2 < n:
                right = self._array[2*i + 2]
            
            print(f"nodo {node} -> parent: {parent}, left child: {left}, right child: {right}")
