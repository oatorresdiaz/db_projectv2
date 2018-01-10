from config.dbconfig import pg_config
import psycopg2

class RequestersDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllRequesters(self):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join addresses natural inner join telephonenumbers natural inner join requesters;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequesterById(self, reqID):
        cursor = self.conn.cursor()
        query = "select * from users natural inner join addresses natural inner join telephonenumbers natural inner join requesters where reqID = %s;"
        cursor.execute(query, (reqID,))
        result = cursor.fetchone()
        return result

    def insert(self, uid):
        cursor = self.conn.cursor()
        query = "insert into requesters(uID) values (%s) returning reqid;"
        cursor.execute(query, (uid,))
        reqid = cursor.fetchone()[0]
        self.conn.commit()
        return reqid

    def getOrdersByRequesterId(self, reqID):
        cursor = self.conn.cursor()
        query = "select ordQty, ordDate, ordExpDate, ordType, ordPrice, suppID, resName, resSpecifications from orders natural inner join inventory natural inner join sells natural inner join resources where reqID = %s"
        cursor.execute(query, (reqID, ))
        result = []
        for row in cursor:
            result.append(row)
        return result