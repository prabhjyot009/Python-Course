# class dog:
#     def show(s):
#         a=10
#         b=10
#         s.age=a+b
#         print(s.age)
#     def show1(s1):
#         s1.age=30
#         print(s1.age)
# d=dog()
# d.show()
# d.show1()

# #define a class student and display whether the student is pass or fail based on the score of 5 subjects

# class student:
#     def input1(m):
#         m.maths=int(input("Enter Marks for Maths:"))
#         m.science=int(input("Enter Marks for Science:"))
#         m.sst=int(input("Enter Marks for sst:"))
#         m.hindi=int(input("Enter Marks for hindi:"))
#         m.python=int(input("Enter Marks for python:"))
#     def show(m):
#         m.total=m.maths+m.science+m.sst+m.hindi+m.python
#         print("Total marks are:",m.total)
#         m.per=m.total/5
#         if(m.per>33):
#             print("Pass")
#         else:
#             print("Fail")
#         #grading system:
#     def avg(m1):
#         if(m1.per>=90):
#             print("Grade A")
#         elif(m1.per>=80):
#             print("Grade B")
#         elif(m1.per>=70):
#             print("Grade C")
#         elif(m1.per>=60):
#             print("Grade D")
#         elif(m1.per>=50):
#             print("Grade E")
#         else:
#             print("Grade F")
# s=student()
# s.input1()
# s.show()
# s.avg()
# import numpy as np
# class student:
#     ayush=[]
#     sam=[]
#     aakash=[]
#     size=int(input("Enter the size of array:"))
#     def input1(s):
#         for i in range(s.size):
#             print("Enter marks for ayush")
#             s.ayush.append(int(input("Enter the marks for maths:")))
#             s.ayush.append(int(input("Enter the marks for science:")))
#             s.ayush.append(int(input("Enter the marks for hindi:")))
#             print("Enter marks for sam")
#             s.sam.append(int(input("Enter the marks for maths:")))
#             s.sam.append(int(input("Enter the marks for science:")))
#             s.sam.append(int(input("Enter the marks for hindi:")))
#             print("Enter marks for aakash")
#             s.aakash.append(int(input("Enter the marks for maths:")))
#             s.aakash.append(int(input("Enter the marks for science:")))
#             s.aakash.append(int(input("Enter the marks for hindi:")))
            
#     def show(s):
#         print(s.ayush)
#         print(s.sam)
#         print(s.aakash)
#     def max(s):
#         #who got highest marks in maths
#         s.ayush1=np.array(s.ayush)
#         s.sam1=np.array(s.sam)
#         s.aakash1=np.array(s.aakash)
#         s.ayush2=s.ayush1[0:3]
#         s.sam2=s.sam1[0:3]
#         s.aakash2=s.aakash1[0:3]
#         s.ayush3=np.sum(s.ayush2)
#         s.sam3=np.sum(s.sam2)
#         s.aakash3=np.sum(s.aakash2)
#         if(s.ayush3>s.sam3 and s.ayush3>s.aakash3):
#             print("Ayush got highest marks in maths")
#         elif(s.sam3>s.ayush3 and s.sam3>s.aakash3):
#             print("Sam got highest marks in maths")
#         else:
#             print("Aakash got highest marks in maths")
#         #who got highest marks in science
#         s.ayush4=s.ayush1[3:6]
#         s.sam4=s.sam1[3:6]
#         s.aakash4=s.aakash1[3:6]
#         s.ayush5=np.sum(s.ayush4)
#         s.sam5=np.sum(s.sam4)
#         s.aakash5=np.sum(s.aakash4)
#         if(s.ayush5>s.sam5 and s.ayush5>s.aakash5):
#             print("Ayush got highest marks in science")
#         elif(s.sam5>s.ayush5 and s.sam5>s.aakash5):
#             print("Sam got highest marks in science")
#         else:
#             print("Aakash got highest marks in science")
#         #who got highest marks in hindi
#         s.ayush6=s.ayush1[6:9]
#         s.sam6=s.sam1[6:9]
#         s.aakash6=s.aakash1[6:9]
#         s.ayush7=np.sum(s.ayush6)
#         s.sam7=np.sum(s.sam6)
#         s.aakash7=np.sum(s.aakash6)
#         if(s.ayush7>s.sam7 and s.ayush7>s.aakash7):
#             print("Ayush got highest marks in hindi")
#         elif(s.sam7>s.ayush7 and s.sam7>s.aakash7):
#             print("Sam got highest marks in hindi")
#         else:
#             print("Aakash got highest marks in hindi")
        
# s1=student()
# s1.input1()
# s1.show()
# s1.max()


# class student:
#     def set_data(self):
#         self.name=input('Enter name:')
#         self.roll=int(input("Enter roll no."))
#         self.per=float(input("Enter percentage:"))
#     def show(self):
#         print("Name:",self.name)
#         print("Roll no.:",self.roll)
#         print("Percentage:",self.per)
# obj=student()
# obj.set_data()
# obj.show()

#init constructor:
class student:
    def __init__(self,x,y,z):
        self.name=x
        self.roll=y
        self.per=z
    def show(self):
        print("Name:",self.name)
        print("Roll no.:",self.roll)
        print("Percentage:",self.per)
obj=student("karan",6,7.8)
obj.show()
