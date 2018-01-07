from config.dbconfig import pg_config
import psycopg2

class CredentialsDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllCredentials(self):
        cursor = self.conn.cursor()
        query = "select * from credentials;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCredentialById(self, cID):
        cursor = self.conn.cursor()
        query = "select * from credentials where cID = %s;"
        cursor.execute(query, (cID,))
        result = cursor.fetchone()
        return result

    def login(self, uname, passwd):
        cursor = self.conn.cursor()
        cursor.execute("select * from credentials Where username = %s And password = %s;", (uname, passwd))
        try:
            if cursor.fetchone():
                print("Login successful")
                result = "true"
                return result
            else:
                print("Wrong credentials. Login failed.")
                result = "false"
                return result
        except Exception as e:
            print("DB Error.")