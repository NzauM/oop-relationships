from course import Course
from managercourse import ManagerCourse
class Manager:
    def __init__(self,name):
        self.name = name
        pass

    def assignCourse(self,course):
        # initialize a new instance of our intermediary class
        if isinstance(course,Course):
            ManagerCourse(self,course)
        else:
            raise TypeError("Not of class Course")

# class Manager:
#     # managerCourses = [] #class attribute -> stores data that is common across all instances of the class
#     def __init__(self, name):
#         self.name = name
#         self.courses = [] #instance attribute -> stores data that is unique to the specific instance
#         pass

#     def assignCourse(self, course):
#         if isinstance(course, Course):
#             self.courses.append(course)
#         else:
#             raise TypeError("course is not a valid instance of class Course")
#     pass
