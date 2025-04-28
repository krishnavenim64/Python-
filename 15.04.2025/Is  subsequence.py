Class Solution:

    Def isSubsequence(self, s: str, t: str) -> bool:

        I, j = 0, 0

        While i < len(s) and j < len(t):

            If s[i] == t[j]:

                I += 1

            J += 1

        Return i == len(s)


