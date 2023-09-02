class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        #loop thru word
        # search s for word
        #index . pop


        for word in dictionary:
            if word in s:
                s = s.replace(word, '$', 1)

            count = 0
            for char in s:
                if char.isalpha():
                    count += 1
        return count
