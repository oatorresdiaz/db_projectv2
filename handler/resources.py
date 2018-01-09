from flask import jsonify
from dao.resources import ResourcesDAO

class ResourcesHandler:
    def build_resource_dict(self, row):
        result = {}
        result['resID'] = row[0]
        result['resCategory'] = row[1]
        result['resSubCategory'] = row[2]
        return result

    def getAllResources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllResources()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourceById(self, resID):
        dao = ResourcesDAO()
        row = dao.getResourceById(resID)
        if not row:
            return jsonify(Error="Resource not found"), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource=resource)

    def getAllAvailableResources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllAvailableResources()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(AvailableResources = result_list)

    def searchResources(self, args):
        pass