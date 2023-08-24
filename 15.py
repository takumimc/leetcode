class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        output = []

        for i,num in enumerate(nums):
            target = 0 - num
            l = i + 1
            r = len(nums) - 1
            while l < len(nums) - 2:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                elif nums[l] + nums[r] == target:
                    output.append([num,nums[l],nums[r]])

        return output
