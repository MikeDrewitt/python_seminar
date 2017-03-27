class Student:
    def __init__(self, name, studentID, major):
        self.name = name
        self.studentID = studentID
        self.major = major
        self.courseMap = {}
    
    def printInfo(self):
        print(self.name, self.studentID, self.major, self.courseMap)
    
    def addCourse(self, courseName, grade):
        self.courseMap[courseName] = grade
    
    def printCourses(self):
        for course in self.courseMap:
            print(course, self.courseMap[course])
        
    def calculateGPA(self):
        total = 0
        for course in self.courseMap:
            total += self.courseMap[course]
        return total/len(self.courseMap) 


