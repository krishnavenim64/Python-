Class Solution:

    Def plusOne(self, digits):

        N = len(digits)

        For i in range(n – 1, -1, -1):

            If digits[i] < 9:

                Digits[i] += 1

                Return digits

            Digits[i] = 0

        Return [1] + [0] * n

