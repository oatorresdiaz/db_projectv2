from config.dbconfig import pg_config
import psycopg2

class FoodsDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
         self.conn = psycopg2._connect(connection_url)

    def getAllFoods(self):
        cursor = self.conn.cursor()
        query = "select * from foods;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFoodById(self, fID):
        cursor = self.conn.cursor()
        query = "select * from foods where fID = %s;"
        cursor.execute(query, (fID,))
        result = cursor.fetchone()
        return result