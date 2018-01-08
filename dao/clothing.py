from config.dbconfig import pg_config
import psycopg2

class ClothingsDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllClothings(self):
        cursor = self.conn.cursor()
        query = "select * from clothings;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClothingById(self, clothID):
        cursor = self.conn.cursor()
        query = "select * from clothings where clothID = %s;"
        cursor.execute(query, (clothID,))
        result = cursor.fetchone()
        return result

    def getClothingByResourceId(self, resID):
        cursor = self.conn.cursor()
        query = "select * from clothings where resID = %s;"
        cursor.execute(query, (resID,))
        result = cursor.fetchone()
        return result

    def getClothingByCategoryId(self, catID):
        cursor = self.conn.cursor()
        query = "select * from clothings where catID = %s;"
        cursor.execute(query, (catID,))
        result = cursor.fetchone()
        return result

    def getClothingByGender(self, clothGender):
        cursor = self.conn.cursor()
        query = "select * from clothings where clothGender = %s;"
        cursor.execute(query, (clothGender,))
        result = cursor.fetchone()
        return result

    def getClothingByBrand(self, clothBrand):
        cursor = self.conn.cursor()
        query = "select * from clothings where clothBrand = %s;"
        cursor.execute(query, (clothBrand,))
        result = cursor.fetchone()
        return result

    def getClothingBySize(self, clothSize):
        cursor = self.conn.cursor()
        query = "select * from clothings where clothSize = %s;"
        cursor.execute(query, (clothSize,))
        result = cursor.fetchone()
        return result

    def getClothingByColor(self, clothColor):
        cursor = self.conn.cursor()
        query = "select * from clothings where clothColor = %s;"
        cursor.execute(query, (clothColor,))
        result = cursor.fetchone()
        return result

    def getClothingByDesignPattern(self, clothDesignPattern):
        cursor = self.conn.cursor()
        query = "select * from clothings where clothDesignPattern = %s;"
        cursor.execute(query, (clothDesignPattern,))
        result = cursor.fetchone()
        return result