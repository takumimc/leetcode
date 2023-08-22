class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == '':
            return 0
        result = 1
        sub = s[0]
        l = 0
        r = 1
        while r < len(s):
            if s[r] not in sub:
                sub += s[r]
                r += 1
                if len(sub) > result:
                    result = len(sub)
            else:
                l += 1
                r = l + 1
                sub = s[l]

        return result
