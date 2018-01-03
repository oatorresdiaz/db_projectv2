from config.dbconfig import pg_config
import psycopg2

class UsersDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
         self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, uID):
        cursor = self.conn.cursor()
        query = "select * from users where uID = %s;"
        cursor.execute(query, (uID,))
        result = cursor.fetchone()
        return result

    def getUsersByFirstName(self, firstName):
        cursor = self.conn.cursor()
        query = "select * from users where uFname = %s;"
        cursor.execute(query, (firstName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersByLastName(self, lastName):
        cursor = self.conn.cursor()
        query = "select * from users where uLname = %s;"
        cursor.execute(query, (lastName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUsersByFirstNameAndLastName(self, firstName, lastName):
        cursor = self.conn.cursor()
        query = "select * from users where uFname = %s and uLname = %s;"
        cursor.execute(query, (firstName, lastName))
        result = []
        for row in cursor:
            result.append(row)
        return result