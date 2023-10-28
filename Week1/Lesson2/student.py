class Student:
    def __init__(self, name: str, age: float, group: str, gradeavg: float):
        self.Name = name
        self.Age = age
        self.Group = group
        self.GradeAvg = gradeavg
    def __bool__(self):
        return self.Name !=  None and\
                self.Age != None and\
                self.Group != None and\
                self.GradeAvg != None
    def __len__(self):
        return len(self.Name)
    def __str__(self):
        return (f"Name - {self.Name}\n"
                f"Age - {self.Age}\n"
                f"Group - {self.Group}\n"
                f"Average Grade - {self.GradeAvg}")
