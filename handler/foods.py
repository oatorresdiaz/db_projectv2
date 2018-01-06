from flask import jsonify
from dao.foods import FoodsDAO

class FoodsHandler:
    def build_food_dict(self, row):
        result = {}
        result['fID'] = row[0]
        result['resID'] = row[1]
        result['fCategory'] = row[2]
        result['fExpDate'] = row[3]
        return result

    def getAllFoods(self):
        dao = FoodsDAO()
        foods_list = dao.getAllFoods()
        result_list = []
        for row in foods_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return jsonify(Food=result_list)

    def getFoodById(self, fID):
        dao = FoodsDAO()
        row = dao.getFoodById(fID)
        if not row:
            return jsonify(Error="Food not found"), 404
        else:
            food = self.build_food_dict(row)
            return jsonify(Food=food)