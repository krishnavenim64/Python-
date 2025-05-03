Class Solution(object):

    Def spiralOrder(self, matrix):

        “””

        :type matrix: List[List[int]]

        :rtype: List[int]

        “””

        N, m = len(matrix), len(matrix[0])

        Checked = [[False for _ in range(m)] for _ in range(n)]

        Result = []

        R, c = 0, 0

        Go_dir = [0, 1] # go right

        While(True):

            V = matrix[r][c]

            Checked[r][c] = True

            Result.append(v)



            Right = r < n and (c+1) < m and not checked[r][c+1]

            Down = (r+1) < n and c < m and not checked[r+1][c]

            Left = r >= 0 and (c-1) >= 0 and not checked[r][c-1]

            Up = (r-1) >= 0 and c >= 0 and not checked[r-1][c]



            # go right

            If right:

                If not(up and go_dir == [-1, 0]):

                    Go_dir = [0, 1]

            # go down

            Elif down:

                Go_dir = [1, 0]

            # go left

            Elif left:

                Go_dir = [0, -1]

            # go up

            Elif up:

                Go_dir = [-1, 0]

            Else:

                Break



            R = go_dir[0] + r

            C = go_dir[1] + c

            

        Return result

