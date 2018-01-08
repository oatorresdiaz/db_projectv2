from flask import jsonify
from dao.batteries import BatteriesDAO

class BatteriesHandler:
    def build_battery_dict(self, row):
        result = {}
        result['bID'] = row[0]
        result['resID'] = row[1]
        result['catID'] = row[2]
        result['bType'] = row[3]
        result['bBrand'] = row[4]
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
            return jsonify(Battery=battery)

    def getBatteryByResourceId(self, resID):
        dao = BatteriesDAO()
        row = dao.getBatteryByResourceId(resID)
        if not row:
            return jsonify(Error="Battery not found"), 404
        else:
            battery = self.build_battery_dict(row)
            return jsonify(Battery=battery)

    def getBatteryByCategoryId(self, catID):
        dao = BatteriesDAO()
        row = dao.getBatteryByCategoryId(catID)
        if not row:
            return jsonify(Error="Battery not found"), 404
        else:
            battery = self.build_battery_dict(row)
            return jsonify(Battery=battery)

    def getBatteryByType(self, bType):
        dao = BatteriesDAO()
        row = dao.getBatteryByType(bType)
        if not row:
            return jsonify(Error="Battery not found"), 404
        else:
            battery = self.build_battery_dict(row)
            return jsonify(Battery=battery)

    def getBatteryByBrand(self, bBrand):
        dao = BatteriesDAO()
        row = dao.getBatteryByBrand(bBrand)
        if not row:
            return jsonify(Error="Battery not found"), 404
        else:
            battery = self.build_battery_dict(row)
            return jsonify(Battery=battery)

    def searchBatteries(self, args):
            pass
