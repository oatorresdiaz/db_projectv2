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
from handler.credentials import CredentialsHandler
from handler.orders import OrdersHandler

app = Flask(__name__)

#Base route
@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App!'

#Shows all users
@app.route('/db_project/users')
def getAllUsers():
    if not request.args:
        return UsersHandler().getAllUsers()
    else:
        return UsersHandler().searchUsersByArguments(request.args)
        #return UsersHandler().searchUsers(request.args)

#Shows user by ID
@app.route('/db_project/users/<int:uID>')
def getUserById(uID):
    return UsersHandler().getUserById(uID)



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


#Shows all admins
@app.route('/db_project/admins', methods=['GET', 'POST' ])
def getAllAdmins():
    if request.method == 'POST':
        return AdminsHandler.insertAdmin(request.form)
    else:
        if not request.args:
            return AdminsHandler().getAllAdmins()
        else:
            return AdminsHandler().searchAdmins(request.args)

#Show admin by ID
@app.route('/db_project/admins/<int:adminID>')
def getAdminById(adminID):
    return AdminsHandler().getAdminById(adminID)


@app.route('/db_project/admins/<int:uID>')
def getAdminByUserId(uID):
    return AdminsHandler().getAdminByUserId(uID)


#Show all suppliers
@app.route('/db_project/suppliers', methods=['GET', 'POST' ])
def getAllSuppliers():
    if request.method == 'POST':
        return SuppliersHandler.insertAdmin(request.form)
    else:
        if not request.args:
            return SuppliersHandler().getAllSuppliers()
        else:
            return SuppliersHandler().searchSuppliers(request.args)

#Show supplier by ID
@app.route('/db_project/suppliers/<int:suppID>')
def getSupplierById(suppID):
    return SuppliersHandler().getSupplierById(suppID)

@app.route('/db_project/suppliers/<int:suppID>/inventory') #Encontrar productos de un suplidor
def getInventoryBySupplierId(suppID):
    return SuppliersHandler().getInventoryBySupplierId(suppID)

@app.route('/db_project/suppliers/<int:suppID>/orders')
def getOrdersBySupplierId(suppID):
    return SuppliersHandler().getOrdersBySupplierId(suppID)

#Show all requesters
@app.route('/db_project/requesters', methods=['GET', 'POST' ])
def getAllRequesters():
    if request.method == 'POST':
        return RequestersHandler.insertRequester(request.form)
    else:
        if not request.args:
            return RequestersHandler().getAllRequesters()
        else:
            return RequestersHandler().searchRequesters(request.args)

#Show requester by ID
@app.route('/db_project/requesters/<int:reqID>')
def getRequesterById(reqID):
    return RequestersHandler().getRequesterById(reqID)

#Show all resources
@app.route('/db_project/resources')
def getAllResources():
    if not request.args:
        return ResourcesHandler().getAllResources()
    else:
        return ResourcesHandler().searchResources(request.args)

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
        return InventoryHandler().searchInventory(request.args)

#Show inventory by ID
@app.route('/db_project/inventory/<int:invID>')
def getInventoryById(invID):
    return InventoryHandler().getInventoryById(invID)

@app.route('/db_project/inventory/<int:invID>/suppliers')
def getSupplierByInventoryId(invID):
    return InventoryHandler().getSupplierByInventoryId(invID)

@app.route('/db_project/resources/<string:resName>/suppliers') #Encontrar suplidores para un producto dado
def getSuppliersByResourceName(resName):
    return InventoryHandler().getSuppliersByResourceName(resName)

@app.route('/db_project/requests')
def getAllRequests():
    if not request.args:
        return RequestsHandler().getAllRequests()
    else:
        return RequestsHandler().searchRequests(request.args)

@app.route('/db_project/orders')
def getAllOrders():
    if not request.args:
        return OrdersHandler().getAllOrders()
    else:
        return OrdersHandler().searchOrders(request.args)

@app.route('/db_project/resources/available')
def getAllAvailableResources():
    if not request.args:
        return ResourcesHandler().getAllAvailableResources()
    else:
        return ResourcesHandler().searchResources(request.args)

@app.route('/db_project/categories/<string:catName>/resources')
def getResourcesByCategories(catName):
        return ResourcesHandler().getResourcesByCategories(catName)

@app.route('/db_project/categories/<string:catName>/resources/available')
def getAvailableResourcesByCategories(catName):
        return ResourcesHandler().getAvailableResourcesByCategories(catName)

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
