from config.dbconfig import pg_config
import psycopg2

class CreditCardsDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'], pg_config['host'], pg_config['port'])
         self.conn = psycopg2._connect(connection_url)

    def getAllCreditCards(self):
        cursor = self.conn.cursor()
        query = "select * from creditcards;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCreditCardById(self, ccID):
        cursor = self.conn.cursor()
        query = "select * from creditcards where ccID = %s;"
        cursor.execute(query, (ccID,))
        result = cursor.fetchone()
        return result