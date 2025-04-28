Class Solution:

    Def generate(self, numRows: int) -> List[List[int]]:

        Output = [[1]]



        For r in range(2,numRows+1):

            

 = [1]

            For c in range(1,r-1):

                Tmp.append(output[-1][c]+output[-1][c-1])

            Tmp.append(1)

            Output.append(tmp)

        Return output



