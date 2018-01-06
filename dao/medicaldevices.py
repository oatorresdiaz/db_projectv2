from config.dbconfig import pg_config
import psycopg2

class MedicalDevicesDAO:
    def __init__(self):
         connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'], pg_config['user'], pg_config['passwd'])
         self.conn = psycopg2._connect(connection_url)

    def getAllMedicalDevices(self):
        cursor = self.conn.cursor()
        query = "select * from medicaldevices;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getMedicalDeviceById(self, mdID):
        cursor = self.conn.cursor()
        query = "select * from medicaldevices where mdID = %s;"
        cursor.execute(query, (mdID,))
        result = cursor.fetchone()
        return result