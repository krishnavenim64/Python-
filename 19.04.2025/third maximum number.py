Class Solution(object):

    Def thirdMax(self, nums):

        First = second = third = None

        For num in nums:

            If num == first or num == second or num == third:

                Continue

            If first is None or num > first:

                Third = second

                Second = first

                First = num

            Elif second is None or num > second:

                Third = second

                Second = num

            Elif third is None or num > third:

                Third = num

        Return third if third is not None else first

