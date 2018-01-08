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
