Class Solution(object):

    Def sortArrayByParityII(self, nums):

        “””

        :type nums: List[int]

        :rtype: List[int]

        “””

        # Variables

        N = len(nums)

        I, j = 0, n-1



        # Logic

        While (i < n and j > 0):

            If (nums[i]%2 == 0 and nums[j]%2 != 0):

                I += 2

                J -= 2

            Elif (nums[i]%2 != 0 and nums[j]%2 == 0):

                Nums[i], nums[j] = nums[j], nums[i]

                I += 2

                J -= 2

            Elif (nums[i]%2 == 0 and nums[j]%2 == 0):

                I += 2

            Else :

                J -= 2

        

        Return nums

