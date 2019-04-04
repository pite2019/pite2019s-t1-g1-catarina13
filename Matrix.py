import math
import traceback

class Matrix:
    def __init__(self, *args):
        try:
            if (math.sqrt(len(args))-int(math.sqrt(len(args)))):
                raise Exception("Wrong number of arguments!")
        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())

        self.n = int(math.sqrt(len(args)))
        self.matrix = [[ args[self.n*i+j] for j in range(self.n)] for i in range(self.n)]

    def __getitem__(self, index):
        return self.matrix[index]

    def create_matrix(self, values):
        return Matrix(*values)

    def __add__(self, m2):
        
        if type(m2) != Matrix:
            m2 = self.create_matrix([m2 for i in range(self.n*self.n)])
            
        try:
            if self.n != m2.n:
                raise Exception("Different matrix sizes")
        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())

        sumM = [ 0 for j in range(self.n*self.n)]
        count = 0
        
        for i in range(self.n):
            for j in range(self.n):
                sumM[count] = self.matrix[i][j] + m2[i][j]
                count += 1

        return self.create_matrix(sumM)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, m2):
        try:
            if self.n != m2.n:
                raise Exception("Different matrix sizes")
        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())
            
        sub = [ 0 for j in range(self.n*self.n)]
        count = 0
        gen = self.generator_function(self.matrix)
        gen2 = self.generator_function(m2)
        
        for i in range(self.n):
            for j in range(self.n):
                elem = next(gen)
                elem2 = next(gen2)
                sub[count] = elem - elem2
                count += 1

        return self.create_matrix(sub)

    def __matmul__(self, m2):
        try:
            if self.n != m2.n:
                raise Exception("Different matrix sizes")
        except Exception as e:
            print("type error: " + str(e))
            print(traceback.format_exc())

        gen = self.generator_function(self.matrix)
        gen2 = self.generator_function(m2)
        product = [0 for i in range(self.n*self.n)]
        count = 0
        
        for i in range(self.n):
            for k in range(self.n):
                elem = next(gen)
                elem2 = next(gen2)
                s = 0
                for j in range(self.n):
                    s += self.matrix[i][j] * m2[j][k]

                product[count] = s
                count += 1

        return self.create_matrix(product)       
                
    def print_matrix(self,matrix):

        gen = self.generator_function(matrix)
        col = 0
        spaces = [0 for j in range(matrix.n)]
        for i in range(matrix.n*matrix.n):
            if col % 3 == 0:
                col = 0
            item = next(gen)
            if len(str(item)) > spaces[col]:
                for j in range(matrix.n):
                    if i - j*matrix.n == col:
                        spaces[col] = len(str(item))

            col+=1

        gen = self.generator_function(matrix)
        
        for i in range(matrix.n):
            stri = ''
            for j in range(matrix.n):
                elem = next(gen)
                stri+= str(elem)
                if len(str(elem)) != spaces[j]:
                    stri+=' '
                stri+=' '

            print(stri)

        print('\n')
                
    def generator_function(self,m):
        for i in m:
            for j in i:
                yield j




