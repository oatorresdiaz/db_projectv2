from flask import jsonify
from dao.admins import AdminsDAO
from dao.users import UsersDAO

class AdminsHandler:
    def build_admin_dict(self, row):
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
        result['adminID'] = row[15]
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

    def insertAdmin(self, form): #TODO: FOR PHASE 3
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

    def searchAdminsByArguments(self, args):
        dao = AdminsDAO()
        if not 'orderby' in args:
            admins_list = dao.searchAdminsByArguments(args)
        elif (len(args) == 1) and 'orderby' in args:
            admins_list = dao.searchAdminsWithSorting(args.get('orderby'))
        else:
            admins_list = dao.searchAdminsByArgumentsWithSorting(args)
        result_list = []
        for row in admins_list:
            result = self.build_admin_dict(row)
            result_list.append(result)
        return jsonify(Admins=result_list)