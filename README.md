This code contains a Python implementation of a maximum heap in an array representation:
1. building a max heap: The idea is to start from the first 'non leaf' node (element) and heapify the subtrees recursively by permuting the parent's value with the maximum value of its children.
2. Max heap sorting: We extract the first element (maximum value) of the heap and heapify the remaining elements, ensuring that the maximum value always appears first in the array. We repeat this process until all elements have been extracted (the array is empty).
