from MinHeap import MinHeap

def extract_order_sublist(seq):
    '''Function to extract from a sequence of random numbers an ordered sub-sequence.
    Return the ordered sub-sequence extract and the sub-sequence not ordered.'''
    ordered = [seq[0]]
    not_ordered = []

    for i in range(1, len(seq)):
        if seq[i] >= ordered[-1]:
            ordered.append(seq[i])
        else:
            not_ordered.append(seq[i])

    return ordered, not_ordered

def vanilla_partitioning(seq):
    '''Function to partition an input sequence into its sorted subsequences.'''
    D = list()
    
    while True:
        o, no = extract_order_sublist(seq)
        D.append(o)
        if not no:
            break
        seq = no
        
    return D

def partitioning_optimized(seq):
    '''Optimized version of the partitioning function. 
    Like in the Timsort algorithm implemented in Python, instead of recreating the unsorted list each time, it uses a single pointer that loops through the original list.'''
    if not seq:
        return []
    
    D = []
    current_run = [seq[0]]
    
    for i in range(1, len(seq)):
        if seq[i] >= current_run[-1]:
            # The element continues the current ordered sequence
            current_run.append(seq[i])
        else:
            # The order is broken: save the sequence and start a new one
            D.append(current_run)
            current_run = [seq[i]]
            
    #Add the last run
    D.append(current_run)
    
    return D
    
def merge_sublists(D):
    heap = MinHeap()
    result = []

    # Inizialized heap with the first element of each sub-sequences
    for i, sub in enumerate(D):
        if sub:
            # tuple: (value, index_list, index_element)
            heap.add((sub[0], i, 0))

    # Until the heap is not empty
    while len(heap._array) != 0:
        popped = heap.pop()
        if popped is None:
            break
        value, list_idx, elem_idx = popped
        result.append(value)

        # if there are other elements in the sublist from which the extracted value came from
        if elem_idx + 1 < len(D[list_idx]):
            next_tuple = (
                D[list_idx][elem_idx + 1],
                list_idx,
                elem_idx + 1
            )
            # Add the next element to the heap
            heap.add(next_tuple)

    return result
    
def Vanilla_CascadeSort(x):
    list_ord_subseq = vanilla_partitioning(x)
    return merge_sublists(list_ord_subseq)

def Optimized_CascadeSort(x):
    list_ord_subseq = partitioning_optimized(x)
    return merge_sublists(list_ord_subseq)