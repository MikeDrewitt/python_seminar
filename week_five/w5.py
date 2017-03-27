from student import Student
from roster import Roster

cse115 = Roster("Intro to CS, I", "CSE115", "Jesse Hartloff")

mike = Student("Mike", 50086913, "Liberal Arts")
alex = Student("Alex", 66666666, "Computer Science")

cse115.add_student_to_class(mike)
cse115.add_student_to_class(alex)

print("Students in", cse115.size_of_class())

mike.addCourse("CSE115", 3.4)
mike.addCourse("CSE191", 2.5)
mike.addCourse("MTH151", 2.1)

mike.printCourses()
print("GPA is:", mike.calculateGPA())
        

