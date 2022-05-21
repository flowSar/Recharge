
import sqlite3

class UsersDataBase:

    def __init__(self):

        self.connect = sqlite3.connect("/home/exsar/PycharmProjects/python_oop_Gui/Recharge/Users.db")
        self.cursor = self.connect.cursor()
        try:
            self.cursor.execute("""CREATE TABLE users (
                                username text,
                                password text,
                                permission text
                                
                                )""")
            # i want this command to only eacuted once that's why i put it inside try exacpt with create database table
            self.cursor.execute("INSERT INTO users VALUES ('admin', '12345', 'high')")
        except sqlite3.OperationalError:
            pass


        self.connect.commit()


    def pump_all(self, name):
        self.cursor.execute(f"SELECT * FROM users WHERE username = '{name}'")
        return self.cursor.fetchall()


    def insertdata(self, username, password, permession):
        self.cursor.execute(f"INSERT INTO users VALUES ('{username}', '{password}', '{permession}')")
        self.connect.commit()





# database = UsersDataBase()
# print(database.pump_all("brahim"))
# database.insertdata("khalid", "nutter", 'low')
# print(database.pump_all("khalid"))