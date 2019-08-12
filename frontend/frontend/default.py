import requests

root_url = "http://127.0.0.1:8000/"
api_url = "api/v1/"
headers = {"Content-Type": "application/x-www-form-urlencoded;  charset=utf-8"}

base_data = {
    "shop_name": None,
    "categorys": None
}


def set_base_data():
    global base_data
    if base_data["shop_name"] is None:
        base_data["shop_name"] = "AWESOME SHOP"

    if base_data["categorys"] is None:
        category_response = requests.get(root_url + api_url + "categorys/")
        if category_response.status_code is 200:
            base_data["categorys"] = category_response.json()['data']
