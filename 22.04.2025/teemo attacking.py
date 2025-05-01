Class Solution(object):

    Def findPoisonedDuration(self, timeSeries, duration):

        Res = 0

        N = len(timeSeries)



        For i in range(n – 1):

            D = timeSeries[i + 1] – timeSeries[i]

            Res += duration if d > duration else d



        Return res + (duration if n else 0)

