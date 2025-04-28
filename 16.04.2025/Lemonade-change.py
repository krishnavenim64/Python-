Class Solution:

    Def lemonadeChange(self, bills: List[int]) -> bool:

        Count = {5: 0, 10: 0}

        For bill in bills:

            If bill == 5:

                Count[5] += 1

            Elif bill == 10:

                If count[5]:

                    Count[5] -= 1

                    Count[10] += 1

                Else: return False

            Else:

                If count[5] and count[10]:

                    Count[5] -= 1

                    Count[10] -= 1

                Elif count[5] >= 3:

                    Count[5] -= 3

                Else: return False

        Return True



