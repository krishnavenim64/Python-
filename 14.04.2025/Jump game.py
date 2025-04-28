Class Solution:

    Def jump(self, nums):

        Count = 0

        Near = 0

        Far = 0



        While far < len(nums) – 1:

            Farthest = 0

            For i in range(near, far + 1):

                Farthest = max(farthest, i + nums[i])

            Near = far + 1

            Far = farthest

            Count += 1



        Return count
