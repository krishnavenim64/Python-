Class Solution(object):

    Def longestValidParentheses(self, s):

        “””

        :type s: str

        :rtype: int

        “””

        # use 1D DP

        # dp[i] records the longestValidParenthese EXACTLY ENDING at s[i]

        Dp = [0 for x in xrange(len(s))]

        Max_to_now = 0

        For i in xrange(1,len(s)):

            If s[i] == ‘)’:

                # case 1: ()()

                If s[i-1] == ‘(‘:

                    # add nearest parentheses pairs + 2

                    Dp[i] = dp[i-2] + 2

                # case 2: (()) 

                # i-dp[i-1]-1 is the index of last “(“ not paired until this “)”

                Elif i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == ‘(‘:

                    If dp[i-1] > 0: # content within current matching pair is valid 

                    # add nearest parentheses pairs + 2 + parentheses before last “(“

                        Dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]

                    Else:

                    # otherwise is 0

                        Dp[i] = 0

                Max_to_now = max(max_to_now, dp[i])

        Return max_to_now

