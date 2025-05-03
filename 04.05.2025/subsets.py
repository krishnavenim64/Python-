Class Solution(object):

    Def subsets(self, nums):

        “””

        :type nums: List[int]

        :rtype: List[List[int]]

        “””

        N = len(nums)

        Total = 1 << n

        Result = []



        For mask in range(total):

            Subset = [

                Nums[i] for i in range(n) if mask & (1 << i)

            ]

            Result.append(subset)



        Return result



