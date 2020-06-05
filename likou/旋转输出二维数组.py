class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        outls = []
        a = len(matrix)
        b = len(matrix[0])
        for i in range(a):
            for j in range(b):
                outls.append(matrix[i][:-1])
                outls.append(0)
                outls.append(matrix[:-1][b - j - 1])
                outls.append(1)
                outls.append(matrix[a - i - 1][:])
                outls.append(2)
                outls.append(matrix[:][j])
        return outls
