# The findKthLargest method finds the kth largest element in a list.

# Maintain a min-heap of size k for the k largest elements.
# Heapify the first k elements, then iterate through the rest:
# - If an element is larger than the heap's smallest, replace it.
# Return the smallest element in the heap, which is the kth largest.

# TC: O(n log k) - Heap operations for n-k elements.
# SC: O(k) - Space for the heap.


import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        
        return heap[0]