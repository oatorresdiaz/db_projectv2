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

    def getAddressByUserId(self, uID):
        cursor = self.conn.cursor()
        query = "select * from addresses where uID = %s;"
        cursor.execute(query, (uID,))
        result = cursor.fetchone()
        return result

    def getAddressByCity(self, City):
        cursor = self.conn.cursor()
        query = "select * from addresses where City = %s;"
        cursor.execute(query, (City,))
        result = cursor.fetchone()
        return result

    def getAddressByStreet(self, Street):
        cursor = self.conn.cursor()
        query = "select * from addresses where Street = %s;"
        cursor.execute(query, (Street,))
        result = cursor.fetchone()
        return result

    def getAddressByCountry(self, Country):
        cursor = self.conn.cursor()
        query = "select * from addresses where Country = %s;"
        cursor.execute(query, (Country,))
        result = cursor.fetchone()
        return result

    def getAddressByZipCode(self, ZipCode):
        cursor = self.conn.cursor()
        query = "select * from addresses where ZipCode = %s;"
        cursor.execute(query, (ZipCode,))
        result = cursor.fetchone()
        return result
