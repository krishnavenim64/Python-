Class Solution(object):

    Def insert(self, intervals, newInterval):

        “””

        :type intervals: List[List[int]]

        :type newInterval: List[int]

        :rtype: List[List[int]]

        “””

        Result = []

        I = 0

        N = len(intervals)



        # Add intervals before the newInterval

        While i < n and intervals[i][1] < newInterval[0]:

            Result.append(intervals[i])

            I += 1



        # Merge overlapping intervals

        While i < n and intervals[i][0] <= newInterval[1]:

            newInterval[0] = min(newInterval[0], intervals[i][0])

            newInterval[1] = max(newInterval[1], intervals[i][1])

            i += 1



        result.append(newInterval)



        # Add remaining intervals

        While i < n:

            Result.append(intervals[i])

            I += 1



        Return result

