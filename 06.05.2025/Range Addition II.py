Class Solution(object):

    Def maxCount(self, m, n, ops):

        Min_y = m

        Min_x = n



        For y, x in ops:

            Min_y = min(min_y, y)

            Min_x = min(min_x, x)



        Return min_x * min_y

