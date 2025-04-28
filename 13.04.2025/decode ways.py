Class Solution(object):

    Def numDecodings(self, s):

        “””

        :type s: str

        :rtype: int

        “””

        If s[0] == ‘0’:

            Return 0



        N = len(s)

        Dp = [0] * (n + 1)

        Dp[0] = dp[1] = 1



        For i in range(2, n + 1):

            One_digit = int(s[i-1])

            Two_digits = int(s[i-2:i])



            If one_digit:

                Dp[i] += dp[i-1]



            If 10 <= two_digits <= 26:

                Dp[i] += dp[i-2]



        Return dp[n]

