from flask import jsonify
from dao.pricehistory import PriceHistoryDAO

class PriceHistoryHandler:
    def build_priceHistory_dict(self, row):
        result = {}
        result['phID'] = row[0]
        result['invID'] = row[1]
        result['startDate'] = row[2]
        result['thruDate'] = row[3]
        result['priceAtMoment'] = row[4]
        return result

    def getAllPriceHistory(self):
        dao = PriceHistoryDAO()
        priceHistory_list = dao.getAllPriceHistory()
        result_list = []
        for row in priceHistory_list:
            result = self.build_priceHistory_dict(row)
            result_list.append(result)
        return jsonify(PriceHistory=result_list)

    def getPriceHistoryById(self, phID):
        dao = PriceHistoryDAO()
        row = dao.getPriceHistoryById(phID)
        if not row:
            return jsonify(Error="Price History not found"), 404
        else:
            priceHistory = self.build_priceHistory_dict(row)
            return jsonify(PriceHistory=priceHistory)

    def getPriceHistoryByInventoryId(self, invID):
        dao = PriceHistoryDAO()
        row = dao.getPriceHistoryByInventoryId(invID)
        if not row:
            return jsonify(Error="Price History not found"), 404
        else:
            priceHistory = self.build_priceHistory_dict(row)
            return jsonify(PriceHistory=priceHistory)


