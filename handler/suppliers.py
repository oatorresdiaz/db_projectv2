from flask import jsonify
from dao.suppliers import SuppliersDAO
from dao.users import UsersDAO

class SuppliersHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['uID'] = row[0]
        result['uFirstName'] = row[1]
        result['uLastName'] = row[2]
        result['uGender'] = row[3]
        result['uBirthDate'] = row[4]
        result['addID'] = row[5]
        result['city'] = row[6]
        result['street'] = row[7]
        result['country'] = row[8]
        result['zipcode'] = row[9]
        result['tID'] = row[10]
        result['homeNumber'] = row[11]
        result['mobileNumber'] = row[12]
        result['workNumber'] = row[13]
        result['otherNumber'] = row[14]
        result['suppID'] = row[15]
        return result

    def build_inv_dict(self, row):
        result = {}
        result['catID'] = row[0]
        result['resID'] = row[1]
        result['invID'] = row[2]
        result['suppID'] = row[3]
        result['invDate'] = row[4]
        result['invQty'] = row[5]
        result['invReserved'] = row[6]
        result['invAvailable'] = row[7]
        result['invPrice'] = row[8]
        result['resName'] = row[9]
        result['catName'] = row[10]
        return result

    def build_order_dict(self, row):
        result = {}
        result['ordQty'] = row[0]
        result['ordDate'] = row[1]
        result['ordExpDate'] = row[2]
        result['ordType'] = row[3]
        result['ordPrice'] = row[4]
        result['suppID'] = row[5]
        result['resName'] = row[6]
        result['resSpecifications'] = row[7]
        return result

    def getAllSuppliers(self):
        dao = SuppliersDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getSupplierById(self, suppID):
        dao = SuppliersDAO()
        row = dao.getSupplierById(suppID)
        if not row:
            return jsonify(Error="User not found"), 404
        else:
            supplier = self.build_supplier_dict(row)
            return jsonify(Supplier=supplier)


    def insertSupplier(self, form):
        if len(form) != 1:
            return jsonify(Error = "Malformed post request"), 400
        else:
            uid = form['uid']
            row = UsersDAO.getUserById(uid)
            if not row:
                return jsonify(Error="User not found"), 404
            else:
                if uid:
                    dao = SuppliersDAO()
                    suppid = dao.insert(uid)
                    result = self.build_supplier_attributes(suppid, uid)
                    return jsonify(Admin=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in post request"), 400

    def searchSuppliers(self, args):
        pass
    def getInventoryBySupplierId(self, suppID):
        dao = SuppliersDAO()
        if not dao.getSupplierById(suppID):
            return jsonify(Error="Supplier Not Found"), 404
        inventory_list = dao.getInventoryBySupplierId(suppID)
        result_list = []
        for row in inventory_list:
            result = self.build_inv_dict(row)
            result_list.append(result)
        return jsonify(SupplierInventory=result_list)

    def getOrdersBySupplierId(self, suppID):
        dao = SuppliersDAO()
        if not dao.getSupplierById(suppID):
            return jsonify(Error="Supplier Not Found"), 404
        orders_list = dao.getOrdersBySupplierId(suppID)
        result_list = []
        for row in orders_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(SupplierOrders=result_list)