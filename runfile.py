# create a student
# create a course
# create a TM with a course
# 
# assign a course to a student => A student belongs to a course/One Course has many Students
# assign a course to a TM => One Tm teaches one course, but one course can be taught by several TMs => One Course to Many TMs
# get all students in a specific course => 
# from file import Object
# import ipdb
# manager => A manager can manage many courses and a course can be managed by many managers

# one manager = many courses
# one course = many managers

from student import Student
from course import Course
from tm import TM
from manager import Manager
from managercourse import ManagerCourse

student1 = Student("Ryne")
course1 = Course("Software Development","6 Months")
course2 = Course("Data Science","6 Months")
tm1 = TM("Mercy Nzau",course1)
manager1 = Manager("Mr Manager")
manager2 = Manager("Kiongoss")
manager1.assignCourse(course1)
manager1.assignCourse(course2)
print(ManagerCourse.find_manager_courses(manager1))
print(ManagerCourse.find_manager_courses(manager2), "MAnager 2 courses")

# def runApp():
#     # getting name and password
#     # if name is password is correct
#     # we give them options for what they wat to do, i.e interact with our methods
#     name = input("What's your name")
#     password = input("What's your password")
#     if name == "Mercy" and password == "1234":
#         print("What Do you Want to Do")
#         print("1: Add a student")
#         print("2: Add a manager")
#         print("3. View all course")
#         choice = input("What do you want?")
#         if choice == "1":
#             Student.assignCourse()
#         if choice == "2":
#             Manager.assignCourse()


# runApp()

# managedCourses = ManagerCourse.allmanagedcourses
# print(managedCourses)
# manager1courses = []

# for course in managedCourses:
#     if course.manager == manager1:
#         manager1courses.append(course.course.name)

# print(manager1courses)

# print(manager2.courses, "Line 29")
# print(manager1.courses)

# courseList = manager1.courses
# for course in courseList:
#     print(f"{manager1.name} manages the course {course.name}")
# student1.assignCourse(course1)



# print(student1.course) 
# print(tm1.course.duration)
# print(course1)
# print(tm1)

# ipdb.set_trace()


