from flask import jsonify
from dao.creditcards import CreditCardsDAO

class CreditCardsHandler:
    def build_creditCard_dict(self, row):
        result = {}
        result['ccID'] = row[0]
        result['uID'] = row[1]
        result['ccNumber'] = row[2]
        result['ccExpDate'] = row[3]
        result['ccSecurityCode'] = row[4]
        return result

    def build_creditCard_attributes(self, ccID, uID, ccNumber, ccExpDate, ccSecurityCode):
        result = {}
        result['ccID'] = ccID
        result['uID'] = uID
        result['ccNumber'] = ccNumber
        result['ccExpDate'] = ccExpDate
        result['ccSecurityCode'] = ccSecurityCode
        return result

    def getAllCreditCards(self):
        dao = CreditCardsDAO()
        creditCards_list = dao.getAllCreditCards()
        result_list = []
        for row in creditCards_list:
            result = self.build_creditCard_dict(row)
            result_list.append(result)
        return jsonify(CreditCards=result_list)

    def getCreditCardbyId(self, ccID):
        dao = CreditCardsDAO()
        row = dao.getCredentialById(ccID)
        if not row:
            return jsonify(Error="Credit Card not found"), 404
        else:
            creditCard = self.build_creditCard_dict(row)
            return jsonify(CreditCard=creditCard)

    def getCreditCardsByUserId(self, uID):
        dao = CreditCardsDAO()
        creditCards_list = dao.getCreditCardsByUserId(uID)
        result_list = []
        for row in creditCards_list:
            result = self.build_creditCard_dict(row)
            result_list.append(result)
        return jsonify(CreditCards=result_list)

    def insertCreditCard(self, form):
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            uID = form['uID']
            ccNumber = form['ccNumber']
            ccExpDate = form['ccExpDate']
            ccSecurityCode = form['ccSecurityCode']
            if uID and ccNumber and ccExpDate and ccSecurityCode:
                dao = CreditCardsDAO()
                ccID = dao.insert(uID, ccNumber, ccExpDate, ccSecurityCode)
                result = self.build_creditCard_attributes(ccID, uID, ccNumber, ccExpDate, ccSecurityCode)
                return jsonify(CreditCard=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def updateCreditCard(self, uID, form):
        dao = CreditCardsDAO()
        if not dao.getCreditCardsByUserId(uID):
            return jsonify(Error="User not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                ccID = form['ccID']
                ccNumber = form['ccNumber']
                ccExpDate = form['ccExpDate']
                ccSecurityCode = form['ccSecurityCode']
                if uID and ccNumber and ccExpDate and ccSecurityCode:
                    ccID = dao.update(ccID, uID, ccNumber, ccExpDate, ccSecurityCode)
                    result = self.build_creditCard_attributes(ccID, uID, ccNumber, ccExpDate, ccSecurityCode)
                    return jsonify(CreditCard=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400


