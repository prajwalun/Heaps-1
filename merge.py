# The mergeKLists method merges k sorted linked lists into one sorted list.

# Use a min-heap to track the smallest node among the current heads of the lists.
# Wrap nodes in a NodeWrapper to enable comparison based on values.
# Pop the smallest node, attach it to the result, and push its next node if available.
# Continue until the heap is empty and return the merged list.

# TC: O(n log k) - n is total nodes, k is the number of lists.
# SC: O(k) - Space for the heap.


import heapq
from typing import List, Optional


class NodeWrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        res = ListNode(0)
        cur = res
        minHeap = []

        for lst in lists:
            if lst is not None:
                heapq.heappush(minHeap, NodeWrapper(lst))

        while minHeap:
            node_wrapper = heapq.heappop(minHeap)
            cur.next = node_wrapper.node
            cur = cur.next
            
            if node_wrapper.node.next:
                heapq.heappush(minHeap, NodeWrapper(node_wrapper.node.next))
        
        return res.next