from flask import jsonify
from dao.orders import OrdersDAO
from dao.inventory import InventoryDAO

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

    def build_order_attributes(self, reqID, invID, ordQty, ordDate, ordExpDate, ordType, ordPrice):
        result = {}
        result['reqID'] = reqID
        result['invID'] = invID
        result['ordQty'] = ordQty
        result['ordDate'] = ordDate
        result['ordExpDate'] = ordExpDate
        result['ordType'] = ordType
        result['ordPrice'] = ordPrice
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

    def insertOrder(self, form):
        if len(form) != 12:
            return jsonify(Error="Malformed post request"), 400
        else:
            reqID = form['reqID']
            invID = form['invID']
            ordQty = form['ordQty']
            ##ordDate = form['ordDate']
            ##ordExpDate = form['ordExpDate']
            ##ordType = form['ordType']
            ##ordPrice = form['ordPrice']
            if reqID and invID and ordQty:
                ordDao = OrdersDAO()

                invAvailable = InventoryDAO().getAvailableById(invID)
                if ordQty > invAvailable:
                    return jsonify(Error="Value out of bounds"), 400

                ordPrice = InventoryDAO().getPriceById(invID)[0]
                if ordPrice > 0:
                    ordType = "Purchase"
                    ordID = ordDao.insertPurchase(reqID, invID, ordQty)

                else:
                    ordType = "Reserve"
                    ordID = ordDao.insertReserve(reqID, invID, ordQty)


                result = self.build_user_attributes(uID, uFirstName, uLastName, uGender, uBirthDate, addID, city, street, country, zipcode, tID, homeNumber, mobileNumber, workNumber, otherNumber)
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400
