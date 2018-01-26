from flask import Flask, jsonify, request
from handler.users import UsersHandler
from handler.admins import AdminsHandler
from handler.suppliers import SuppliersHandler
from handler.requesters import RequestersHandler
from handler.resources import ResourcesHandler
from handler.inventory import InventoryHandler
from handler.requests import RequestsHandler
from handler.addresses import AddressesHandler
from handler.credentials import CredentialsHandler
from handler.orders import OrdersHandler
from handler.telephonenumbers import TelephoneNumbersHandler
from handler.pricehistory import PriceHistoryHandler
from handler.creditcards import CreditCardsHandler

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App!'


@app.route('/db_project/users', methods=['GET', 'POST'])
def getAllUsers():
    if request.method == 'POST':
        return UsersHandler().insertUser(request.form)
    else:
        if not request.args:
            return UsersHandler().getAllUsers()
        else:
            return UsersHandler().searchUsersByArguments(request.args)


@app.route('/db_project/users/<int:uID>', methods=['GET', 'PUT'])
def getUserById(uID):
    if request.method == 'GET':
        return UsersHandler().getUserById(uID)
    elif request.method == 'PUT':
        return UsersHandler().updateUser(uID, request.form)
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/db_project/addresses', methods=['GET', 'POST'])
def getAllAddresses():
    if request.method == 'POST':
        return AddressesHandler().insertAddress(request.form)
    else:
        if not request.args:
            return AddressesHandler().getAllAddresses()
        else:
            return AddressesHandler().searchAddressesByArguments(request.args)


@app.route('/db_project/addresses/<int:addID>', methods=['GET', 'PUT'])
def getAddressById(addID):
    if request.method == 'GET':
        return AddressesHandler().getAddressById(addID)
    elif request.method == 'PUT':
        return AddressesHandler().updateAddress(addID, request.form)
    else:
        return jsonify(Error="Method not allowed."), 405


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


@app.route('/db_project/admins', methods=['GET', 'POST' ])
def getAllAdmins():
    if request.method == 'POST':
        return AdminsHandler.insertAdmin(request.form)
    else:
        if not request.args:
            return AdminsHandler().getAllAdmins()
        else:
            return AdminsHandler().searchAdminsByArguments(request.args)


@app.route('/db_project/admins/<int:adminID>')
def getAdminById(adminID):
    return AdminsHandler().getAdminById(adminID)


@app.route('/db_project/admins/<int:uID>')
def getAdminByUserId(uID):
    return AdminsHandler().getAdminByUserId(uID)


