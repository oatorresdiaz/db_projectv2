from flask import jsonify
from dao.tools import ToolsDAO

class ToolsHandler:
    def build_tool_dict(self, row):
        result = {}
        result['tID'] = row[0]
        result['resID'] = row[1]
        result['tName'] = row[2]
        result['tType'] = row[3]
        result['tWeight'] = row[4]
        result['tSize'] = row[5]
        return result

    def getAllTools(self):
        dao = ToolsDAO()
        tools_list = dao.getAllTools()
        result_list = []
        for row in tools_list:
            result = self.build_tool_dict(row)
            result_list.append(result)
        return jsonify(Tool=result_list)

    def getToolById(self, tID):
        dao = ToolsDAO()
        row = dao.getToolById(tID)
        if not row:
            return jsonify(Error="Tool not found"), 404
        else:
            tool = self.build_tool_dict(row)
            return jsonify(Tools=tool)