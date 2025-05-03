Class Solution(object):

    Def canJump(self, nums):

        “””

        :type nums: List[int]

        :rtype: bool

        “””

        High=0

        For i in range(len(nums)-1):

            If i<=high:

                H= i+nums[i]

                If high>=len(nums)-1:

                   Return True

                High=max(h,high)

            Else:

                Return False

        If high>=len(nums)-1:

            Return True

        Return False    



