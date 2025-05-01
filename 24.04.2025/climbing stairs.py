Class Solution(object):

    Def climbStairs(self, n):

        If n==1:

            Return 1

        Elif n==2:

            Return 2

        A,b=1,2

        For i in range(3,n+1):

            A,b=b,a+b

        Return b        

