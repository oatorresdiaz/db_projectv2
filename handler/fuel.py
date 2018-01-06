from flask import jsonify
from dao.fuel import FuelDAO

class FuelHandler:
    def build_fuel_dict(self, row):
        result = {}
        result['fuelID'] = row[0]
        result['resID'] = row[1]
        result['fuelCategory'] = row[2]
        return result

    def getAllFuel(self):
        dao = FuelDAO()
        fuel_list = dao.getAllFuel()
        result_list = []
        for row in fuel_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=result_list)

    def getFuelById(self, fuelID):
        dao = FuelDAO()
        row = dao.getFuelById(fuelID)
        if not row:
            return jsonify(Error="Fuel not found"), 404
        else:
            fuel = self.build_fuel_dict(row)
            return jsonify(Fuel=fuel)