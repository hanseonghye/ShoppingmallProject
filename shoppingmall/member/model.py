class Member:
    def __init__(self, name="", id="", password="", email=None):
        self.name = name
        self.id = id
        self.password = password
        self.email = email

    def check_id(self, checkId):
        return True


class Cart:
    def __init__(self, member_no, product_no, product_detail_no, amount):
        self.member_no = member_no
        self.product_no = product_no
        self.product_detail_no = product_detail_no
        self.amount = amount
