from flask import jsonify
from dao.users import UsersDAO

class UsersHandler:
    def build_user_dict(self, row):
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
        return result

    def getAllUsers(self):
        dao = UsersDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getUserById(self, uID):
        dao = UsersDAO()
        row = dao.getUserById(uID)
        if not row:
            return jsonify(Error="User not found"), 404
        else:
            user = self.build_user_dict(row)
            return jsonify(User=user)

    def searchUsers(self, args): #TODO: EXPAND 
        firstName = args.get('uFname')
        lastName = args.get('uLname')
        dao = UsersDAO()
        users_list = []
        if (len(args) == 2) and firstName and lastName:
            users_list = dao.getUsersByFirstNameAndLastName(firstName, lastName)
        elif (len(args) == 1) and firstName:
            users_list = dao.getUsersByFirstName(firstName)
        elif (len(args) == 1) and lastName:
            users_list = dao.getUsersByLastName(lastName)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users = result_list)
