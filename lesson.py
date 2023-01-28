class Lesson:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def printLesson(self):
        print("{name}, {count},".format(name = self.name, count = self.count))