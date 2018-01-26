from config.dbconfig import pg_config
import psycopg2

class SuppliersDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join addresses natural inner join telephonenumbers natural inner join suppliers;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierById(self, suppID):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join addresses natural inner join telephonenumbers natural inner join suppliers where suppID = %s;"
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

    def getSupplierByInventoryId(self, invID):
        cursor = self.conn.cursor()
        query = "select suppID from suppliers natural inner join inventory where invID = %s;"
        cursor.execute(query, (invID,))
        suppID = cursor.fetchone()[0]
        return suppID

    def insert(self, uID):
        cursor = self.conn.cursor()
        query = "insert into suppliers(uID) values(%s) returning suppID;"
        cursor.execute(query, (uID,))
        suppID = cursor.fetchone()[0]
        self.conn.commit()
        return suppID

    def getOrdersBySupplierId(self, suppID):
        cursor = self.conn.cursor()
        query = "select ordQty, ordDate, ordExpDate, ordType, ordPrice, suppID, resName, resSpecifications from orders natural inner join inventory natural inner join sells natural inner join resources natural inner join categories where suppID = %s;"
        cursor.execute(query, (suppID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersByArguments(self, args):
        cursor = self.conn.cursor()
        arguments = ""
        values = list(args.values())
        for arg in args:
            arguments = arguments + arg + "= %s" + " and "
        arguments = arguments[:-5]  # Remove the last ' and '
        query = "select * from users natural inner join addresses natural inner join telephonenumbers natural inner join suppliers where " + arguments
        cursor.execute(query, values)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersWithSorting(self, orderby):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join addresses natural inner join telephonenumbers natural inner join suppliers order by " + orderby
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchSuppliersByArgumentsWithSorting(self, args):
        cursor = self.conn.cursor()
        arguments = ""
        values = list(args.values())
        values.remove(args.get('orderby'))
        for arg in args:
            if arg != 'orderby':
                arguments = arguments + arg + "= %s" + " and "
        arguments = arguments[:-5]  # Remove the last ' and '
        query = "select * from users natural inner join addresses natural inner join telephonenumbers natural inner join suppliers where " + arguments + " order by " + args.get('orderby')
        cursor.execute(query, values)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, uID):
        cursor = self.conn.cursor()
        query = "insert into suppliers(uID) values (%s) returning suppID;"
        cursor.execute(query, (uID,))
        suppID = cursor.fetchone()[0]
        self.conn.commit()
        return suppID