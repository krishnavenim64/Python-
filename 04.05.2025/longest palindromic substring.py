Class Solution(object):

    Def longestPalindrome(self, s):

        “””

        :type s: str

        :rtype: str

        “””

        N = len(s)

        If n == 0:

            Return “”

        

        Start = 0

        Max_length = 1

        

        Dp = [[False] * n for _ in range(n)]

        

        For i in range(n):

            Dp[i][i] = True  # Single characters are palindromes

        

        For length in range(2, n + 1):

            For i in range(n – length + 1):

                J = i + length – 1

                

                If s[i] == s[j]:

                    If length == 2:

                        Dp[i][j] = True

                    Else:

                        Dp[i][j] = dp[i + 1][j – 1]

                    

                    If dp[i][j] and length > max_length:

                        Start = i

                        Max_length = length

        

        Return s[start:start + max_length]

