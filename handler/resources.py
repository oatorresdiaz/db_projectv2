from flask import jsonify
from dao.resources import ResourcesDAO

class ResourcesHandler:
    def build_resource_dict(self, row):
        result = {}
        result['resID'] = row[0]
        result['resName'] = row[1]
        result['catID'] = row[2]
        result['resSpecifications'] = row[3]
        result['resName'] = row[1]
        result['catID']=row[2]
        result['resSpecifications'] = row[3]
        return result

    def build_cat_dict(self, row):
        result = {}
        result['resName'] = row[0]
        result['resSpecifications'] = row[1]
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

    def getResourcesByCity(self, city):
        dao = ResourcesDAO()
        resources_list = dao.getResourcesByCity(city)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getAllAvailableResources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllAvailableResources()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(AvailableResources = result_list)

    def getResourcesByCategories(self, catName):
        dao = ResourcesDAO()
        resources_list = dao.getResourcesByCategories(catName)
        result_list = []
        for row in resources_list:
            result = self.build_cat_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)

    def getAvailableResourcesByCategories(self, catName):
        dao = ResourcesDAO()
        resources_list = dao.getAvailableResourcesByCategories(catName)
        result_list = []
        for row in resources_list:
            result = self.build_cat_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def searchResources(self, args):
        pass
