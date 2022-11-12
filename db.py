import sqlite3


class Databasse:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO test (user_id) VALUES (?)", (user_id,))

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM test WHERE user_id = ?", (user_id,)). fetchall()
            return bool(len(result))

    def set_user_name(self, user_id, user_name):
        with self.connection:
            return self.cursor.execute("UPDATE test SET user_name = ? WHERE user_id = ?", (user_name, user_id,))

    def get_signup(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT signup FROM test WHERE user_id = ?", (user_id,)).fetchall()
            for row in result:
                signup = str(row[0])
                return signup


    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE test SET signup = ? WHERE user_id = ?", (signup, user_id,))

    def set_user_male(self, user_id, user_male):
        with self.connection:
            return self.cursor.execute("UPDATE test SET user_male = ? WHERE user_id = ?", (user_male, user_id,))

    def get_signup1(self, user_id):
        with self.connection:
            result1 = self.cursor.execute("SELECT signup1 FROM test WHERE user_id = ?", (user_id,)).fetchall()
            for row in result1:
                signup1 = str(row[0])
            return signup1

    def set_signup1(self, user_id, signup1):
        with self.connection:
            return self.cursor.execute("UPDATE test SET signup1 = ? WHERE user_id = ?", (signup1, user_id,))
