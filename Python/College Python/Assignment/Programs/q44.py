#marks of 10 students using less than and greater than operator using operator overloading and also display the name of the student with highest marks using user defined exception
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 
    def __str__(self):
        return f"{self.name}: {self.marks}"

students = []

for i in range(10):
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    student = Student(name, marks)
    students.append(student)
highest_scorer = students[0]

for student in students[1:]:
    if student.marks > highest_scorer.marks:
        highest_scorer = student

print("\nHighest Scorer:",highest_scorer)


#algorithm to find the highest scorer among 10 students using less than and greater than operator using operator overloading and also display the name of the student with highest marks using user defined exception.
#step1: start
#step2: define a class Student
#step3: define a constructor with self, name and marks as parameter
#step4: define a method __str__(self) with self as parameter
#step5: return self.name and self.marks
#step6: define a empty list students
#step7: define a for loop with range(10) as parameter
#step8: define a variable name and assign input("Enter student name: ") to it
#step9: define a variable marks and assign float(input("Enter marks: ")) to it
#step10: define a object student of class Student with parameter name and marks
#step11: append student to students
#step12: define a variable highest_scorer and assign students[0] to it
#step13: define a for loop with students[1:] as parameter
#step14: if student.marks > highest_scorer.marks then assign student to highest_scorer
#step15: print "Highest Scorer:",highest_scorer
#step16: stop