import student


class Group(list):

    def __init__(self, students):
        super().__init__(item for item in students)
    
    
    def __setitem__(self, index, item):
        super().__setitem__(index, student.Student(item))

    


    # def add(self, student) :
    #     self.students.append(student)
