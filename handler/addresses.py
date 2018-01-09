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

    def getAddressByUserId(self, uID):
        dao = AddressesDAO()
        row = dao.getAddressByUserId(uID)
        if not row:
            return jsonify(Error="Address not found"), 404
        else:
            address = self.build_address_dict(row)
            return jsonify(Address=address)

    def getAddressByCity(self, City):
        dao = AddressesDAO()
        row = dao.getAddressByCity(City)
        if not row:
            return jsonify(Error="Address not found"), 404
        else:
            address = self.build_address_dict(row)
            return jsonify(Address=address)

    def getAddressByStreet(self, Street):
        dao = AddressesDAO()
        row = dao.getAddressByStreet(Street)
        if not row:
            return jsonify(Error="Address not found"), 404
        else:
            address = self.build_address_dict(row)
            return jsonify(Address=address)

    def getAddressByCountry(self, Country):
        dao = AddressesDAO()
        row = dao.getAddressByCountry(Country)
        if not row:
            return jsonify(Error="Address not found"), 404
        else:
            address = self.build_address_dict(row)
            return jsonify(Address=address)

    def getAddressByZipCode(self, ZipCode):
        dao = AddressesDAO()
        row = dao.getAddressByZipCode(ZipCode)
        if not row:
            return jsonify(Error="Address not found"), 404
        else:
            address = self.build_address_dict(row)
            return jsonify(Address=address)
