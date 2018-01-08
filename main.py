from flask import Flask, jsonify, request
from handler.users import UsersHandler
from handler.admins import AdminsHandler
from handler.suppliers import SuppliersHandler
from handler.requesters import RequestersHandler
from handler.resources import ResourcesHandler
from handler.inventory import InventoryHandler
from handler.reserves import ReservesHandler
from handler.requests import RequestsHandler
from handler.addresses import AddressesHandler
from handler.batteries import BatteriesHandler
from handler.clothing import ClothingHandler

app = Flask(__name__)


@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App!'


@app.route('/db_project/addresses')
def getAllAddresses():
    if not request.args:
        return AddressesHandler().getAllAddresses()
    else:
        return AddressesHandler().searchAddresses(request.args)


@app.route('/db_project/addresses/<int:addID>')
def getAddressById(addID):
    return AddressesHandler().getAddressById(addID)


@app.route('/db_project/addresses/<int:uID>')
def getAddressByUserId(uID):
    return AddressesHandler().getAddressByUserId(uID)


@app.route('/db_project/addresses/<string:City>')
def getAddressByCity(City):
    return AddressesHandler().getAddressByCity(City)


@app.route('/db_project/addresses/<string:Street>')
def getAddressByStreet(Street):
    return AddressesHandler().getAddressByStreet(Street)


@app.route('/db_project/addresses/<string:Country>')
def getAddressByCountry(Country):
    return AddressesHandler().getAddressByCountry(Country)


@app.route('/db_project/addresses/<int:ZipCode>')
def getAddressByZipCode(ZipCode):
    return AddressesHandler().getAddressByZipCode(ZipCode)


@app.route('/db_project/admins')
def getAllAdmins():
    if not request.args:
        return AdminsHandler().getAllAdmins()
    else:
        return AdminsHandler().searchAdmins(request.args)


@app.route('/db_project/admins/<int:adminID>')
def getAdminById(adminID):
    return AdminsHandler().getAdminById(adminID)


@app.route('/db_project/admins/<int:uID>')
def getAdminByUserId(uID):
    return AdminsHandler().getAdminByUserId(uID)


@app.route('/db_project/batteries')
def getAllBatteries():
    if not request.args:
        return BatteriesHandler().getAllBatteries()
    else:
        return BatteriesHandler().searchBatteries(request.args)


@app.route('/db_project/batteries/<int:bID>')
def getBatteriesById(bID):
    return BatteriesHandler().getBatteryById(bID)


@app.route('/db_project/batteries/<int:resID>')
def getBatteriesByResourceId(resID):
    return BatteriesHandler().getBatteryByResourceId(resID)


@app.route('/db_project/batteries/<int:catID>')
def getBatteriesByCategoryId(catID):
    return BatteriesHandler().getBatteryByCategoryId(catID)


@app.route('/db_project/batteries/<string:bType>')
def getBatteriesByType(bType):
    return BatteriesHandler().getBatteryByType(bType)


@app.route('/db_project/batteries/<string:bBrand>')
def getBatteriesByBrand(bBrand):
    return BatteriesHandler().getBatteryByBrand(bBrand)


@app.route('/db_project/cloth')
def getAllClothing():
    if not request.args:
        return ClothingHandler().getAllClothing()
    else:
        return ClothingHandler().searchClothing(request.args)


@app.route('/db_project/cloth/<int:clothID>')
def getClothingById(clothID):
    return ClothingHandler().getClothingById(clothID)


@app.route('/db_project/cloth/<int:resID>')
def getClothingByResourceId(resID):
    return ClothingHandler().getClothingByResourceId(resID)


@app.route('/db_project/cloth/<int:catID>')
def getClothingByCategoryId(catID):
    return ClothingHandler().getClothingByCategoryId(catID)


@app.route('/db_project/cloth/<string:clothGender>')
def getClothingByGender(clothGender):
    return ClothingHandler().getClothingByGender(clothGender)


@app.route('/db_project/cloth/<string:clothBrand>')
def getClothingByBrand(clothBrand):
    return ClothingHandler().getClothingByBrand(clothBrand)


@app.route('/db_project/cloth/<string:clothSize>')
def getClothingBySize(clothSize):
    return ClothingHandler().getClothingBySize(clothSize)


@app.route('/db_project/cloth/<string:clothColor>')
def getClothingByColor(clothColor):
    return ClothingHandler().getClothingByColor(clothColor)


@app.route('/db_project/cloth/<string:clothDesignPattern>')
def getClothingByDesignPattern(clothDesignPattern):
    return ClothingHandler().getClothingByDesignPattern(clothDesignPattern)

    
@app.route('/db_project/suppliers')
def getAllSuppliers():
    if not request.args:
        return SuppliersHandler().getAllSuppliers()
    else:
        return SuppliersHandler().searchSuppliers(request.args)

@app.route('/db_project/suppliers/<int:suppID>')
def getSupplierById(suppID):
    return SuppliersHandler().getSupplierById(suppID)

@app.route('/db_project/requesters')
def getAllRequesters():
    if not request.args:
        return RequestersHandler().getAllRequesters()
    else:
        return RequestersHandler().searchRequesters(request.args)

@app.route('/db_project/requesters/<int:reqID>')
def getRequesterById(reqID):
    return RequestersHandler().getRequesterById(reqID)

@app.route('/db_project/resources')
def getAllResources():
    if not request.args:
        return ResourcesHandler().getAllResources()
    else:
        return ResourcesHandler().searchResources(request.args)

@app.route('/db_project/resources/<int:resID>')
def getResourceById(resID):
    return ResourcesHandler().getResourceById(resID)

@app.route('/db_project/inventory')
def getAllInventory():
    if not request.args:
        return InventoryHandler().getAllInventory()
    else:
        return InventoryHandler().searchInventory(request.args)

@app.route('/db_project/inventory/<int:invID>')
def getInventoryById(invID):
    return InventoryHandler().getInventoryById(invID)

@app.route('/db_project/reserves')
def getAllReserves():
    if not request.args:
        return ReservesHandler().getAllReserves()
    else:
        return ReservesHandler().searchReserves(request.args)


@app.route('/db_project/requests')
def getAllRequests():
    if not request.args:
        return RequestsHandler().getAllRequests()
    else:
        return RequestsHandler().searchRequests(request.args)


@app.route('/db_project/users')
def getAllUsers():
    if not request.args:
        return UsersHandler().getAllUsers()
    else:
        return UsersHandler().searchUsers(request.args)


@app.route('/db_project/users/<int:uID>')
def getUserById(uID):
    return UsersHandler().getUserById(uID)


if __name__ == '__main__':
    app.run()
