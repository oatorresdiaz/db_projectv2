from config.dbconfig import pg_config
import psycopg2

class RequestsDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = "select * from requests natural inner join resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestById(self, reqID):
        cursor = self.conn.cursor()
        query = "select * from requests natural inner join resources where reqID = %s;"
        cursor.execute(query, (reqID,))
        result = cursor.fetchone()
        return result

    def searchRequestsByArguments(self, args):
        cursor = self.conn.cursor()
        arguments = ""
        values = list(args.values())
        for arg in args:
            arguments = arguments + arg + "= %s" + " and "
        arguments = arguments[:-5]  # Remove the last ' and '
        query = "select * from requests natural inner join resources where " + arguments
        cursor.execute(query, values)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchRequestsWithSorting(self, orderby):
        cursor = self.conn.cursor()
        query = "select * from requests natural inner join resources order by " + orderby
        cursor.execute(query)
        print(cursor.query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def searchRequestsByArgumentsWithSorting(self, args):
        cursor = self.conn.cursor()
        arguments = ""
        values = list(args.values())
        values.remove(args.get('orderby'))
        for arg in args:
            if arg != 'orderby':
                arguments = arguments + arg + "= %s" + " and "
        arguments = arguments[:-5]  # Remove the last ' and '
        query = "select * from requests natural inner join resources where " + arguments + " order by " + args.get('orderby')
        cursor.execute(query, values)
        print(cursor.query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, reqID, resID, reqQty, reqUnit, reqDate):
        cursor = self.conn.cursor()
        query = "insert into requests(reqID, resID, reqQty, reqUnit, reqDate) values (%s, %s, %s, %s, %s);"
        cursor.execute(query, (reqID, resID, reqQty, reqUnit, reqDate,))
        self.conn.commit()
        return resID, reqID