from config.dbconfig import pg_config
import psycopg2

class AddressesDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllAddresses(self):
        cursor = self.conn.cursor()
        query = "select * from addresses;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAddressById(self, addID):
        cursor = self.conn.cursor()
        query = "select * from addresses where addID = %s;"
        cursor.execute(query, (addID,))
        result = cursor.fetchone()
        return result