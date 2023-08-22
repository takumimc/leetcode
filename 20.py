class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        starters =  []
        left = ['(','[','{']
        right = {
            ')':'(',
            ']':'[',
            '}':'{',
        }

        # for char in s:
        #     if char not in left and len(starters) == 0:
        #         return False
        #     if char in left:
        #         starters.insert(0, char)
        #     else:
        #         if right[char] == starters[0]:
        #             starters.pop(0)
        #         else:
        #             return False
        # if len(starters) == 0:
        #     return True
        # else:
        #     return False

        for char in s:
            if char in right:
                if starters and right[char] == starters[0] :
                    starters.pop(0)
                else:
                    return False
            else:
                starters.insert(0,char)
        return not starters
