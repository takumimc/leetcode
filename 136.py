class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = {
            '1': [],
            '2':  [],
        }

        for num in nums:
            if num in counts['2']:
                continue
            elif num in counts['1']:
                counts['2'].append(num)
                counts['1'].remove(num)
            else:
                counts['1'].append(num)

        return counts['1'][0]
