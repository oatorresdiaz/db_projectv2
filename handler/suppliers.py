from flask import jsonify
from dao.suppliers import SuppliersDAO

class SuppliersHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['uID'] = row[0]
        result['uFname'] = row[1]
        result['uLname'] = row[2]
        result['uGender'] = row[3]
        result['uBirthDate'] = row[4]
        result['uCity'] = row[5]
        result['uStreet'] = row[6]
        result['uCountry'] = row[7]
        result['uZipCode'] = row[8]
        result['username'] = row[9]
        result['password'] = row[10]
        result['suppID'] = row[11]
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

    def searchSuppliers(self, args):
        pass