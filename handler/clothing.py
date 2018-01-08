from flask import jsonify
from dao.clothing import ClothingsDAO

class ClothingHandler:
    def build_clothing_dict(self, row):
        result = {}
        result['clothID'] = row[0]
        result['resID'] = row[1]
        result['catID'] = row[2]
        result['clothGender'] = row[3]
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

    def getClothingById(self, clothID):
        dao = ClothingsDAO()
        row = dao.getClothingById(clothID)
        if not row:
            return jsonify(Error="Cloth not found"), 404
        else:
            cloth = self.build_clothing_dict(row)
            return jsonify(Cloth=cloth)

    def getClothingByResourceId(self, resID):
        dao = ClothingsDAO()
        row = dao.getClothingByResourceId(resID)
        if not row:
            return jsonify(Error="Cloth not found"), 404
        else:
            cloth = self.build_clothing_dict(row)
            return jsonify(Cloth=cloth)

    def getClothingByCategoryId(self, catID):
        dao = ClothingsDAO()
        row = dao.getClothingByCategoryId(catID)
        if not row:
            return jsonify(Error="Cloth not found"), 404
        else:
            cloth = self.build_clothing_dict(row)
            return jsonify(Cloth=cloth)

    def getClothingByGender(self, clothGender):
        dao = ClothingsDAO()
        row = dao.getClothingByGender(clothGender)
        if not row:
            return jsonify(Error="Cloth not found"), 404
        else:
            cloth = self.build_clothing_dict(row)
            return jsonify(Cloth=cloth)

    def getClothingByBrand(self, clothBrand):
        dao = ClothingsDAO()
        row = dao.getClothingByBrand(clothBrand)
        if not row:
            return jsonify(Error="Cloth not found"), 404
        else:
            cloth = self.build_clothing_dict(row)
            return jsonify(Cloth=cloth)

    def getClothingBySize(self, clothSize):
        dao = ClothingsDAO()
        row = dao.getClothingBySize(clothSize)
        if not row:
            return jsonify(Error="Cloth not found"), 404
        else:
            cloth = self.build_clothing_dict(row)
            return jsonify(Cloth=cloth)

    def getClothingByColor(self, clothColor):
        dao = ClothingsDAO()
        row = dao.getClothingByColor(clothColor)
        if not row:
            return jsonify(Error="Cloth not found"), 404
        else:
            cloth = self.build_clothing_dict(row)
            return jsonify(Cloth=cloth)

    def getClothingByDesignPattern(self, clothDesignPattern):
        dao = ClothingsDAO()
        row = dao.getClothingByDesignPattern(clothDesignPattern)
        if not row:
            return jsonify(Error="Cloth not found"), 404
        else:
            cloth = self.build_clothing_dict(row)
            return jsonify(Cloth=cloth)

    def searchClothing(self, args):
        pass
