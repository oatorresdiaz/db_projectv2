from flask import jsonify
from dao.addresses import AddressesDAO

class AddressesHandler:
    def build_address_dict(self, row):
        result = {}
        result['addID'] = row[0]
        result['uID'] = row[1]
        result['City'] = row[2]
        result['Street'] = row[3]
        result['Country'] = row[4]
        result['ZipCode'] = row[5]
        return result

    def getAllAddresses(self):
        dao = AddressesDAO()
        addresses_list = dao.getAllAddresses()
        result_list = []
        for row in addresses_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Addresses=result_list)

    def getAddressById(self, addID):
        dao = AddressesDAO()
        row = dao.getAddressById(addID)
        if not row:
            return jsonify(Error="Address not found"), 404
        else:
            address = self.build_address_dict(row)
            return jsonify(Address=address)
