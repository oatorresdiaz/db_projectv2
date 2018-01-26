from flask import jsonify
from dao.inventory import InventoryDAO
from dao.categories import CategoriesDAO
from dao.resources import ResourcesDAO
from dao.suppliers import SuppliersDAO

class InventoryHandler:
    def build_inventory_dict(self, row):
        result = {}
        result['catID'] = row[0]
        result['resID'] = row[1]
        result['invID'] = row[2]
        result['suppID'] = row[3]
        result['invDate'] = row[4]
        result['invQty'] = row[5]
        result['invReserved'] = row[6]
        result['invAvailable'] = row[7]
        result['invPrice'] = row[8]
        result['resName'] = row[9]
        result['resspecifications'] = row[10]
        result['catName'] = row[11]
        return result

    def build_supplier_dict(self, row):
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
        result['cID'] = row[10]
        result['username'] = row[11]
        result['password'] = row[12]
        result['email'] = row[13]
        result['tID'] = row[14]
        result['homeNumber'] = row[15]
        result['mobileNumber'] = row[16]
        result['workNumber'] = row[17]
        result['otherNumber'] = row[18]
        result['suppID'] = row[19]
        return result

    def build_inventory_attributes(self, catID, resID, invID, suppID, invDate, invQty, invReserved, invAvailable, invPrice,
                                   resName, resspecifications, catName):
        result = {}
        result['catID'] = catID
        result['resID'] = resID
        result['invID'] = invID
        result['suppID'] = suppID
        result['invDate'] = invDate
        result['invQty'] = invQty
        result['invReserved'] = invReserved
        result['invAvailable'] = invAvailable
        result['invPrice'] = invPrice
        result['resName'] = resName
        result['resspecifications'] = resspecifications
        result['catName'] = catName
        return result

    def getAllInventory(self):
        dao = InventoryDAO()
        inventory_list = dao.getAllInventory()
        result_list = []
        for row in inventory_list:
            result = self.build_inventory_dict(row)
            result_list.append(result)
        return jsonify(Inventory=result_list)

    def getInventoryById(self, invID):
        dao = InventoryDAO()
        row = dao.getInventoryById(invID)
        if not row:
            return jsonify(Error="Inventory not found"), 404
        else:
            inventory = self.build_inventory_dict(row)
            return jsonify(Inventory=inventory)

    def searchInventory(self, args):
        resname = args.get('resName')
        city = args.get('city')
        dao = InventoryDAO()
        inventory_list = []
        if (len(args) == 2) and resname and city:
            inventory_list = dao.getInventoryByResourceNameAndCity(resname, city)
        elif (len(args) == 1) and resname:
            inventory_list = dao.getInventoryByResourceName(resname)
        elif (len(args) == 1) and city:
            inventory_list = dao.getInventoryByCity(city)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in inventory_list:
            result = self.build_inventory_dict(row)
            result_list.append(result)
        return jsonify(Inventory=result_list)

    def getSupplierByInventoryId(self, invID):
        dao = InventoryDAO()
        row = dao.getSupplierByInventoryId(invID)
        if not row:
            return jsonify(Error="Supplier not found"), 404
        else:
            supplier = self.build_supplier_dict(row)
            return jsonify(Supplier=supplier)

    def getSuppliersByResourceName(self, resName):
        dao = InventoryDAO()
        row = dao.getSuppliersByResourceName(resName)
        if not row:
            return jsonify(Error="Supplier not found"), 404
        else:
            supplier = self.build_supplier_dict(row)
            return jsonify(Supplier=supplier)

    def searchInventoryByArguments(self, args):
        dao = InventoryDAO()
        if not 'orderby' in args:
            users_list = dao.searchInventoryByArguments(args)
        elif (len(args) == 1) and 'orderby' in args:
            users_list = dao.searchInventoryWithSorting(args.get('orderby'))
        else:
            users_list = dao.searchInventoryByArgumentsWithSorting(args)
        result_list = []
        for row in users_list:
            result = self.build_inventory_dict(row)
            result_list.append(result)
        return jsonify(Inventory=result_list)


    def getMaxPriceInInventory(self):
        dao = InventoryDAO()
        maxPriceInInventory = dao.getMaxPriceInInventory()
        result_list = []
        result = self.build_inventory_dict(maxPriceInInventory)
        result_list.append(result)
        return jsonify(Inventory=result_list)

    # def getMaxPriceInInventory(self):
    #        dao = InventoryDAO()
    #        maxPriceInInventory = dao.getMaxPriceInInventory()
    #        result_list = []
    #        for row in maxPriceInInventory:
    #            result = self.build_inventory_dict(row)
    #            result_list.append(result)
    #        return jsonify(Inventory=result_list)


    def getMinPriceInInventory(self):
        dao = InventoryDAO()
        minPriceInInventory = dao.getMinPriceInInventory()
        result_list = []
        result = self.build_inventory_dict(minPriceInInventory)
        result_list.append(result)
        return jsonify(Inventory=result_list)


    # def getMinPriceInInventory(self):
    #     dao = InventoryDAO()
    #     minPriceInInventory = dao.getMinPriceInInventory()
    #     result_list = []
    #     for row in minPriceInInventory:
    #         result = self.build_inventory_dict(row)
    #         result_list.append(result)
    #     return jsonify(Inventory=result_list)


    def getFreeInInventory(self):
        dao = InventoryDAO()
        freeInInventory = dao.getFreeInInventory()
        result_list = []
        result = self.build_inventory_dict(freeInInventory)
        result_list.append(result)
        return jsonify(Inventory=result_list)

    # def getFreeInInventory(self):
    #     dao = InventoryDAO()
    #     freeInInventory = dao.getFreeInInventory()
    #     result_list = []
    #     for row in freeInInventory:
    #         result = self.build_inventory_dict(row)
    #         result_list.append(result)
    #     return jsonify(Inventory=result_list)


    def insertInventory(self, form):
        if len(form) != 9:
            return jsonify(Error="Malformed post request"), 400
        else:
            invDate = form['invDate']
            invQty = form['invQty']
            invReserved = form['invReserved']
            invAvailable = form['invAvailable']
            invPrice = form['invPrice']
            resName = form['resName']
            resspecifications = form['resspecifications']
            catName = form['catName']
            uID = form['uID']

            if invDate and invQty and invReserved and invAvailable and invPrice and resName and resspecifications and catName and uID:
                catDao = CategoriesDAO()
                catID = catDao.insert(catName)

                resDao = ResourcesDAO()
                resID = resDao.insert(resName, catID, resspecifications)

                suppDao = SuppliersDAO()
                suppID = suppDao.insert(uID)

                invDao = InventoryDAO()
                invID = invDao.insert(suppID, invDate, invQty, invReserved, invAvailable, invPrice)

                result = self.build_inventory_attributes(catID, resID, invID, suppID, invDate, invQty, invReserved, invAvailable, invPrice, resName, resspecifications, catName)
                return jsonify(Inventory=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateInventory(self, invID, form):
        invDao = InventoryDAO()
        catDao = CategoriesDAO()
        resDao = ResourcesDAO()
        suppDao = SuppliersDAO()
        if not invDao.getInventoryById(invID):
            return jsonify(Error="Inventory not found."), 404
        else:
            if len(form) != 8:
                return jsonify(Error="Malformed update request"), 400
            else:
                invDate = form['invDate']
                invQty = form['invQty']
                invReserved = form['invReserved']
                invAvailable = form['invAvailable']
                invPrice = form['invPrice']
                resName = form['resName']
                resspecifications = form['resspecifications']
                catName = form['catName']

                if invDate and invQty and invReserved and invAvailable and invPrice and resName and resspecifications and catName:
                    catID = catDao.getCategoryByInventoryId(invID)
                    resID = resDao.getResourcesByInventoryId(invID)
                    suppID = suppDao.getSupplierByInventoryId(invID)

                    result = self.build_inventory_attributes(catID, resID, invID, suppID, invDate, invQty, invReserved, invAvailable, invPrice, resName, resspecifications, catName)
                    return jsonify(Inventory=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400