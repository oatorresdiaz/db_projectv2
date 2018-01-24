from flask import jsonify
from dao.users import UsersDAO
from dao.addresses import AddressesDAO
from dao.telephonenumbers import TelephoneNumbersDAO

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

    def build_user_attributes(self, uid, uFirstName, uLastName, uGender, uBirthDate, addID, city, street, country,
                              zipcode, tID, homeNumber, mobileNumber, workNumber, otherNumber):
        result = {}
        result['uID'] = uid
        result['uFirstName'] = uFirstName
        result['uLastName'] = uLastName
        result['uGender'] = uGender
        result['uBirthDate'] = uBirthDate
        result['addID'] = addID
        result['city'] = city
        result['street'] = street
        result['country'] = country
        result['zipcode'] = zipcode
        result['tID'] = tID
        result['homeNumber'] = homeNumber
        result['mobileNumber'] = mobileNumber
        result['workNumber'] = workNumber
        result['otherNumber'] = otherNumber
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

    def insertUser(self, form):
        if len(form) != 12:
            return jsonify(Error="Malformed post request"), 400
        else:
            uFirstName = form['uFirstName']
            uLastName = form['uLastName']
            uGender = form['uGender']
            uBirthDate = form['uBirthDate']
            city = form['city']
            street = form['street']
            country = form['country']
            zipcode = form['zipcode']
            homeNumber = form['homeNumber']
            mobileNumber = form['mobileNumber']
            workNumber = form['workNumber']
            otherNumber = form['otherNumber']
            if uFirstName and uLastName and uGender and uBirthDate and city and street and country and zipcode and (homeNumber or mobileNumber or workNumber or otherNumber):
                uDao = UsersDAO()
                uID = uDao.insert(uFirstName, uLastName, uGender, uBirthDate)
                addDao = AddressesDAO()
                addID = addDao.insert(uID, city, street, country, zipcode)
                telDao = TelephoneNumbersDAO()
                tID = telDao.insert(uID, homeNumber, mobileNumber, workNumber, otherNumber)
                result = self.build_user_attributes(uID, uFirstName, uLastName, uGender, uBirthDate, addID, city, street, country, zipcode, tID, homeNumber, mobileNumber, workNumber, otherNumber)
                return jsonify(User=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400