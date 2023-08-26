class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1

        tot = 0
        while l < r:
            cur = (r - l) * min(height[r],height[l])
            if cur > tot:
                tot = cur

            if height[r] > height[l]:
                l += 1
            else:
                r -=1

        return tot
