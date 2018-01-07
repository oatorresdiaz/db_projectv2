from flask import jsonify
from dao.requesters import RequestersDAO
from dao.users import UsersDAO

class RequestersHandler:
    def build_requester_dict(self, row):
        result = {}
        result['reqID'] = row[0]
        result['uID'] = row[1]
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

