‘’’

Approach 1: Check for divergence if n == 2^31 – 1 then not happy 



‘’’



Class Solution(object):

    Def split(self, n): 

        Nums = [0] 

        While n > 0: 

            Q = n // 10

            R = (n % 10) ** 2 

            Nums.append(nums[-1] + r) 

            N = q 

        Return nums[-1]



    Def isHappy(self, n):

        “””

        :type n: int

        :rtype: bool

        “””

        Memo = set()

        While n < 2e31 – 1: 

            If n == 1: 

                Return True 

            If n in memo: 

                Return False 



            Memo.add(n) 

            N = self.split(n)



        Return False  

