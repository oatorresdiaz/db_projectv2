from flask import jsonify
from dao.ice import IceDAO

class HeavyEquipmentsHandler:
    def build_ice_dict(self, row):
        result = {}
        result['iceID'] = row[0]
        result['resID'] = row[1]
        result['iceWeight'] = row[2]
        result['iceContainer'] = row[3]
        return result

    def getAllIce(self):
        dao = IceDAO()
        ice_list = dao.getAllIce()
        result_list = []
        for row in ice_list:
            result = self.build_ice_dict(row)
            result_list.append(result)
        return jsonify(Ice=result_list)

    def getIceById(self, iceID):
        dao = IceDAO()
        row = dao.getIceById(iceID)
        if not row:
            return jsonify(Error="Ice not found"), 404
        else:
            ice = self.build_ice_dict(row)
            return jsonify(Ice=ice)