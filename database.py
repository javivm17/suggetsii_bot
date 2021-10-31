import pymysql

class Suggest_database:        
    def __init__(self):
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