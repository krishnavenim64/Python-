Class Solution(object):

    Def maxSubArray(self, nums):

        “””

        :type nums: List[int]

        :rtype: int

        “””

        maxSubSum = nums[0]

        res = nums[0]

        n = len(nums)

        

        for i in range(1, n):

            maxSubSum = max(maxSubSum + nums[i], nums[i])

            res = max(res, maxSubSum)

            

        return res

