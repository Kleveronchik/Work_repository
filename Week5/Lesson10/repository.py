import sqlite3
class Repository:
    def __init__(self, database:str, timeout:float):
        self.Database:str = database
        self.TimeOut:float = timeout
    def Query(self, sqlQuery:str):
        try:
            connection = sqlite3.connect(self.Database, self.TimeOut)
            cursor = connection.cursor()
            cursor.execute(sqlQuery)
            connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            connection.close()