from flask import jsonify
from dao.requests import RequestsDAO
from dao.resources import ResourcesDAO

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

    def build_request_attributes(self, resID, reqID, reqQty, reqUnit, reqDate, resName, catID):
        result = {}
        result['resID'] = resID
        result['reqID'] = reqID
        result['reqQty'] = reqQty
        result['reqUnit'] = reqUnit
        result['reqDate'] = reqDate
        result['resName'] = resName
        result['catID'] = catID
        return result

    def getAllRequests(self):
        dao = RequestsDAO()
        requests_list = dao.getAllRequests()
        result_list = []
        for row in requests_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def searchRequestsByArguments(self, args):
        dao = RequestsDAO()
        if not 'orderby' in args:
            requests_list = dao.searchRequestsByArguments(args)
        elif (len(args) == 1) and 'orderby' in args:
            requests_list = dao.searchRequestsWithSorting(args.get('orderby'))
        else:
            requests_list = dao.searchRequestsByArgumentsWithSorting(args)
        result_list = []
        for row in requests_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def insertRequest(self, form):
        if len(form) != 7:
            return jsonify(Error="Malformed post request"), 400
        else:
            resName = form['resName']
            catID = form['catID']
            resSpecifications = form['resSpecifications']
            reqID = form['reqID']
            reqQty = form['reqQty']
            reqUnit = form['reqUnit']
            reqDate = form['reqDate']
            if resName and catID and resSpecifications and reqID and reqQty and reqUnit and reqDate:
                requestsDao = RequestsDAO()
                resourcesDao = ResourcesDAO()
                resID = resourcesDao.insert(resName, catID, resSpecifications)
                requestsDao.insert(reqID, resID, reqQty, reqUnit, reqDate)
                result = self.build_request_attributes(resID, reqID, reqQty, reqUnit, reqDate, resName, catID)
                return jsonify(Request=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400


