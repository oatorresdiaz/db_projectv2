from flask import jsonify
from dao.requests import RequestsDAO

class RequestsHandler:
    def build_request_dict(self, row):
        result = {}
        result['resID'] = row[0]
        result['reqID'] = row[1]
        result['reqQty'] = row[2]
        result['reqUnit'] = row[3]
        result['reqDate'] = row[4]
        result['resName'] = row[5]
        result['catID'] = row[6]
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