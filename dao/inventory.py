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

    def getInventoryBySupplierId(self, suppID):
        cursor = self.conn.cursor()
        query = "select * from inventory where suppID = %s;"
        cursor.execute(query, (suppID,))
        result = cursor.fetchone()
        return result

    def getInventoryByDate(self, invDate):
        cursor = self.conn.cursor()
        query = "select * from inventory where invDate = %s;"
        cursor.execute(query, (invDate,))
        result = cursor.fetchone()
        return result

    def getInventoryByQuantity(self, invQty):
        cursor = self.conn.cursor()
        query = "select * from inventory where invQty = %s;"
        cursor.execute(query, (invQty,))
        result = cursor.fetchone()
        return result

    def getInventoryReserved(self, invReserved):
        cursor = self.conn.cursor()
        query = "select * from inventory where invReserved = %s;"
        cursor.execute(query, (invReserved,))
        result = cursor.fetchone()
        return result

    def getInventoryAvailable(self, invAvailable):
        cursor = self.conn.cursor()
        query = "select * from inventory where invAvailable = %s;"
        cursor.execute(query, (invAvailable,))
        result = cursor.fetchone()
        return result

    def getInventoryByPrice(self, invPrice):
        cursor = self.conn.cursor()
        query = "select * from inventory where invPrice = %s;"
        cursor.execute(query, (invPrice,))
        result = cursor.fetchone()
        return result
