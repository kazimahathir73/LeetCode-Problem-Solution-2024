class Solution:
    def setZeroes(self, matrix):
        arr = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    arr.append((i,j))
        
        for rc in arr:
            matrix[rc[0]] = [0]*len(matrix[rc[0]])

            for k in range(len(matrix)):
                matrix[k][rc[1]] = 0
                
        return matrix

