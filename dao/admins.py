from config.dbconfig import pg_config
import psycopg2

class AdminsDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllAdmins(self):
        cursor = self.conn.cursor()
        query = "select * from admins;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdminById(self, admID):
        cursor = self.conn.cursor()
        query = "select * from admins where admID = %s;"
        cursor.execute(query, (admID,))
        result = cursor.fetchone()
        return result

    def insert(self, uid):
        cursor = self.conn.cursor()
        query = "insert into admins(uID) values (%s) returning adminid;"
        cursor.execute(query, (uid,))
        adminid = cursor.fetchone()[0]
        self.conn.commit()
        return adminid