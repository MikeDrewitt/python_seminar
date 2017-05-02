class Roster:
    def __init__(self, courseName, courseNumber, instructor):
        self.courseName = courseName
        self.courseNumber = courseNumber
        self.instructor = instructor
        self.student_list = []

    def add_student_to_class(self, student_name):
        self.student_list.append(student_name)

    def size_of_class(self):
        return len(self.student_list)
