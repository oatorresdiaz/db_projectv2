from flask import jsonify
from dao.heavyequipment import HeavyEquipmentsDAO

class HeavyEquipmentsHandler:
    def build_heavyEquipment_dict(self, row):
        result = {}
        result['heID'] = row[0]
        result['resID'] = row[1]
        result['heName'] = row[2]
        result['heType'] = row[3]
        result['heWeight'] = row[4]
        result['heSize'] = row[5]
        return result

    def getAllHeavyEquipment(self):
        dao = HeavyEquipmentsDAO()
        heavyEquipments_list = dao.getAllHeavyEquipments()
        result_list = []
        for row in heavyEquipments_list:
            result = self.build_heavyEquipment_dict(row)
            result_list.append(result)
        return jsonify(HeavyEquipments=result_list)

    def getHeavyEquipment(self, heID):
        dao = HeavyEquipmentsDAO()
        row = dao.getHeavyEquipmentById(heID)
        if not row:
            return jsonify(Error="Heavy Equipment not found"), 404
        else:
            heavyEquipment = self.build_heavyEquipment_dict(row)
            return jsonify(HeavyEquipment=heavyEquipment)