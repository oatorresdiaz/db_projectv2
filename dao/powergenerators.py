from config.dbconfig import pg_config
import psycopg2

class PowerGeneratorsDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllPowerGenerators(self):
        cursor = self.conn.cursor()
        query = "select * from powergenerators;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPowerGeneratorById(self, pgID):
        cursor = self.conn.cursor()
        query = "select * from powergenerators where pgID = %s;"
        cursor.execute(query, (pgID,))
        result = cursor.fetchone()
        return result