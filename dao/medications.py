from config.dbconfig import pg_config
import psycopg2

class MedicationsDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
         self.conn = psycopg2._connect(connection_url)

    def getAllMedications(self):
        cursor = self.conn.cursor()
        query = "select * from medications;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicationById(self, medID):
        cursor = self.conn.cursor()
        query = "select * from medications where medID = %s;"
        cursor.execute(query, (medID,))
        result = cursor.fetchone()
        return result