from flask import jsonify
from dao.telephonenumbers import TelephoneNumbersDAO

class TelephoneNumbersHandler:
    def build_telephoneNumber_dict(self, row):
        result = {}
        result['tID'] = row[0]
        result['uID'] = row[1]
        result['homeNumber'] = row[2]
        result['mobileNumber'] = row[3]
        result['workNumber'] = row[4]
        result['otherNumber'] = row[5]
        return result

    def getAllTelephoneNumbers(self):
        dao = TelephoneNumbersDAO()
        telephoneNumbers_list = dao.getAllTelephoneNumbers()
        result_list = []
        for row in telephoneNumbers_list:
            result = self.build_telephoneNumber_dict(row)
            result_list.append(result)
        return jsonify(TelephoneNumbers=result_list)

    def getTelephoneNumberById(self, tID):
        dao = TelephoneNumbersDAO()
        row = dao.getUserById(tID)
        if not row:
            return jsonify(Error="Telephone Number not found"), 404
        else:
            telephoneNumber = self.build_telephoneNumber_dict(row)
            return jsonify(TelephoneNumber=telephoneNumber)

    def searchUsers(self, args):
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
