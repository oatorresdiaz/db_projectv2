from flask import jsonify
from dao.suppliers import SuppliersDAO

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
        result['cID'] = row[10]
        result['username'] = row[11]
        result['password'] = row[12]
        result['email'] = row[13]
        result['tID'] = row[14]
        result['homeNumber'] = row[15]
        result['mobileNumber'] = row[16]
        result['workNumber'] = row[17]
        result['otherNumber'] = row[18]
        result['suppID'] = row[19]
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