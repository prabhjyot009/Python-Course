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

#algorithm to add two matrix using overloaded + operator.
#step1: start
#step2: define a class Matrix
#step3: define a constructor with self and matrix as parameter
#step4: define a method __add__(self,other) with self and other as parameter
#step5: define a for loop with range(len(self.matrix)) as parameter
#step6: define a nested for loop with range(len(self.matrix[0])) as parameter
#step7: add self.matrix[i][j] and other.matrix[i][j] and store it in self.matrix[i][j]
#step8: return self.matrix
#step9: define a object m1 of class Matrix with parameter [[1,2,3],[4,5,6],[7,8,9]]
#step10: define a object m2 of class Matrix with parameter [[1,2,3],[4,5,6],[7,8,9]]
#step11: define a object m3 and assign m1+m2 to it
#step12: print m3
#step13: stop