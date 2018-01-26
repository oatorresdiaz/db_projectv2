from config.dbconfig import pg_config
import psycopg2

class PriceHistoryDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllPriceHistory(self):
        cursor = self.conn.cursor()
        query = "select * from pricehistory;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPriceHistoryById(self, phID):
        cursor = self.conn.cursor()
        query = "select * from pricehistory where phID = %s;"
        cursor.execute(query, (phID,))
        result = cursor.fetchone()
        return

    def getPriceHistoryByInventoryId(self, invID):
        cursor = self.conn.cursor()
        query = "select * from pricehistory where invID = %s;"
        cursor.execute(query, (invID,))
        result = cursor.fetchone()
        return

    def insert(self, invID, priceAtMoment):
        cursor = self.conn.cursor()
        query = "insert into pricehistory(invID, startDate, thruDate, priceAtMoment) values (%s, current_timestamp, NULL, %s)"
        cursor.execute(query, (invID, priceAtMoment,))
        self.conn.commit()

    def findPriceHistoryId(self, invID):
        cursor = self.conn.cursor()
        query = "select phID from pricehistory where thruDate = NULL and invID = %s"
        cursor.execute(query, (invID,))
        phID = cursor.fetchone()[0]
        self.conn.commit()
        return phID


    def updateThruDate(self, phID):
        cursor = self.conn.cursor()
        query = "update pricehistory set ordexpdate = current_timestamp where phID = %s;"
        cursor.execute(query, (phID,))
        self.conn.commit()
