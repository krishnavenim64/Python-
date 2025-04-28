Class Solution:

    Def isMatch(self, s, p):

        Dp = [[False for _ in range(len(p)+1)] for i in range(len(s)+1)]

        Dp[0][0] = True

        For j in range(1, len(p)+1):

            If p[j-1] != ‘*’:

                Break

            Dp[0][j] = True

                

        For i in range(1, len(s)+1):

            For j in range(1, len(p)+1):

                If p[j-1] in {s[i-1], ‘?’}:

                    Dp[i][j] = dp[i-1][j-1]

                Elif p[j-1] == ‘*’:

                    Dp[i][j] = dp[i-1][j] or dp[i][j-1]

        Return dp[-1][-1]

