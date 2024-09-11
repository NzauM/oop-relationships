from course import Course
class TM:
    def __init__(self,name, course):
        self.name = name
        self.course = course
        pass

    # add validation to ensure course is an instance of class Course, before a TM can be initialized
    @property
    def course(self):
        return self._course
    
    @course.setter
    def course(self, course):
        if isinstance(course, Course):
            self._course = course
        else:
            raise TypeError("Hii course mimi sija instantiate, umetoa wapi?")



    # @property
    # def course(self):
    #     return self._course
    
    # @course.setter
    # def course(self,course):
    #     if isinstance(course,Course):
    #         self._course = course
    #     else:
    #         raise TypeError("Course must be of Class Course")        
    # pass
