'''
from counter import Counter
#1
students = [["Nikita", 15, True], 1, 2, 3, 4, 5, "Nikita"]
iter_students = iter(students)

#1.1
for student in iter_students:
    print(student)
for student in iter_students:
    print(student)

#1.2
try:
    #1.21
    print(iter_students.__next__())
    print(iter_students.__next__())
    print(iter_students.__next__())
    print(iter_students.__next__())
    print(iter_students.__next__())
    print(iter_students.__next__())
    
    #1.22
    while (iter_students.__next__()):
        print(iter_students.__iter__().__str__())
    
    1.23
    while (True):
        #print(next(iter_students))
        print(iter_students.__next__())
except StopIteration:
    pass
'''

'''
#2
counter = Counter(25, 40)
try:
    while(True):
        print(next(counter))
except StopIteration:
    pass
'''