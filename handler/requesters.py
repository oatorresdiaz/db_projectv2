from flask import jsonify
from dao.requesters import RequestersDAO
from dao.users import UsersDAO

class RequestersHandler:
    def build_requester_dict(self, row):
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
        result['reqID'] = row[15]
        return result

    def build_order_dict(self, row):
        result = {}
        result['ordQty'] = row[0]
        result['ordDate'] = row[1]
        result['ordExpDate'] = row[2]
        result['ordType'] = row[3]
        result['ordPrice'] = row[4]
        result['suppID'] = row[5]
        result['resName'] = row[6]
        result['resSpecifications'] = row[7]
        return result

    def getAllRequesters(self):
        dao = RequestersDAO()
        requesters_list = dao.getAllRequesters()
        result_list = []
        for row in requesters_list:
            result = self.build_requester_dict(row)
            result_list.append(result)
        return jsonify(Requester=result_list)

    def getRequesterById(self, reqID):
        dao = RequestersDAO()
        row = dao.getRequesterById(reqID)
        if not row:
            return jsonify(Error="Requester not found"), 404
        else:
            requester = self.build_requester_dict(row)
            return jsonify(Requester=requester)

    def insertRequester(self, form):
        if len(form) != 1:
            return jsonify(Error = "Malformed post request"), 400
        else:
            uid = form['uid']
            row = UsersDAO.getUserById(uid)
            if not row:
                return jsonify(Error="User not found"), 404
            else:
                if uid:
                    dao = RequestersDAO()
                    reqid = dao.insert(uid)
                    result = self.build_requester_attributes(reqid, uid)    #A~adir buil attributes
                    return jsonify(Admin=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in post request"), 400

    def searchRequesters(self, args):
        pass

    def getOrdersByRequesterId(self, reqID):
        dao = RequestersDAO()
        orders_list = dao.getOrdersByRequesterId(reqID)
        result_list = []
        for row in orders_list:
            result = self.build_order_dict(row)
            result_list.append(result)
        return jsonify(Orders=result_list)

