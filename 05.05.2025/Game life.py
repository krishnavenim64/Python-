Class Solution(object):

    Def gameOfLife(self, board):

        “””

        :type board: List[List[int]]

        :rtype: None Do not return anything, modify board in-place instead.

        “””

        Rows=len(board)

        Cols=len(board[0])

        Neigh=[(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        Def changeing(row,col):

            Live=0

            For i,j in neigh:

                New_r=row+i

                New_c=col+j

                If (new_r>=0 and new_r<rows) and (new_c>=0 and new_c<cols) and abs(board[new_r][new_c])==1:

                    Live+=1

            Return live

        For i in range(rows):

            For j in range(cols):

                Lives=changeing(i,j)

                If board[i][j]==1:

                    If lives<2 or lives>3:

                        Board[i][j]=-1

                Else:

                    If lives==3:

                        Board[i][j]=2

        For i in range(rows):

            For j in range(cols):

                If board[i][j]>0:

                    Board[i][j]=1

                Else:

                    Board[i][j]=0

