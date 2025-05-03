Def largestRectangleArea(self, height):

    Height.append(0)

    Stack = [-1]

    Ans = 0

    For i in xrange(len(height)):

        While height[i] < height[stack[-1]]:

            H = height[stack.pop()]

            W = i – stack[-1] – 1

            Ans = max(ans, h * w)

        Stack.append(i)

    Height.pop()

    Return ans







# 94 / 94 test cases passed.

# Status: Accepted

# Runtime: 76 ms

# 97.34%



