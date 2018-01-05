from flask import jsonify
from dao.sells import SellsDAO

class SellsHandler:
    def build_sell_dict(self, row):
        result = {}
        result['invID'] = row[0]
        result['resID'] = row[1]
        return result

    def getAllSells(self):
        dao = SellsDAO()
        sells_list = dao.getAllSells()
        result_list = []
        for row in sells_list:
            result = self.build_sell_dict(row)
            result_list.append(result)
        return jsonify(Sells=result_list)
