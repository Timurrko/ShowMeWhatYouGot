# Создай объект класса Даниэля, считай с его помощью информацию из файла hobbies.json,
# получи из этого объекта словарь с информацией и хобби и сохрани у себя в аттрибуте
#
# Создай метод, который заносит эти данные в бд sqlite3 в файл hobbies
# и метод, который их оттуда считывает
import sqlite3
import os



class Ramil:

    def __init__(self, danya, db_name):
        self.danya = danya
        self.db_name = db_name
        self.data = dict()
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.file_data = None

    def dan_f(self):
        self.data = self.danya.read_file()

    def save(self):

        #self.cursor.execute("DROP TABLE IF EXISTS Users")
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
            name TEXT PRIMARY KEY,
            hobbies TEXT
            )
            ''')
       # self.cursor.execute("DELETE FROM Users")

        for key, value in self.data.items():  # [('Harry1', 'running video_games')('Alex1', 'anime pottery')]
            result = ' '.join(value)
            self.cursor.execute("REPLACE INTO Users (name, hobbies) VALUES (?, ?);", (key, result))

        self.connection.commit()

    def read(self):

        self.cursor.execute("SELECT * FROM Users;")
        results = self.cursor.fetchall()
        data = dict()
        for name, hobbies in results:
            data[name] = hobbies.split()
        print(data)

        self.connection.commit()

    def close(self):
        self.connection.close()


def read_file_text():
    current_path = os.getcwd()
    curr_spl = current_path.split(os.sep)
    curr_spl = curr_spl[:-1]
    curr_spl += ['data', 'hobbies']
    current_path = os.sep.join(curr_spl)
    return current_path



if __name__ == '__main__':
   d = Ramil(Hobby(read_file_text()), "new_database.db")
   d.dan_f()
   d.save()
   d.read()
   d.close()