@app.route('/db_project/suppliers', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        return SuppliersHandler().insertSupplier(request.form)
    else:
        if not request.args:
            return SuppliersHandler().getAllSuppliers()
        else:
            return SuppliersHandler().searchSuppliersByArguments(request.args)


@app.route('/db_project/suppliers/<int:suppID>', methods=['GET', 'PUT'])
def getSupplierById(suppID):
    if request.method == 'GET':
        return SuppliersHandler().getSupplierById(suppID)


@app.route('/db_project/suppliers/<int:suppID>/inventory')
def getInventoryBySupplierId(suppID):
    return SuppliersHandler().getInventoryBySupplierId(suppID)


@app.route('/db_project/suppliers/<int:suppID>/orders')
def getOrdersBySupplierId(suppID):
    return SuppliersHandler().getOrdersBySupplierId(suppID)


@app.route('/db_project/requesters', methods=['GET', 'POST'])
def getAllRequesters():
    if request.method == 'POST':
        return RequestersHandler().insertRequester(request.form)
    else:
        if not request.args:
            return RequestersHandler().getAllRequesters()
        else:
            return RequestersHandler().searchRequestersByArguments(request.args)


@app.route('/db_project/requesters/<int:reqID>')
def getRequesterById(reqID):
    return RequestersHandler().getRequesterById(reqID)


@app.route('/db_project/resources')
def getAllResources():
    if not request.args:
        return ResourcesHandler().getAllResources()
    else:
        return ResourcesHandler().searchResourcesByArguments(request.args)


@app.route('/db_project/requesters/<int:reqID>/orders')
def getOrdersByRequesterId(reqID):
    return RequestersHandler().getOrdersByRequesterId(reqID)


@app.route('/db_project/resources/<int:resID>')
def getResourceById(resID):
    return ResourcesHandler().getResourceById(resID)


@app.route('/db_project/resources/<string:city>')
def getResourcesByCity(city):
    return ResourcesHandler().getResourcesByCity(city)


@app.route('/db_project/inventory')
def getAllInventory():
    if not request.args:
        return InventoryHandler().getAllInventory()
    else:
        return InventoryHandler().searchInventoryByArguments(request.args)


@app.route('/db_project/inventory/<int:invID>')
def getInventoryById(invID):
    return InventoryHandler().getInventoryById(invID)


@app.route('/db_project/inventory/<int:invID>/suppliers')
def getSupplierByInventoryId(invID):
    return InventoryHandler().getSupplierByInventoryId(invID)


@app.route('/db_project/inventory/maxPrice')
def getMaxPriceInInventory():
    return InventoryHandler().getMaxPriceInInventory()


@app.route('/db_project/inventory/minPrice')
def getMinPriceInInventory():
    return InventoryHandler().getMinPriceInInventory()


@app.route('/db_project/inventory/free')
def getFreeInInventory():
    return InventoryHandler().getFreeInInventory()


@app.route('/db_project/resources/<string:resName>/suppliers')
def getSuppliersByResourceName(resName):
    return InventoryHandler().getSuppliersByResourceName(resName)


@app.route('/db_project/requests', methods=['GET', 'POST'])
def getAllRequests():
    if request.method == 'POST':
        return RequestsHandler().insertRequest(request.form)
    else:
        if not request.args:
            return RequestsHandler().getAllRequests()
        else:
            return RequestsHandler().searchRequestsByArguments(request.args)


@app.route('/db_project/orders')
def getAllOrders():
    if not request.args:
        return OrdersHandler().getAllOrders()
    else:
        return OrdersHandler().searchOrdersByArguments(request.args)


@app.route('/db_project/resources/available')
def getAllAvailableResources():
    if not request.args:
        return ResourcesHandler().getAllAvailableResources()
    else:
        return ResourcesHandler().searchResourcesByArguments(request.args)


@app.route('/db_project/categories/<string:catName>/resources')
def getResourcesByCategoryName(catName):
    return ResourcesHandler().getResourcesByCategoryName(catName)


@app.route('/db_project/categories/<string:catName>/resources/available')
def getAvailableResourcesByCategories(catName):
    return ResourcesHandler().getAvailableResourcesByCategories(catName)


@app.route('/db_project/telephoneNumbers')
def getAllTelephoneNumbers():
    if not request.args:
        return TelephoneNumbersHandler().getAllTelephoneNumbers()
    else:
        return TelephoneNumbersHandler().searchUsers(request.args)


@app.route('/db_project/telephoneNumbers/<int:tID>')
def getTelephoneNumberById(tID):
    return TelephoneNumbersHandler().getTelephoneNumberById(tID)


@app.route('/db_project/telephoneNumbers/users/<int:uID>')
def getTelephoneNumberByUserId(uID):
    return TelephoneNumbersHandler().getTelephoneNumberByUserId(uID)


@app.route('/db_project/priceHistory')
def getAllPriceHistory():
    return PriceHistoryHandler.getAllPriceHistory()


@app.route('/db_project/priceHistory/<int:phID>')
def getPriceHistoryById(phID):
    return PriceHistoryHandler().getPriceHistoryById(phID)

@app.route('/db_project/priceHistory/inventory/<int:invID>')
def getPriceHistoryByUserId(invID):
    return PriceHistoryHandler().getPriceHistoryByInventoryId(invID)

@app.route('/db_project/creditcards', methods=['GET', 'POST'])
def getAllCreditCards():
    if request.method == 'POST':
        return CreditCardsHandler().insertCreditCard(request.form)
    else:
        return CreditCardsHandler().getAllCreditCards()


@app.route('/db_project/creditcards/<int:uID>', methods=['GET', 'PUT'])
def getCreditCardsByUserId(uID):
    if request.method == 'GET':
        return CreditCardsHandler().getCreditCardsByUserId(uID)
    elif request.method == 'PUT':
        return CreditCardsHandler().updateCreditCard(uID, request.form)
    else:
        return jsonify(Error="Method not allowed."), 405


#TODO: FOR PHASE 3
@app.route('/db_project/login')
def login():
     print("Welcome to the user program")
     uname = input("Enter username: ")
     print("Value entered: " + str(uname))
     upasswd = input("Enter password: ")
     print("Value entered: " + str(upasswd))
     if not request.args:
         return CredentialsHandler().login(uname, upasswd)
     else:
         return CredentialsHandler().searchCredentials(request.args)


if __name__ == '__main__':
    app.run()
