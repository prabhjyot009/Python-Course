#marks of 10 students using less than and greater than operator using operator overloading and also display the name of the student with highest marks using user defined exception
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 
    def __gt__(self, other):
        return self.marks > other.marks
    def __lt__(self, other):
        return self.marks < other.marks
    
students=[]    
for i in range(10):
        name=input("Enter Student Name:")
        crypto=int(input("Enter Marks for Cryptography:"))
        python=int(input("Enter Marks for Python:"))
        android=int(input("Enter Marks for Android:"))
        marks=(crypto+python+android)//3
        student=Student(name,marks)
        students.append(student)
        
highest_marks=max(students, key=lambda student: student.marks)
print("Highest marks are:",highest_marks.marks)
print("Student with highest marks is:",highest_marks.name)
        