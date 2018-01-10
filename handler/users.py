from flask import jsonify
from dao.users import UsersDAO

class UsersHandler:
    def build_user_dict(self, row):
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
        firstName = args.get('uFirstName')
        lastName = args.get('uLastName')
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

    def searchUsersByArguments(self, args):
        dao = UsersDAO()
        if not 'orderby' in args:
            users_list = dao.searchUsersByArguments(args)
        elif (len(args) == 1) and 'orderby' in args:
            users_list = dao.searchUsersWithSorting(args.get('orderby'))
        else:
            users_list = dao.searchUsersByArgumentsWithSorting(args)
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)