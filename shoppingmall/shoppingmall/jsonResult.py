from rest_framework.utils import json


class JsonResult:
    def __init__(self, status="", result="", data={}):
        self.status = status
        self.result = result
        self.data = data

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
