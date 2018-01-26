from config.dbconfig import pg_config
import psycopg2

class CategoriesDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllCategories(self):
        cursor = self.conn.cursor()
        query = "select * from categories;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoriesById(self, catID):
        cursor = self.conn.cursor()
        query = "select * from categories where catID = %s;"
        cursor.execute(query, (catID,))
        result = cursor.fetchone()
        return result

    def getCategoryByInventoryId(self, invID):
        cursor = self.conn.cursor()
        query = "select catID from inventory natural inner join resources where invID = %s;"
        cursor.execute(query, (invID,))
        catID = cursor.fetchone()[0]
        print(catID)
        return catID

    def insert(self, catName):
        cursor = self.conn.cursor()
        query = "insert into categories(catName) values (%s) returning catID;"
        cursor.execute(query, (catName,))
        catID = cursor.fetchone()[0]
        self.conn.commit()
        return catID

    def update(self, catID, catName):
        cursor = self.conn.cursor()
        query = "update categories set catName = %s where catID = %s;"
        cursor.execute(query, (catName, catID,))
        self.conn.commit()
        return catID

    def getCatIdByResId(self, resID):
        cursor = self.conn.cursor()
        query = "select catId from categories natural inner join resources where resID = %s;"
        cursor.execute(query, (resID,))
        catID = cursor.fetchone()[0]
        self.conn.commit()
        return catID

    def getCatNameByResId(self, resID):
        cursor = self.conn.cursor()
        query = "select catName from categories natural inner join resources where resID = %s;"
        cursor.execute(query, (resID,))
        catName = cursor.fetchone()[0]
        self.conn.commit()
        return catName
