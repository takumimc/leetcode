import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l = 1
        r = max(piles)
        mink = r

        while l <= r:
            k = l + r //2
            tot = 0
            for num in piles:
                tot += math.ceil(num/k)

            if tot <= h:
                mink = min(k,mink)
                r = k - 1
            else:
                l = k + 1

        return mink


import math
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l = 1
        r = max(piles)
        mink = r

        while l <= r:
            k = (l + r) //2
            tot = 0
            for num in piles:
                tot += math.ceil(num/k)

            if tot <= h:
                mink = min(k,mink)
                r = k - 1
            else:
                l = k + 1

        return mink
