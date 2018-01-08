from flask import jsonify
from dao.clothing import ClothingsDAO

class ClothingHandler:
    def build_clothing_dict(self, row):
        result = {}
        result['clothID'] = row[0]
        result['resID'] = row[1]
        result['clothGender'] = row[2]
        result['clothType'] = row[3]
        result['clothBrand'] = row[4]
        result['clothSize'] = row[5]
        result['clothColor'] = row[6]
        result['clothDesignPattern'] = row[7]
        return result

    def getAllClothing(self):
        dao = ClothingsDAO()
        clothing_list = dao.getAllClothings()
        result_list = []
        for row in clothing_list:
            result = self.build_clothing_dict(row)
            result_list.append(result)
        return jsonify(Clothing=result_list)

    def getCloth(self, clothID):
        dao = ClothingsDAO()
        row = dao.getClothingById(clothID)
        if not row:
            return jsonify(Error="Cloth not found"), 404
        else:
            cloth = self.build_clothing_dict(row)
            return jsonify(Cloth=cloth)