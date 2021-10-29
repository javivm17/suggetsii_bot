import pymysql

class Suggest_database:        
    def __init__(self):
        self.db = pymysql.connect(
                host="xxx",
                user="xxx",
                password="xxx",
                db="xxx"
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