#wap to add two matrix using overloaded + operator
class Matrix:
    def __init__(self,matrix):
        self.matrix=matrix
    def __add__(self,other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                self.matrix[i][j]=self.matrix[i][j]+other.matrix[i][j]
        return self.matrix
m1=Matrix([[1,2,3],[4,5,6],[7,8,9]])
m2=Matrix([[1,2,3],[4,5,6],[7,8,9]])
m3=m1+m2
print(m3)