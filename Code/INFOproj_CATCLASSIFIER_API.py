#Jared Keklak INFO 762 Dr.Walters API Project

import requests
import INFOproj_GLOBALS as G

#this method makes a call to the cat classifier API, and returns a json object which lists all possible breeds the cat could be
#the values returned range from 0 to 1, one being most accurate match
def classify_cat(image_url: str):
    url = "https://zylalabs.com/api/499/cat+breed+classification+api/373/pet+classification?url=" + image_url
    headers = {
        'Authorization': 'Bearer ' + G.API_KEY_CatClassifier
    }
    response = requests.request("POST", url, headers=headers, data=image_url)
    results = response.json()

    max = 0
    name = ""
    for result in results['results']:
        if(max < result['score']):
            max = result['score']
            name = result['label']

    name = name.rstrip(' cat')
    return name

def classify_cat_test():
    print("classify cat was triggered")

#url = "https://cdn2.thecatapi.com/images/4G_bcp35K.jpg"
