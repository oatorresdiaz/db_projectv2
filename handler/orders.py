from flask import jsonify
from dao.orders import OrdersDAO

class OrdersHandler:
    def build_order_dict(self, row):
        result = {}
        result['reqID'] = row[0]
        result['invID'] = row[1]
        result['orderQty'] = row[2]
        result['ordDate'] = row[3]
        result['ordExpDate'] = row[4]
        result['ordType'] = row[5]
        return result

    def getAllOrders(self):
        dao = OrdersDAO()
        orders_list = dao.getAllOrders()
        result_list = []
        for row in orders_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    def searchOrders(self, args):
        pass