Class Solution:

    Def getPermutation(self, n, k):

        # Create a list of numbers as strings for easier concatenation later

        Numbers = [str(i) for i in range(1, n + 1)]

        

        # Precompute factorials up to n

        Factorial = [1] * (n + 1)

        For i in range(1, n + 1):

            Factorial[i] = factorial[i – 1] * i



        # Convert k to 0-indexed

        K -= 1

        

        Result = []

        For i in range(n, 0, -1):

            # Determine the index of the current digit

            Index = k // factorial[i – 1]

            Result.append(numbers.pop(index))

            # Reduce k for the next iteration

            K %= factorial[i – 1]

            

        Return ‘’.join(result)



# Example usage:

If __name__ == ‘__main__’:

    Solution = Solution()

    Print(solution.getPermutation(3, 3))  # Expected output: “213”

    Print(solution.getPermutation(4, 9))  # Expected output: “2314”

    Print(solution.getPermutation(3, 1))  # Expected output: “123”







