from flask import jsonify
from dao.credentials import CredentialsDAO

class CredentialsHandler:
    def build_credential_dict(self, row):
        result = {}
        result['cID'] = row[0]
        result['uID'] = row[1]
        result['username'] = row[2]
        result['password'] = row[3]
        result['email'] = row[4]
        return result

    def getAllCredentials(self):
        dao = CredentialsDAO()
        credentials_list = dao.getAllCredentials()
        result_list = []
        for row in credentials_list:
            result = self.build_credential_dict(row)
            result_list.append(result)
        return jsonify(Credentials=result_list)

    def getCredentialById(self, cID):
        dao = CredentialsDAO()
        row = dao.getCredentialById(cID)
        if not row:
            return jsonify(Error="Credential not found"), 404
        else:
            credential = self.build_credential_dict(row)
            return jsonify(Credential=credential)

    def login(self,uname, passwd):
        dao = CredentialsDAO()
        verification = dao.login(uname, passwd)
        if verification == "false":
            return jsonify(Error="Login Failed")
        else:
            return jsonify(Credentials="Login Successful")