class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        pre = []
        post = []


        for num in nums:
            if len(pre) == 0:
                pre.append(num)
            else:
                pre.append(num*pre[-1])

        for i in range(len(nums),1,-1):
            if len(post) == 0:
                post.append(nums[i - 1])
            else:
                post.insert(0,post[0] *nums[i - 1])
        print('pre',pre)
        print('post',post)
        for i in range(len(nums)):
            if i == 0:
                output.append(post[0])
            elif i == len(nums) - 1:
                output.append(pre[i-1])
            else:
                output.append(pre[i-1] * post[i])

        return output
