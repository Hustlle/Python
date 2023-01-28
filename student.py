class Student :
    def __init__(self, firstName, secondName, thirdName, course):
        self.firstName = firstName
        self.secondName = secondName
        self.thirdName = thirdName
        self.course = course
    
    def printStudents(self):
        print("{firstName}, {secondName}, {thirdName}, {course}".format(firstName = self.firstName, secondName = self.secondName, thirdName = self.thirdName, course = self.course))

    # def returnSt(self):
    #     return self