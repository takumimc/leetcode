import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [[(point[0] ** 2) + (point[1] **2),point[0],point[1]]
                 for point in points]
        heapq.heapify(dist)
        result = []

        for x in range(k):
            point = heapq.heappop(dist)
            coor = [point[1],point[2]]
            result.append(coor)

        return result
