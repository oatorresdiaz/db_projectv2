from flask import Flask, jsonify, request
from handler.users import UsersHandler
from handler.admins import AdminsHandler
from handler.suppliers import SuppliersHandler
from handler.requesters import RequestersHandler
from handler.resources import ResourcesHandler
from handler.inventory import InventoryHandler
from handler.reserves import ReservesHandler
from handler.requests import RequestsHandler

app = Flask(__name__)

@app.route('/')
def greeting():
    return 'Hello, this is the parts DB App!'

@app.route('/db_project/users')
def getAllUsers():
    if not request.args:
        return UsersHandler().getAllUsers()
    else:
        return UsersHandler().searchUsersByArguments(request.args)
        #return UsersHandler().searchUsers(request.args)

@app.route('/db_project/users/<int:uID>')
def getUserById(uID):
    return UsersHandler().getUserById(uID)

@app.route('/db_project/admins')
def getAllAdmins():
    if not request.args:
        return AdminsHandler().getAllAdmins()
    else:
        return AdminsHandler().searchAdmins(request.args)

@app.route('/db_project/admins/<int:adminID>')
def getAdminById(adminID):
    return AdminsHandler().getAdminById(adminID)

@app.route('/db_project/suppliers')
def getAllSuppliers():
    if not request.args:
        return SuppliersHandler().getAllSuppliers()
    else:
        return SuppliersHandler().searchSuppliers(request.args)

@app.route('/db_project/suppliers/<int:suppID>')
def getSupplierById(suppID):
    return SuppliersHandler().getSupplierById(suppID)

@app.route('/db_project/suppliers/<int:suppID>/inventory') #Encontrar productos de un suplidor
def getSupplierInventory(suppID):
    return SuppliersHandler().getSupplierInventory(suppID)

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

@app.route('/db_project/inventory/<int:invID>/suppliers') #Encontrar suplidores para un producto dado
def getResourceSuppliers(invID):
    return ResourcesHandler().getResourceSuppliers(invID)

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

if __name__ == '__main__':
    app.run()