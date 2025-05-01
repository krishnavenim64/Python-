Class Solution(object):

    Def nextGreaterElement(self, nums1, nums2):

        Stack = []

        D = {}

        For n in nums2:

            While stack and n > stack[-1]:

                D[stack.pop()] = n

            Stack.append(n)

        For n in stack:

            D[n] = -1

        Return [d[x] for x in nums1]

