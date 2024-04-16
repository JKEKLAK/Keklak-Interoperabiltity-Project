#Jared Keklak INFO 762 Dr.Walters API Project

import requests

#this method makes a call to the cat classifier API, and returns a json object which lists all possible breeds the cat could be
#the values returned range from 0 to 1, one being most accurate match
def classify_cat(image_url: str, api_key: str):
    url = "https://zylalabs.com/api/499/cat+breed+classification+api/373/pet+classification?url=https://i.guim.co.uk/img/media/c9b0aad22638133aa06cd68347bed2390b555e63/0_477_2945_1767/master/2945.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=97bf92d90f51da7067d00f8156512925"
    headers = {
        'Authorization': api_key
    }
    response = requests.request("POST", url, headers=headers, data=image_url)
    return response.txt