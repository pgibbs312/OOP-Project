import sqlite3
from models.scores import Score, ScoreManager


class DatabaseManager:
    def __init__(self, filename):
        # Connect to the database
        self._db = sqlite3.connect(filename)

        # Create a curosr, cursor is what does stuff
        self._cursor = self._db.cursor()

        # 
        self._cursor.execute('SELECT name from sqlite_master where type = "table"')
        res = self._cursor.fetchone()

        # create a table if one does not already exist
        if not res or "scores" not in res:
            # always execute on your cursor 
            # can also use doc string method so that you can write on multiple lines
            self._cursor.execute("CREATE TABLE scores (name TEXT NOT NULL, score INTEGER NOT NULL)")
            # after any change you have to commit
            self._db.commit()

    def get_scores_by_name(self, name):
        """ get the scores that matches the name """
        self._cursor.execute("SELECT * FROM scores WHERE name LIKE?", (f"{name} %", ))
        return self._cursor.fetchall()
    
    def add_score(self, name, score):
        
        self._cursor.execute(f"INSERT INTO scores ('name', 'score') VALUES ('{name}', {score})")
        self._db.commit()
        print("Added score")
    
    def get_all(self):
        self._cursor.execute("SELECT * FROM scores ORDER BY score DESC")
        score_list = list()
        for data in self._cursor.fetchall():
            score_list.append(data)
        return score_list
        
    # closing database connection
    def close(self):
        self._db.close()
        

if __name__ == "__main__":
    # db = sqlite3.connect("scores.sqlite")
    # cursor = db.cursor()
    # cursor.execute("CREATE TABLE scores (name TEXT NOT NULL, score INTERGER NOT NULL)")

    # # insterting a name and score into the db
    # # cursor.execute("INSERT INTO scores ('name', 'score') VALUES ('Peter', 5000)")
    # # db.commit()

    # cursor.execute("SELECT * FROM scores")
    # for data in cursor.fetchall():
    #    print(data)
    
    score_db_manager = DatabaseManager("scores.sqlite")
    #score_db_manager.add_score('Tom', 3000)
    print(score_db_manager.get_all())



    