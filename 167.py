class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0
        r = len(numbers) - 1
        while numbers[l] + numbers[r] != target:
            condition = numbers[l] + numbers[r]
            if condition >  target:
                r -= 1
            elif condition < target:
                l += 1
        return [l+1,r+1]
