#Jared Keklak INFO 762 Dr.Walters API Project

import requests


#this method makes a call to the cat facts API and provides facts about the cat specified by name
#it returns a json object with various facts
def get_cat_facts(cat_name: str, api_key: str):
    url = "https://zylalabs.com/api/3561/cat+information+api/3922/get+data?name=" + cat_name

    headers = {
        'Authorization': api_key
    }

    response = requests.request("GET", url, headers=headers, data="data")
    return response.txt