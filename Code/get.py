import requests

BASE = " http://127.0.0.1:5000/"
APP_VERSION = "v1/"


def get_(cat_id: int):

    response = requests.get(BASE + APP_VERSION + "cat/" + str(cat_id))
    return (response.json())

