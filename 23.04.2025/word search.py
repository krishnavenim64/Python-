Class Solution(object):

    Def exist(self, board, word):

    

        M = len(board)

        N = len(board[0])

        Directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        Def traverse(current, i):

            If i == len(word):

                Return True

            Temp = board[current[0]][current[1]]

            Board[current[0]][current[1]] = “”

            For d in directions:

                X = d[0]+ current[0]

                Y = d[1]+ current[1]

                If 0<= x<m and 0<=y<n and board[x][y]==word[i]:

                       If traverse((x, y), i+1):

                         Return True

            Board[current[0]][current[1]] = temp

            Return False

        For i in range(m):

            For j in range(n):

                If board[i][j]==word[0] and traverse((i, j), 1):

                    Return True

        Return False

