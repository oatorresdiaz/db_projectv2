from flask import jsonify
from dao.admins import AdminsDAO
from dao.users import UsersDAO

class AdminsHandler:
    def build_admin_dict(self, row):
        result = {}
        result['adminID'] = row[0]
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

    def getAdminById(self, adminID):
        dao = AdminsDAO()
        row = dao.getAdminById(adminID)
        if not row:
            return jsonify(Error="User not found"), 404
        else:
            admin = self.build_admin_dict(row)
            return jsonify(Admin=admin)

    def getAdminByUserId(self, uID):
        dao = AdminsDAO()
        row = dao.getAdminByUserId(uID)
        if not row:
            return jsonify(Error="User not found"), 404
        else:
            admin = self.build_admin_dict(row)
            return jsonify(Admin=admin)

    def insertAdmin(self, form):
        if len(form) != 1:
            return jsonify(Error = "Malformed post request"), 400
        else:
            uid = form['uid']
            row = UsersDAO.getUserById(uid)
            if not row:
                return jsonify(Error="User not found"), 404
            else:
                if uid:
                    dao = AdminsDAO()
                    adminid = dao.insert(uid)
                    result = self.build_admin_attributes(adminid, uid)
                    return jsonify(Admin=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in post request"), 400

    def searchAdmins(self, args):
        pass