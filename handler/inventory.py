from flask import jsonify
from dao.inventory import InventoryDAO

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
        result['catName'] = row[10]
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
        pass

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
