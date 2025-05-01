Class Solution(object):

    Def sortColors(self, nums):

        R,w,b = 0,0,0

        For i in nums:

            If i == 0:

                R += 1

            Elif i == 1:

                W += 1

            Else :

                B += 1

        Nums[:r] = [0]*r 

        Nums[r:r+w]= [1]*w 

        Nums[r+w:] = [2]*b

        “””

        :type nums: List[int]

        :rtype: None Do not return anything, modify nums in-place instead.

        “””

          
