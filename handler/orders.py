from flask import jsonify
from dao.orders import OrdersDAO

class OrdersHandler:
    def build_order_dict(self, row):
        result = {}
        result['reqID'] = row[0]
        result['invID'] = row[1]
        result['ordQty'] = row[2]
        result['ordDate'] = row[3]
        result['ordExpDate'] = row[4]
        result['ordType'] = row[5]
        result['ordPrice'] = row[6]
        return result

    def getAllOrders(self):
        dao = OrdersDAO()
        orders_list = dao.getAllOrders()
        result_list = []
        for row in orders_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

    def searchOrdersByArguments(self, args):
        dao = OrdersDAO()
        if not 'orderby' in args:
            orders_list = dao.searchOrdersByArguments(args)
        elif (len(args) == 1) and 'orderby' in args:
            orders_list = dao.searchOrdersWithSorting(args.get('orderby'))
        else:
            orders_list = dao.searchOrdersByArgumentsWithSorting(args)
        result_list = []
        for row in orders_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)