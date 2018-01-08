from flask import jsonify
from dao.water import WaterDAO

class WaterHandler:
    def build_water_dict(self, row):
        result = {}
        result['wID'] = row[0]
        result['resID'] = row[1]
        result['wCategory'] = row[2]
        result['wExpDate'] = row[3]
        return result

    def getAllWater(self):
        dao = WaterDAO()
        water_list = dao.getAllWater()
        result_list = []
        for row in water_list:
            result = self.build_water_dict(row)
            result_list.append(result)
        return jsonify(Water=result_list)

    def getWaterById(self, wID):
        dao = WaterDAO()
        row = dao.getWaterById(wID)
        if not row:
            return jsonify(Error="Water not found"), 404
        else:
            water = self.build_water_dict(row)
            return jsonify(Water=water)