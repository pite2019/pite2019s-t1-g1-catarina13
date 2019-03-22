class Matrix:
    def __init__(self, matrix):
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.matrix = matrix

    def sum_matrix(self, m1, m2):
        if m1.n != m2.n or m1.m != m2.m:
            return None
        else:
            sumM = [[0 for i in range(m1.n)] for j in range(m1.m)]
            for i in range(m1.n):
                for j in range(m1.m):
                    sumM[i][j] = m1[i][j] + m2[i][j]

            return sumM

    ##def product_matrix(self, m1, m2):
      ##  if m1.m != m2.n:
          ##  return None
        ##else:
           ## product = [[0 for i in range(m1.m)] for j in range(m1.n)]
            ##for i in range(m1.n):
              ##  s = 0
                ##for j in range(m1.m):
                  ##  for k in range(m2.m):
                    ##    s += m1[i][j] * m2[k][i]

                ##product[i][j]


matrix1 = Matrix([[1,2],[1,2]])
matrix2 = Matrix([[1,2],[1,2]])
print(sum_matrix(matrix1,matrix2))
