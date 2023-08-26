class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        r = len(nums) - 1
        l = 0
        while l <= r:
            c = (l + r)//2
            if nums[c] < target:
                l = c + 1
            elif nums[c] > target:
                r = c - 1
            else:
                return c
        return -1


nums = [-1,0,3,5,9,12]
target = 2
x = Solution()
print(x.search(nums,target))
