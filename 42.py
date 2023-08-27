class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = 1
        tot = 0
        taken = 0
        while l < len(height) - 2:

            if r == len(height) - 1:
                l += 1
                r = l + 1
            elif height[l] < height[r]:
                l += 1
                r = l + 1
            elif height[r] < height[l]:
                taken += height[r]
                r += 1
            else:
                h = min(height[l],height[r])
                tot += (r - l) * h - taken
                l = r
                r = l +1

        return tot


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        tot = 0
        l = 0
        r = 1
        taken = 0
        while l < len(height) - 1:

            if height[l] == 0:
                l += 1
                r = l +1
            elif r == len(height) - 2:
                l += 1
                r = l + 1
            elif height[r] >= height[l]:
                h = min(height[r],height[l])
                cur = (r - l - 1) * h - taken
                tot += cur

                l = r
                r = l + 1
                taken = 0
            elif height[r] < height[l]:
                taken += height[r]
                r += 1

        return tot
