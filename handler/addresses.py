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

    def build_address_attributes(self, uID, addID, city, street, country, zipcode):
        result = {}
        result['uID'] = uID
        result['addID'] = addID
        result['city'] = city
        result['street'] = street
        result['country'] = country
        result['zipcode'] = zipcode
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

    def searchAddressesByArguments(self, args):
        dao = AddressesDAO()
        addresses_list = dao.searchAddressesByArguments(args)
        result_list = []
        for row in addresses_list:
            result = self.build_address_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def insertAddress(self, form):
        if len(form) != 5:
            return jsonify(Error="Malformed post request"), 400
        else:
            uID = form['uID']
            city = form['city']
            street = form['street']
            country = form['country']
            zipcode = form['zipcode']
            if uID and city and street and country and zipcode:
                addDao = AddressesDAO()
                addID = addDao.insert(uID, city, street, country, zipcode)
                result = self.build_address_attributes(uID, addID, city, street, country, zipcode)
                return jsonify(Address=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateAddress(self, addID, form):
        dao = AddressesDAO()
        if not dao.getAddressById(addID):
            return jsonify(Error="User not found."), 404
        else:
            if len(form) != 5:
                return jsonify(Error="Malformed update request"), 400
            else:
                print("HEEEYYY YOOUUUU GUUUYYYYS!!!")
                uID = form['uID']
                city = form['city']
                street = form['street']
                country = form['country']
                zipcode = form['zipcode']
                if city and street and country and zipcode:
                    dao.update(addID, uID, city, street, country, zipcode)
                    result = self.build_address_attributes(uID, addID, city, street, country, zipcode)
                    return jsonify(Address=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400
