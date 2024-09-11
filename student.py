class Student:
    def __init__(self,name):
        self.name = name
        pass

    def assignCourse(self,course):
        # validatio to ensure course is an instance of class Course
        self.course = course 
        print(f"{self.name} has been assigned to course {self.course.name}")
        # return f"{self.name} has been assigned to course {self.course.name}"
pass