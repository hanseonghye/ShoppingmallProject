from rest_framework.utils import json


class Member:
    def __init__(self, name, id, password="", email=None, phone_number=None):
        self.name = name
        self.id = id
        self.password = password
        self.email = email
        self.phone_number = phone_number

    @staticmethod
    def check_id(checkId):
        return True

    def is_valid(self):
        return self.name and self.id and self.password

    def __str__(self):
        print(f'{self.name}, {self.id}, {self.password}')

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


class Cart:
    def __init__(self, member_no, product_no, product_detail_no, amount):
        self.member_no = member_no
        self.product_no = product_no
        self.product_detail_no = product_detail_no
        self.amount = amount

    def __iter__(self):
        return iter([('member_no', self.member_no), ('product_no', self.product_no),
                     ('product_detail_no', self.product_detail_no), ('amount', self.amount)])
