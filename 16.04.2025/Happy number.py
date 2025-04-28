Class Solution:

    Def isHappy(self, n: int) -> bool:

        Def get_next(number):

            Return sum(int(digit) ** 2 for digit in str(number))

        

        Seen = set()

        While n != 1 and n not in seen:

            Seen.add(n)

            N = get_next(n)

        Return n == 1

