Class Solution:

    Def isMatch(self, s, p):

        Dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]



        Dp[0][0] = True

        For j in range(1, len(p) + 1):

            If p[j – 1] == ‘*’:

                Dp[0][j] = dp[0][j – 2]



        For i in range(1, len(s) + 1):

            For j in range(1, len(p) + 1):

                If p[j – 1] in {s[i – 1], ‘.’}:

                    Dp[i][j] = dp[i – 1][j – 1]

                Elif p[j – 1] == ‘*’:

                    Dp[i][j] = dp[i][j – 2] or (dp[i – 1][j] and p[j – 2] in {s[i – 1], ‘.’})



        Return dp[len(s)][len(p)]



