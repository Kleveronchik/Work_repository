from generator import Generator

students = [["Nikita", 15, True], 2, 3, 4, 5, "Andrii"]
iter_students = iter(students)

iter_students1 = iter(students)
for student in iter_students:
    print(student)
for student in iter_students1:
    print(student)
try:
    print(iter_students.__next__())
    print(iter_students.__next__())
    print(iter_students.__next__())
    print(iter_students.__next__())
    print(iter_students.__next__())
    print(iter_students.__next__())
    print(iter_students.__next__())
    #while(True):
        #print(next(iter_students))
        ##print(iter_students.__next__())
except StopIteration:
    pass
print("Hello Iterators")

students = [["Nikita", 15, True], "Andrii", "Dima", "Roma", "Igor"]
generator = Generator(students)
for i in generator.GetStyudents():
    print(i)