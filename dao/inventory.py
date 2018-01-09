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