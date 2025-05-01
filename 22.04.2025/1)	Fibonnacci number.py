Class Solution(object):

    Def fib(self, n):

        If n == 0:

            Return 0

        If n == 1:

            Return 1

        A, b = 0, 1

        For _ in range(2, n + 1):

            A, b = b, a + b

        Return b

