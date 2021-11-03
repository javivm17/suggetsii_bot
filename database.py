import pymysql
import os

class Suggest_database:        
    def __init__(self):
        '''self.db = pymysql.connect(
                host=os.environ.get("HOST"),
                user=os.environ.get("USER"),
                password=os.environ.get("PASSWORD"),
                db= os.environ.get("DB")
            )'''
        self.db = pymysql.connect(
                host="sql11.freesqldatabase.com",
                user="sql11447724",
                password="JlaIeR9bT7",
                db="sql11447724"
            )
        self.cursor = self.db.cursor()

    def insert_suggest(self,date,suggest):
        sql = "INSERT INTO sugerencia(fecha,sugerencia) values ('"+str(date)+"','"+str(suggest)+"')"
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            # Commit your changes in the database
            self.db.commit()
        except:
            # Rollback in case there is any error
            self.db.rollback()
        self.db.close()

    def get_suggests(self):
        sql = "SELECT * FROM sugerencia order by id desc"
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except:
            # Rollback in case there is any error
            self.db.rollback()
        self.db.close()
    
    def delete_suggest(self,id):
        sql = "DELETE FROM sugerencia where id = %s" % id
        try:
            # Execute the SQL command
            self.cursor.execute(sql)
            self.db.commit()
        except:
            # Rollback in case there is any error
            self.db.rollback()
        self.db.close()  