Class Solution(object):

    Def checkPerfectNumber(self, num):

        If num < 2: return False

        S = 1

        I = 2

        While i * i <= num:

            If num % i == 0:

                S += i

                If i * i != num:

                    S += num // i

            I += 1

        Return s == num

