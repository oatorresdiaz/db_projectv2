from flask import jsonify
from dao.inventory import InventoryDAO

class InventoryHandler:
    def build_inventory_dict(self, row):
        result = {}
        result['invID'] = row[0]
        result['suppID'] = row[1]
        result['invDate'] = row[2]
        result['invQty'] = row[3]
        result['invReserved'] = row[4]
        result['invAvailable'] = row[5]
        result['invPrice'] = row[6]
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
