import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS apps(app_name text, app_path text)")
        self.conn.commit()

    def add_app(self, name, path):
        self.cur.execute("""INSERT INTO apps VALUES(?, ?)""",(name, path))
        self.conn.commit()

    def remove_app(self, name):
        self.cur.execute("DELETE FROM apps WHERE app_name=?",(name,))
        self.conn.commit()

    def pass_apps(self):
        self.cur.execute("SELECT * FROM apps")
        apps = self.cur.fetchall()
        return apps

    def pass_selected_app(self, name):
        self.cur.execute("SELECT * FROM apps WHERE app_name=?",(name,))
        app = self.cur.fetchall()
        return app

    def __del__(self):
        self.conn.close()
        