import student
import group
import lesson
import semestr

st1 = student.Student("Nam1","lastName1","thirdName1","course1")
st2 = student.Student("Name2","lastName2","thirdName2","course1")
st3 = student.Student("Name3","lastName3","thirdName3","course1")
st4 = student.Student("Name4","lastName4","thirdName4","course1")

st5 = student.Student("Name5","lastName5","thirdName5","course2")
st6 = student.Student("Name6","lastName6","thirdName6","course2")
st7 = student.Student("Name7","lastName7","thirdName7","course2")
st8 = student.Student("Name8","lastName8","thirdName8","course2")

st9 = student.Student("Name9","lastName9","thirdName9","course3")
st10 = student.Student("Name10","lastName10","thirdName10","course3")
st11 = student.Student("Name11","lastName11","thirdName11","course3")
st12 = student.Student("Name12","lastName12","thirdName12","course3")

ls = lesson.Lesson("Lesson1", "20")
ls1 = lesson.Lesson("Lesson2", "34")
ls2 = lesson.Lesson("Lesson3", "48")
ls3 = lesson.Lesson("Lesson4", "34")
ls4 = lesson.Lesson("Lesson5", "48")
ls5 = lesson.Lesson("Lesson6", "34")
ls6 = lesson.Lesson("Lesson7", "20")
ls7 = lesson.Lesson("Lesson8", "34")

gp = group.Group([st1, st2, st3, st4])
gp1 = group.Group([st5, st6, st7, st8])
gp2 = group.Group([st9, st10, st11, st12])

smst1 = semestr.Semestr([ls, ls1, ls3, ls5, ls7])
smst2 = semestr.Semestr([ls3, ls2, ls7, ls6, ls4])
smst3 = semestr.Semestr([ls6, ls1, ls3, ls2, ls7,])

for item in gp:
    item.printStudents()

for item in gp1:
    item.printStudents()

for item in gp2:
    item.printStudents()


for item in smst1:
    item.printLesson()

for item in smst2:
    item.printLesson()

for item in smst3:
    item.printLesson()
