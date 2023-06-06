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