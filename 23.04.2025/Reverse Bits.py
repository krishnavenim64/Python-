Class Solution:

    Def reverseBits(self, n):

        Result = 0

        For i in range(32):

            Result = (result << 1) | (n & 1)

            N >>= 1

        Return result

