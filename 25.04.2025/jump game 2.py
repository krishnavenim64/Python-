Class Solution(object):

    Def canJump(self, nums):

        “””

        :type nums: List[int]

        :rtype: bool

        “””

        Count = 0

        Flag = True

        For i in range(len(nums)-2,-1,-1):

            If (nums[i] == 0) & (flag):

                Count = 1

                Flag = False

            Elif count:

                If nums[i]>count:

                    Flag = True

                    Count = 0

                Else:

                    Count += 1

        If count or not(flag):

            Return False

        Else:

            Return True

