Class Solution:

    Def majorityElement(self, nums: List[int]) -> int:

        Hash = {}

        Res = majority = 0

        

        For n in nums:

            Hash[n] = 1 + hash.get(n, 0)

            If hash[n] > majority:

                Res = n

                Majority = hash[n]

        

        Return res

