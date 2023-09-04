class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.values = nums.sort()
        self.k = k

    def add(self, val: int) -> int:
        self.values.append(val)
        self.values.sort()
        return self.values[-self.k]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
