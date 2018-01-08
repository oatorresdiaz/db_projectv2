from flask import jsonify
from dao.medications import MedicationsDAO

class MedicationsHandler:
    def build_medication_dict(self, row):
        result = {}
        result['medID'] = row[0]
        result['resID'] = row[1]
        result['medName'] = row[2]
        result['medBrand'] = row[3]
        result['medType'] = row[4]
        result['medOz'] = row[5]
        result['medExpDate'] = row[6]
        return result

    def getAllMedications(self):
        dao = MedicationsDAO()
        medicalDevices_list = dao.getAllMedications()
        result_list = []
        for row in medicalDevices_list:
            result = self.build_medication_dict(row)
            result_list.append(result)
        return jsonify(Medications=result_list)

    def getMedicationById(self, medID):
        dao = MedicationsDAO()
        row = dao.getMedicationById(medID)
        if not row:
            return jsonify(Error="Medication not found"), 404
        else:
            medication = self.build_medication_dict(row)
            return jsonify(Medication=medication)