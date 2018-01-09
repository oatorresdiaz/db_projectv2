from config.dbconfig import pg_config
import psycopg2

class SuppliersDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join addresses natural inner join credentials natural inner join telephonenumbers natural inner join suppliers;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierById(self, suppID):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join addresses natural inner join credentials natural inner join telephonenumbers natural inner join suppliers where suppID = %s;"
        cursor.execute(query, (suppID,))
        result = cursor.fetchone()
        return result

    def getInventoryBySupplierId(self, suppID):
        cursor = self.conn.cursor()
        query = "select catID, resID, invID, suppID, invDate, invQty, invReserved, invAvailable, invPrice, resName, catName from suppliers natural inner join inventory natural inner join sells natural inner join resources natural inner join categories where suppID = %s;"
        cursor.execute(query, (suppID,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, uid):
        cursor = self.conn.cursor()
        query = "insert into suppliers(uID) values (%s) returning suppid;"
        cursor.execute(query, (uid,))
        suppid = cursor.fetchone()[0]
        self.conn.commit()
        return suppid