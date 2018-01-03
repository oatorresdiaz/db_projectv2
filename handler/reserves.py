from flask import jsonify
from dao.reserves import ReservesDAO

class ReservesHandler:
    def build_reserve_dict(self, row):
        result = {}
        result['reqID'] = row[0]
        result['invID'] = row[1]
        result['resDate'] = row[2]
        result['resExpDate'] = row[3]
        result['resQty'] = row[4]
        return result

    def getAllReserves(self):
        dao = ReservesDAO()
        reserves_list = dao.getAllReserves()
        result_list = []
        for row in reserves_list:
            result = self.build_reserve_dict(row)
            result_list.append(result)
        return jsonify(Reserves=result_list)

    def searchReserves(self, args):
        pass