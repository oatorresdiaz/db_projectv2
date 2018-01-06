from config.dbconfig import pg_config
import psycopg2

class FuelDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllFuel(self):
        cursor = self.conn.cursor()
        query = "select * from fuel;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFuelById(self, fuelID):
        cursor = self.conn.cursor()
        query = "select * from fuel where fuelID = %s;"
        cursor.execute(query, (fuelID,))
        result = cursor.fetchone()
        return result