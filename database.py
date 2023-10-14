import sqlite3

class DataBase:
    def __init__(self, database):
        self.conn = sqlite3.connect(database, check_same_thread=False)
        self.cursor = self.conn.cursor()
    

    def sample_request(self, user_id):
        """sample_request comment"""
        with self.conn:
            pass


    def close(self):
        """Закрываем соединение с БД"""
        self.conn.close()





