from rest_framework.utils import json


class JsonResult:

    def __init__(self):
        self.result = None  # success or fail
        self.message = None
        self.data = {}

    def success(self, data=None):
        self.result = "success"
        self.data = data

    def fail(self, message=None):
        self.result = "fail"
        self.message = message

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
