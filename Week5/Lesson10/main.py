from repository import Repository
repo = Repository('students.sl3', 5.0)
'''
#1 CREATE TABLE .... (fields_definitions)
repo.Query('CREATE TABLE S2813 (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(20), age INT, avg_grade FLOAT)')
'''
#2 INSERT INTO .... (name_of_fields) VALUES(set_of_values)
repo.Query("INSERT INTO S2813(name, age, avg_grade) VALUES('Akinin Illya', 14, 12)")
repo.Query("INSERT INTO S2813(name, age, avg_grade) VALUES('Protsko Arsenii', 13, 11)")
repo.Query("INSERT INTO S2813(name, age, avg_grade) VALUES('Klevaichuk Nikita', 15, 10.5)")

#3 Update .... SET .... ()
#repo.Query('UPDATE S2813 SET avg_grade = 10.7 WHERE id = 2')
print("Done")