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

    def getCreditCardsByUserId(self, uID):
        cursor = self.conn.cursor()
        query = "select * from creditcards where uID = %s;"
        cursor.execute(query, (uID,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, uID, ccNumber, ccExpDate, ccSecurityCode):
        cursor = self.conn.cursor()
        query = "insert into creditcards(uID, ccNumber, ccExpDate, ccSecurityCode) values (%s, %s, %s, %s) returning ccID;"
        cursor.execute(query, (uID, ccNumber, ccExpDate, ccSecurityCode,))
        ccID = cursor.fetchone()[0]
        self.conn.commit()
        return ccID

    def update(self, ccID, uID, ccNumber, ccExpDate, ccSecurityCode):
        cursor = self.conn.cursor()
        query = "update creditcards set uID = %s, ccNumber = %s, ccExpDate = %s, ccSecurityCode = %s where ccID = %s;"
        cursor.execute(query, (uID, ccNumber, ccExpDate, ccSecurityCode, ccID,))
        self.conn.commit()
        return ccID