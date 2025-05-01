Class Solution(object):

    Def spiralOrder(self, matrix):

        “””

        :type matrix: List[List[int]]

        :rtype: List[int]

        “””

        ROWS, COLS = len(matrix), len(matrix[0])

        

        Next_dir = {

            (0, 1): (1, 0),

            (1, 0): (0, -1),

            (0, -1): (-1, 0),

            (-1, 0): (0, 1)

        }



        Direction = (0, 1)

        Visited = set()

        R, c = 0, 0



        Res = []



        For _ in range(ROWS * COLS):  # Visit every cell exactly once

            Res.append(matrix[r][c])

            Visited.add((r, c))



            Nxt_r, nxt_c = r + direction[0], c + direction[1]

            If (nxt_r < 0 or nxt_r >= ROWS or

                Nxt_c < 0 or nxt_c >= COLS or

                (nxt_r, nxt_c) in visited):

                # Change direction if necessary

                Direction = next_dir[direction]

                Nxt_r, nxt_c = r + direction[0], c + direction[1]



            R, c = nxt_r, nxt_c



        Return res

