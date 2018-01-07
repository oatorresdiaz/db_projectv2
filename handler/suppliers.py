from flask import jsonify
from dao.suppliers import SuppliersDAO

class SuppliersHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['suppID'] = row[0]
        result['uID'] = row[1]
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


    def insertRequester(self, form):
        if len(form) != 1:
            return jsonify(Error = "Malformed post request"), 400
        else:
            uid = form['uid']
            row = UsersDAO.getUserById(uid)
            if not row:
                return jsonify(Error="User not found"), 404
            if uid:
                dao = AdminsDAO()
                adminid = dao.insert(uid)
                result = self.build_admin_attributes(adminid, uid)
                return jsonify(Admin=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def searchSuppliers(self, args):
        pass