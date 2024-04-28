import requests

BASE = "http://127.0.0.1:5000/"
APP_VERSION = "v1/"

def put():
    data = [{"name": "", 'image_url': "https://api-ninjas.com/images/cats/abyssinian.jpg", 'youtube': "youtube video", 'facts': "facts"},
            {"name": "", 'image_url': "https://cdn2.thecatapi.com/images/MTgzMDYxNw.jpg", 'youtube': "youtube video", 'facts': "facts"},
            {"name": "", 'image_url': "https://cdn2.thecatapi.com/images/L-aDi29wP.jpg", 'youtube': "youtube video", 'facts': "facts"},
            {"name": "", 'image_url': "https://cdn2.thecatapi.com/images/4G_bcp35K.jpg", 'youtube': "youtube video", 'facts': "facts"}]

    for i in range(len(data)):
        r = BASE + APP_VERSION + "cat/" + str(i)
        response = requests.put(BASE + APP_VERSION + "cat/" + str(i), data[i])
        print(response.json())

#input()
#response = requests.get(BASE + APP_VERSION + "cat/2") #test get
#print(response.json())


def put_new(image_url: str, number: int):
    data = [{'name': "", 'image_url': image_url, 'youtube': "", 'facts': ""}]
    r = BASE + APP_VERSION + "cat/4"
    response = requests.put(BASE + APP_VERSION + "cat/" + str(number), data[0])
    print(response.json())
