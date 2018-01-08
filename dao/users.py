from config.dbconfig import pg_config
import psycopg2

class UsersDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join addresses natural inner join credentials natural inner join telephonenumbers;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, uID):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join addresses natural inner join credentials natural inner join telephonenumbers where uID=%s;"
        cursor.execute(query, (uID,))
        result = cursor.fetchone()
        return result

    def getUsersByFirstName(self, firstName):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join addresses natural inner join credentials natural inner join telephonenumbers where ufirstname = %s;"
        cursor.execute(query, (firstName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersByLastName(self, lastName):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join addresses natural inner join credentials natural inner join telephonenumbers where ulastname = %s;"
        cursor.execute(query, (lastName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersByFirstNameAndLastName(self, firstName, lastName):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join addresses natural inner join credentials natural inner join telephonenumbers where ufirstname = %s and ulastname = %s;"
        cursor.execute(query, (firstName, lastName))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersByArguments(self, args):
        cursor = self.conn.cursor()
        arguments = ""
        values = list(args.values())
        for arg in args:
            arguments = arguments + arg + "= %s" + " and "
        arguments = arguments[:-5]  + ";" #Remove the last ' and '
        query = "select * from users natural inner join addresses natural inner join credentials natural inner join telephonenumbers where " + arguments
        cursor.execute(query, values)
        print(cursor.query)
        result = []
        for row in cursor:
            result.append(row)
        return result

