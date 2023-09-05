from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        units = [-unit for unit in counts.values()]
        time = 0

        heapq.heapify(units)
        q = deque()

        while units or q:
            if len(units) > 0:
                current_task = heapq.heappop(units)
                if current_task + 1 != 0:
                    q.append([current_task + 1, time + n])


            if q and q[0][1] == time:
                task  = q.popleft()
                heapq.heappush(units,task[0])
            time += 1

        return time
