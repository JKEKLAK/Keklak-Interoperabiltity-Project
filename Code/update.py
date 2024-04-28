import requests

BASE = " http://127.0.0.1:5000/"
APP_VERSION = "v1/"


def update_(cat_id: int, attribute: str, contents: str):
    try:
        response = requests.patch(BASE + APP_VERSION + "cat/" + str(cat_id), {attribute: contents})
        print("value in DB updated successfully")
    except:
        print("Something went wrong. I dont know what because im just a program. Use the Debugger to find out")


