"""square matrix solution."""


class solution:
    def countsq(self,matrix:List[List[int]])->int:
        m=len(matrix)
        n = len(matrix[0])

        count = [0]*n
        tl=0
        result=0

        for i in range(m):
            for j in range (n):
                if matrix[i][j] == 1:
                    top = 0 if i == 0 else count[j]
                    left = 0 if j == 0 else count[j-1]
                    count[j] = 1+min(min(top,left),tl)
                    result += count[j]
                    tl = 0 if j==n-1 else top
                else:
                    count[j]=0
        return result









