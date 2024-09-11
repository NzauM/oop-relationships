
class ManagerCourse:
    allmanagedcourses = []
    def __init__(self,manager,course):
        self.manager = manager
        self.course = course
        ManagerCourse.allmanagedcourses.append(self)
        pass

    # receives a manager and returns all courses managed by that manager
    @classmethod
    def find_manager_courses(cls, manager_instance):
        """
        class method that receives a manager instance and returns all courses this manager manages.
        """
        all_assigned_courses = cls.allmanagedcourses
        target_manager_courses = []
        # find all assigned courses
        # loop through all assigned courses and find those that have been assigned to the given manager_instance
        for course in all_assigned_courses:
            print(course) #ManagerCourse
            if course.manager == manager_instance:
                target_manager_courses.append(course)
        return target_manager_courses
        # append them to the final list and return them

    
    pass
