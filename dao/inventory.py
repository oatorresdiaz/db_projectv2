from config.dbconfig import pg_config
import psycopg2

class InventoryDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllInventory(self):
        cursor = self.conn.cursor()
        query = "select * from inventory natural inner join sells natural inner join resources natural inner join categories;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getInventoryById(self, invID):
        cursor = self.conn.cursor()
        query = "select * from inventory natural inner join sells natural inner join resources natural inner join categories where invID = %s;"
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

    def getSupplierByInventoryId(self, invID):
        cursor = self.conn.cursor()
        query = "select uID, ufirstname, ulastname, ugender, ubirthdate, addid, city, street, country, zipcode, cID, username, password, email, tid, homeNumber, mobileNumber, workNumber, otherNumber, suppID from users natural inner join addresses natural inner join credentials natural inner join telephonenumbers natural inner join suppliers natural inner join inventory where invID = %s;"
        cursor.execute(query, (invID,))
        result = cursor.fetchone()
        return result

    def getSuppliersByResourceName(self, resName):
        cursor = self.conn.cursor()
        query = "select uID, ufirstname, ulastname, ugender, ubirthdate, addid, city, street, country, zipcode, cID, username, password, email, tid, homeNumber, mobileNumber, workNumber, otherNumber, suppID from users natural inner join addresses natural inner join credentials natural inner join telephonenumbers natural inner join suppliers natural inner join inventory natural inner join sells natural inner join resources where resName = %s;"
        cursor.execute(query, (resName,))
        result = cursor.fetchone()
        return result

    def getInventoryByResourceNameAndCity(self, resname, city):
        cursor = self.conn.cursor()
        query = "select catID, resID, invID, suppID, invDate, invQty, invreserved, invAvailable, invprice, resname, resSpecifications, catname from addresses natural inner join suppliers natural inner join inventory natural inner join sells natural inner join resources natural inner join categories where resName = %s and city = %s;"
        cursor.execute(query, (resname, city))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getInventoryByResourceName(self, resname):
        cursor = self.conn.cursor()
        query = "select catID, resID, invID, suppID, invDate, invQty, invreserved, invAvailable, invprice, resname, resSpecifications, catname from addresses natural inner join suppliers natural inner join inventory natural inner join sells natural inner join resources natural inner join categories where resName = %s;"
        cursor.execute(query, (resname, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getInventoryByCity(self, city):
        cursor = self.conn.cursor()
        query = "select catID, resID, invID, suppID, invDate, invQty, invreserved, invAvailable, invprice, resname, resSpecifications, catname from addresses natural inner join suppliers natural inner join inventory natural inner join sells natural inner join resources natural inner join categories where city = %s;"
        cursor.execute(query, (city, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchInventoryByArguments(self, args):
        cursor = self.conn.cursor()
        arguments = ""
        values = list(args.values())
        for arg in args:
            arguments = arguments + arg + "= %s" + " and "
        arguments = arguments[:-5]  # Remove the last ' and '
        query = "select * from inventory natural inner join sells natural inner join resources natural inner join categories where " + arguments
        cursor.execute(query, values)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchInventoryWithSorting(self, orderby):
        cursor = self.conn.cursor()
        query = "select * from inventory natural inner join sells natural inner join resources natural inner join categories order by " + orderby
        cursor.execute(query)
        print(cursor.query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchInventoryByArgumentsWithSorting(self, args):
        cursor = self.conn.cursor()
        arguments = ""
        values = list(args.values())
        values.remove(args.get('orderby'))
        for arg in args:
            if arg != 'orderby':
                arguments = arguments + arg + "= %s" + " and "
        arguments = arguments[:-5]  # Remove the last ' and '
        query = "select * from inventory natural inner join sells natural inner join resources natural inner join categories where " + arguments + " order by " + args.get('orderby')
        cursor.execute(query, values)
        print(cursor.query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMaxPriceInInventory(self):
        cursor = self.conn.cursor()
        query = "select * from inventory natural inner join sells natural inner join resources natural inner join categories where invPrice = (select max(invPrice) from inventory);"
        cursor.execute(query)
        result = cursor.fetchone()
        return result

    def getMinPriceInInventory(self):
        cursor = self.conn.cursor()
        query = "select * from inventory natural inner join sells natural inner join resources natural inner join categories where invPrice = (select min(invPrice) from inventory where invPrice > 0);"
        cursor.execute(query)
        result = cursor.fetchone()
        return result

    def getFreeInInventory(self):
        cursor = self.conn.cursor()
        query = "select * from inventory natural inner join sells natural inner join resources natural inner join categories where invPrice = (select min(invPrice) from inventory);"
        cursor.execute(query)
        result = cursor.fetchone()
        return result

    def getPriceById(self, invID):
        cursor = self.conn.cursor()
        query = "select invprice from inventory where invid = %s;"
        cursor.execute(query, (invID,))
        result = cursor.fetchone()
        return result

    def getAvailableById(self, invID):
        cursor = self.conn.cursor()
        query = "select invavailable from inventory where invid = %s;"
        cursor.execute(query, (invID,))
        result = cursor.fetchone()
        return result

    def updateAvailablePurchase(self, invID, ordQty):
        cursor = self.conn.cursor()
        query = "update inventory set invavailable = (invavailable - %s), invqty = (invqty - %s) where invid = %s;"
        cursor.execute(query, (int(ordQty), int(ordQty), invID,))
        self.conn.commit()

    def updateAvailableReserve(self, invID, ordQty):
        print(ordQty)
        cursor = self.conn.cursor()
        query = "update inventory set invavailable = (invavailable - %s), invreserved = (invreserved + %s) where invid = %s;"
        cursor.execute(query, (int(ordQty), int(ordQty), invID,))
        print(cursor.query)
        self.conn.commit()


    def insert(self, suppID, invQty, invPrice):
        cursor = self.conn.cursor()
        query = "insert into inventory(suppID, invDate, invQty, invReserved, invAvailable, invPrice) values (%s, CURRENT_TIMESTAMP, %s, 0, %s, %s) returning invID;"
        cursor.execute(query, (suppID, invQty, invQty, invPrice,))
        invID = cursor.fetchone()[0]
        self.conn.commit()
        return invID

    def updatePrice(self, invPrice, invID):
        cursor = self.conn.cursor()
        query = "update inventory set invPrice = %s where invID = %s;"
        cursor.execute(query, (invPrice, invID,))
        self.conn.commit()

    def updateQtyAvailable(self, invID, invDiff, currInvQty, currInvAva):
        cursor = self.conn.cursor()
        print(invDiff)
        query = "update inventory set invqty = (%s + %s), invavailable = (%s + %s) where invid = %s"
        cursor.execute(query, (int(currInvQty), int(invDiff), int(currInvAva), int(invDiff), invID))
        self.conn.commit()

    def getInvDateByInvId(self, invID):
        cursor = self.conn.cursor()
        query = "select invDate from inventory where invID = %s;"
        cursor.execute(query, (invID,))
        invDate = cursor.fetchone()[0]
        self.conn.commit()
        return invDate

    def getQtyById(self, invID):
        cursor = self.conn.cursor()
        query = "select invqty from inventory where invid = %s"
        cursor.execute(query, (invID,))
        invQty = cursor.fetchone()
        return invQty
