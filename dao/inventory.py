from config.dbconfig import pg_config
import psycopg2

class InventoryDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllInventory(self):
        cursor = self.conn.cursor()
        query = "select * from inventory;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getInventoryById(self, invID):
        cursor = self.conn.cursor()
        query = "select * from inventory where invID = %s;"
        cursor.execute(query, (invID,))
        result = cursor.fetchone()
        return result