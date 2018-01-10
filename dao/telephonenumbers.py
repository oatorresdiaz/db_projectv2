from config.dbconfig import pg_config
import psycopg2

class TelephoneNumbersDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllTelephoneNumbers(self):
        cursor = self.conn.cursor()
        query = "select * from telephonenumbers;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTelephoneNumberById(self, tID):
        cursor = self.conn.cursor()
        query = "select * from telephonenumbers where tID = %s;"
        cursor.execute(query, (tID,))
        result = cursor.fetchone()
        return result

    def getTelephoneNumberByUserId(self, uID):
        cursor = self.conn.cursor()
        query = "select * from telephonenumbers where uID = %s;"
        cursor.execute(query, (uID,))
        result = cursor.fetchone()
        return result