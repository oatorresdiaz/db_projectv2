from flask import jsonify
from dao.batteries import BatteriesDAO

class BatteriesHandler:
    def build_battery_dict(self, row):
        result = {}
        result['bID'] = row[0]
        result['resID'] = row[1]
        result['bType'] = row[2]
        result['bBrand'] = row[3]
        return result

    def getAllBatteries(self):
        dao = BatteriesDAO()
        batteries_list = dao.getAllBatteries()
        result_list = []
        for row in batteries_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(Batteries=result_list)

    def getBatteryById(self, bID):
        dao = BatteriesDAO()
        row = dao.getBatteryById(bID)
        if not row:
            return jsonify(Error="Battery not found"), 404
        else:
            battery = self.build_battery_dict(row)
            return jsonify(Batteery=battery)