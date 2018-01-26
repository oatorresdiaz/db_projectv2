from flask import jsonify
from dao.categories import CategoriesDAO


class CategoriesHandler:
    def build_categories_dict(self, row):
        result = {}
        result['catID'] = row[0]
        result['catName'] = row[1]
        return result

    def build_categories_attributes(self, catID, catName):
        result = {}
        result['catID'] = catID
        result['catName'] = catName
        return result

    def getAllCategories(self):
        dao = CategoriesDAO()
        categories_list = dao.getAllCategories()
        result_list = []
        for row in categories_list:
            result = self.build_categories_dict(row)
            result_list.append(result)
        return jsonify(Categories=result_list)

    def getCategoriesbyId(self, catID):
        dao = CategoriesDAO()
        row = dao.getCategoriesById(catID)
        if not row:
            return jsonify(Error="Category not found"), 404
        else:
            category = self.build_categories_dict(row)
            return jsonify(Category=category)

    def insertCategories(self, form):
        if len(form) != 1:
            return jsonify(Error="Malformed post request"), 400
        else:
          catName = form['catName']

            if catName:
                catDao = CategoriesDAO()
                catID = catDao.insert(catName)

                result = self.build_categories_attributes(catID, catName)
                return jsonify(Categories=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

