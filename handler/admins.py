from flask import jsonify
from dao.admins import AdminsDAO

class AdminsHandler:
    def build_admin_dict(self, row):
        result = {}
        result['admID'] = row[0]
        result['uID'] = row[1]
        return result

    def getAllAdmins(self):
        dao = AdminsDAO()
        admins_list = dao.getAllAdmins()
        result_list = []
        for row in admins_list:
            result = self.build_admin_dict(row)
            result_list.append(result)
        return jsonify(Admins=result_list)

    def getAdminById(self, admID):
        dao = AdminsDAO()
        row = dao.getAdminById(admID)
        if not row:
            return jsonify(Error="User not found"), 404
        else:
            admin = self.build_admin_dict(row)
            return jsonify(Admin=admin)

    def searchAdmins(self, args):
        pass