Class Solution:

    Def numJewelsInStones(self, jewels: str, stones: str) -> int:

        Counter = 0

        Jewels = set(jewels) 

        For stone in stones:

            If stone in jewels:

                Counter += 1

        Return counter

