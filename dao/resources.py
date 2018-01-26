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
        query = "Select * From resources Where resID IN (Select resID From Inventory NATURAL INNER JOIN Resources Where inventory.invavailable > 0)"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCity(self, city):
        cursor = self.conn.cursor()
        query = "Select resID, resName, catID, resSpecifications from addresses natural inner join suppliers natural inner join inventory natural inner join sells natural inner join resources where city = %s;"
        cursor.execute(query, (city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategoryName(self, catName):
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
        print(cursor.query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByInventoryId(self, invID):
        cursor = self.conn.cursor()
        query = "select resID from resources natural inner join inventory where invID = %s;"
        cursor.execute(query, (invID,))
        resID = cursor.fetchone()[0]
        return resID

    def searchResourcesByArguments(self, args):
        cursor = self.conn.cursor()
        arguments = ""
        values = list(args.values())
        for arg in args:
            arguments = arguments + arg + "= %s" + " and "
        arguments = arguments[:-5]  # Remove the last ' and '
        query = "select * from resources where " + arguments
        cursor.execute(query, values)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchResourcesWithSorting(self, orderby):
        cursor = self.conn.cursor()
        query = "select * from resources order by " + orderby
        cursor.execute(query)
        print(cursor.query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchResourcesByArgumentsWithSorting(self, args):
        cursor = self.conn.cursor()
        arguments = ""
        values = list(args.values())
        values.remove(args.get('orderby'))
        for arg in args:
            if arg != 'orderby':
                arguments = arguments + arg + "= %s" + " and "
        arguments = arguments[:-5]  # Remove the last ' and '
        query = "select * from resources where " + arguments + " order by " + args.get('orderby')
        cursor.execute(query, values)
        print(cursor.query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, resName, catID, resSpecifications):
        cursor = self.conn.cursor()
        query = "insert into resources(resName, catID, resSpecifications) values (%s, %s, %s) returning resID;"
        cursor.execute(query, (resName, catID, resSpecifications,))
        resID = cursor.fetchone()[0]
        self.conn.commit()
        return resID

    def getResourceId(self, resName, catID, resspecifications):
        cursor = self.conn.cursor()
        query = "select resID from inventory natural inner join sells natural inner join resources where resName = %s and catID = %s and resSpecifications = %s;"
        cursor.execute(query, (resName, catID, resspecifications,))
        resID = cursor.fetchone()[0]
        self.conn.commit()
        return resID

    def getResourceNameByResId(self, resID):
        cursor = self.conn.cursor()
        query = "select resName from resources where resID = %s;"
        cursor.execute(query, (resID,))
        resName = cursor.fetchone()[0]
        self.conn.commit()
        return resName

    def getResourceSpecificationsByResId(self, resID):
        cursor = self.conn.cursor()
        query = "select resSpecifications from resources where resID = %s;"
        cursor.execute(query, (resID,))
        resSpecifications = cursor.fetchone()[0]
        self.conn.commit()
        return resSpecifications
