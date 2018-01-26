from config.dbconfig import pg_config
import psycopg2

class AdminsDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllAdmins(self):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join addresses natural inner join telephonenumbers natural inner join admins;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdminById(self, adminID):
        cursor = self.conn.cursor()
        query = "select * from admins where adminID = %s;"
        cursor.execute(query, (adminID,))
        result = cursor.fetchone()
        return result

    def getAdminByUserId(self, uID):
        cursor = self.conn.cursor()
        query = "select * from admins where uID = %s;"
        cursor.execute(query, (uID,))
        result = cursor.fetchone()
        return result

    def insert(self, uID):
        cursor = self.conn.cursor()
        query = "insert into admins(uID) values (%s) returning adminid;"
        cursor.execute(query, (uID,))
        adminid = cursor.fetchone()[0]
        self.conn.commit()
        return adminid

    def searchAdminsByArguments(self, args):
        cursor = self.conn.cursor()
        arguments = ""
        values = list(args.values())
        for arg in args:
            arguments = arguments + arg + "= %s" + " and "
        arguments = arguments[:-5]  # Remove the last ' and '
        query = "select * from users natural inner join addresses natural inner join telephonenumbers natural inner join admins where " + arguments
        cursor.execute(query, values)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchAdminsWithSorting(self, orderby):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join addresses natural inner join telephonenumbers natural inner join admins order by " + orderby
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchAdminsByArgumentsWithSorting(self, args):
        cursor = self.conn.cursor()
        arguments = ""
        values = list(args.values())
        values.remove(args.get('orderby'))
        for arg in args:
            if arg != 'orderby':
                arguments = arguments + arg + "= %s" + " and "
        arguments = arguments[:-5]  # Remove the last ' and '
        query = "select * from users natural inner join addresses natural inner join telephonenumbers natural inner join admins where " + arguments + " order by " + args.get('orderby')
        cursor.execute(query, values)
        result = []
        for row in cursor:
            result.append(row)
        return result


