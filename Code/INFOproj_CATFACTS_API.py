#Jared Keklak INFO 762 Dr.Walters API Project

import requests
import INFOproj_GLOBALS as G

#this method makes a call to the cat facts API and provides facts about the cat specified by name
#it returns a json object with various facts
def get_cat_facts(cat_name: str):

    url = "https://zylalabs.com/api/3561/cat+information+api/3922/get+data?name=" + cat_name
    headers = {
        'Authorization': 'Bearer ' + G.API_KEY_CatFacts
    }
    response = requests.request("GET", url, headers=headers)
    r = response.json()[0]
    #print(response.json()[0])
    facts = "Name: " + r['name'] + "\n" + "Origin: " + r['origin']  + "\n" + "Length: " + str(r['length']) + "\n" + "Weight Range (lbs): " + str(r['min_weight']) +\
            ' - ' + str(r['max_weight']) + "\n" + "Max life expectancy (years): " + str(r['max_life_expectancy']) + "\n" + "Image URL: " + r['image_link']

    return facts

def get_cat_facts_test():
    print("get cat facts was triggered")

#print(get_cat_facts("Burmese", G.API_KEY_CatFacts))