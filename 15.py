class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        output = []
        nums.sort()
        for i,num in enumerate(nums):
            if i > 0 and num == nums[i -  1]:
                continue

            l = i + 1
            r = len(nums) - 1
            while l < r:
                tot = num  + nums[l] + nums[r]
                if tot > 0:
                    r -= 1
                elif tot < 0:
                    l += 1
                else:
                    output.append([num,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1

        return output


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        nums.sort()
        prev = None
        for i in nums:
            if i == prev:
                continue
            prev = i
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tot = i + nums[l] + nums[r]
                if tot > 0:
                    r -= 1
                elif tot < 0:
                    l += 1
                else:
                    output.append([i,nums[l],nums[r]])
                    l += 1

        return output
