import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = [-x for x in stones]

        heapq.heapify(maxheap)
        print(maxheap)
        while len(maxheap) > 1:
            y= heapq.heappop(maxheap)
            x= heapq.heappop(maxheap)
            z = y - x
            heapq.heappush(maxheap,z)

        return -maxheap[0]
