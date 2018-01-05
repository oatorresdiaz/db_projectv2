from flask import jsonify
from dao.requesters import RequestersDAO

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

    def searchRequesters(self, args):
        pass

