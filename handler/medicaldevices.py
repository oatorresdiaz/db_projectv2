from flask import jsonify
from dao.medicaldevices import MedicalDevicesDAO

class MedicalDevicesHandler:
    def build_medicalDevice_dict(self, row):
        result = {}
        result['mdID'] = row[0]
        result['resID'] = row[1]
        result['mdName'] = row[2]
        result['mdType'] = row[3]
        result['mdWeight'] = row[4]
        result['mdSize'] = row[5]
        return result

    def getAllMedicalDevices(self):
        dao = MedicalDevicesDAO()
        medicalDevices_list = dao.getAllMedicalDevices()
        result_list = []
        for row in medicalDevices_list:
            result = self.build_medicalDevice_dict(row)
            result_list.append(result)
        return jsonify(MedicalDevices=result_list)

    def getMedicalDeviceById(self, mdID):
        dao = MedicalDevicesDAO()
        row = dao.getMedicalDeviceById(mdID)
        if not row:
            return jsonify(Error="Medical Device not found"), 404
        else:
            medicalDevice = self.build_medicalDevice_dict(row)
            return jsonify(MedicalDevice=medicalDevice)