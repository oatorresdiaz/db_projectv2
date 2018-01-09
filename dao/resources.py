from config.dbconfig import pg_config
import psycopg2

class ResourcesDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceById(self, resID):
        cursor = self.conn.cursor()
        query = "select * from resources where resID = %s;"
        cursor.execute(query, (resID,))
        result = cursor.fetchone()
        return result

    def getAllAvailableResources(self):
        cursor = self.conn.cursor()
        query = "Select * " \
                "From Resources " \
                "Where resID IN (Select resID" \
                                " From Inventory " \
                                "NATURAL INNER JOIN Resources Where inventory.mavaiable > 0)" \

            #"select resID from inventory NATURAL INNER JOIN sells NATURAL INNER JOIN resources Where mavaiable > 0"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategories(self, catName):
        cursor = self.conn.cursor()
        query = "Select resName, resSpecifications From Requests natural inner join resources natural inner join Categories Where catName = %s Order by resName;"
        cursor.execute(query, (catName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAvailableResourcesByCategories(self, catName):
        cursor = self.conn.cursor()
        query = "Select resName, resSpecifications From Sells natural inner join resources natural inner join Categories Where invID IN (Select invID From Inventory Where invAvailable > 0) And catName = %s Order by resName;"
        cursor.execute(query, (catName,))
        result = []
        for row in cursor:
            result.append(row)
        return result