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

    def searchAddressesByArguments(self, args):
        cursor = self.conn.cursor()
        arguments = ""
        values = list(args.values())
        for arg in args:
            arguments = arguments + arg + "= %s" + " and "
        arguments = arguments[:-5] + ";"  # Remove the last ' and '
        query = "select * from users natural inner join addresses natural inner join telephonenumbers where " + arguments
        cursor.execute(query, values)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, uid, city, street, country, zipcode):
        cursor = self.conn.cursor()
        query = "insert into addresses(uid, city, street, country, zipcode) values (%s, %s, %s, %s, %s) returning addID;"
        cursor.execute(query, (uid, city, street, country, zipcode,))
        addID = cursor.fetchone()[0]
        self.conn.commit()
        return addID

    def update(self, addID, uID, city, street, country, zipcode):
        cursor = self.conn.cursor()
        query = "update addresses set city = %s, street = %s, country = %s, zipcode = %s where uID = %s and addID =%s;"
        cursor.execute(query, (city, street, country, zipcode, uID, addID, ))
        self.conn.commit()
        return addID
