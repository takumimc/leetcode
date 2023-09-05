from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.numbers = SortedList()

    def addNum(self, num: int) -> None:
        self.numbers.add(num)

    def findMedian(self) -> float:
        x = len(self.numbers)
        if x % 2 != 0:
            x = x//2
            return self.numbers[x]
        else:
            x = x//2
            med = (self.numbers[x - 1] + self.numbers[x])/2
            return med



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

class MedianFinder:

    def __init__(self):
        self.numbers = []

    def addNum(self, num: int) -> None:
        self.numbers.append(num)

    def findMedian(self) -> float:
        self.numbers.sort()
        x = len(self.numbers)
        if x % 2 != 0:
            x = x//2
            return self.numbers[x]
        else:
            x = x//2
            med = (self.numbers[x - 1] + self.numbers[x])/2
            return med



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
