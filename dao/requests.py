from config.dbconfig import pg_config
import psycopg2

class RequestsDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = "select * from requests;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestById(self, reqID):
        cursor = self.conn.cursor()
        query = "select * from requests where reqID = %s;"
        cursor.execute(query, (reqID,))
        result = cursor.fetchone()
        return result