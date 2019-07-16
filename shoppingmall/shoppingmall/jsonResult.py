from rest_framework.utils import json


class JsonResult:
    def __init__(self, result=None, message=None, data={}):
        self.result = result  # success or fail
        self.message = message
        self.data = data

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
