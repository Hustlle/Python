import lesson

class Semestr(list):
    def __init__(self, lessones):
        super().__init__(item for item in lessones)

# st.printStudents()
# print(student.printStudents())