Class Solution(object):

    Def setZeroes(self, matrix):

        L = 0

        K = 0

        A = [[]]  

        

        For i in range(len(matrix)):

            For j in range(len(matrix[i])):

                If matrix[i][j] == 0:

                    a.append([i, j])  

        

        for i in range(len(a)):

            if len(a[i]) < 2:  

                continue

            gt1 = a[i][0]

            gt2 = a[i][1]  

            

            for k in range(len(matrix[0])):

                matrix[gt1][k] = 0  

            

            for l in range(len(matrix)):  

                matrix[l][gt2] = 0  

        

        return matrix  

