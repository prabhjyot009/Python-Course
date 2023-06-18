class Student:
    def __init__(self,dw,py):
        self.dw=dw
        self.py=py
    def __add__(self,other):
        self.dw=self.dw+other.dw
        self.py=self.py+other.py
        return self
s1=Student(10,20)
s2=Student(30,40)
s3=s1+s2
print("DW",s3.dw)
print("PY",s3.py)

class A:
    def __init__(self,a):
        self.a=a
    def __gt__(self,other):
        if(self.a>other.a):
            return True
        else:
            return False
n1=A(2)
n2=A(3)
if(n1>n2):
    print("n1 is greater than n2")
else:
    print("n2 is greater than n1")