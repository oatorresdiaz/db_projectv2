from flask import jsonify
from dao.powergenerators import PowerGeneratorsDAO

class PowerGeneratorsHandler:
    def build_powerGenerator_dict(self, row):
        result = {}
        result['pgID'] = row[0]
        result['resID'] = row[1]
        result['pgType'] = row[2]
        result['pgBrand'] = row[3]
        result['pgPower'] = row[4]
        result['pgFuelType'] = row[5]
        return result

    def getAllPowerGenerators(self):
        dao = PowerGeneratorsDAO()
        powerGenerators_list = dao.getAllPowerGenerators()
        result_list = []
        for row in powerGenerators_list:
            result = self.build_powerGenerator_dict(row)
            result_list.append(result)
        return jsonify(PowerGenerators=result_list)

    def getMedicationById(self, pgID):
        dao = PowerGeneratorsDAO()
        row = dao.getPowerGeneratorById(pgID)
        if not row:
            return jsonify(Error="Power Generator not found"), 404
        else:
            powerGenerator = self.build_powerGenerator_dict(row)
            return jsonify(PowerGenerator=powerGenerator)