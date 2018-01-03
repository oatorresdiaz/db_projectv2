from flask import jsonify
from dao.requests import RequestsDAO

class RequestsHandler:
    def build_request_dict(self, row):
        result = {}
        result['reqID'] = row[0]
        result['resID'] = row[1]
        result['rqstsDate'] = row[2]
        result['rqstsQty'] = row[3]
        return result

    def getAllRequests(self):
        dao = RequestsDAO()
        requests_list = dao.getAllRequests()
        result_list = []
        for row in requests_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def searchRequests(self, args):
        pass