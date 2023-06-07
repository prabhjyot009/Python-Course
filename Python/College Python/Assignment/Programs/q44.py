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
