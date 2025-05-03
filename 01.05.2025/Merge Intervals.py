Class Solution(object):

    Def merge(self, intervals):

        “””

        :type intervals: List[List[int]]

        :rtype: List[List[int]]

        “””

        # intervals are in order

        Intervals.sort(key=lambda x: x[0])

        # so b.start is always after a.start

        # so we compare a.start with b.end

        # if overlapping, get mex end

        # else merge previous interval and update a = b and so on

        Result = []

        A = intervals[0]



        For i in range(len(intervals)):

            B = intervals[i]

            If b[0] <= a[1]: # overlapping

                A[1] = max(a[1], b[1])

            Else:

                Result.append(a) # merge

                A = b



        Result.append(a)

        Return result

