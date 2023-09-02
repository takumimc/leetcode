class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numdict = {}
        for num in nums:
            numdict[num] = num
        longest = 0
        for num in nums:
            if numdict.get(num - 1) == None:
                l = 0
                while numdict.get(num + l) != None:
                    l += 1

                longest = max(l,longest)

        return longest

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0

        for n in nums:
            if(n - 1) not in numSet:
                l = 0
                while (n + l) in numSet:
                    l += 1

                longest = max(l,longest)

        return longest
