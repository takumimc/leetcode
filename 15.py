class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        output_set = []
        s = 0
        l = 1
        r = 2

        while s != len(nums) - 2:
            tot = nums[s] + nums[l] + nums[r]

            if tot == 0 and set({s,l,r}) not in output_set:
                output_set.append(set({s,l,r}))
                output.append([nums[s],nums[l],nums[r]])
            elif nums[s] == 0 and nums[l] == 0 and nums[r] == 0 and [0,0,0] not in output:
                output.append[0,0,0]

            if r < len(nums) - 1:
                r += 1
            elif r == len(nums) - 1:
                if l < len(nums) - 2:
                    l += 1
                    r = l + 1
                else:
                    s += 1
                    l = s + 1
                    r = l + 1

        return output
