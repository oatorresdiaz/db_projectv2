from config.dbconfig import pg_config
import psycopg2

class IceDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
         self.conn = psycopg2._connect(connection_url)

    def getAllIce(self):
        cursor = self.conn.cursor()
        query = "select * from ice;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getIceById(self, iceID):
        cursor = self.conn.cursor()
        query = "select * from ice where iceID = %s;"
        cursor.execute(query, (iceID,))
        result = cursor.fetchone()
        return result