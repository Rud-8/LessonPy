import requests


def requete ():
    web = "https://ipinfo.io/9.9.9.9/json"


    r = requests.get(web)
    response = r.json()
    print(response)

requete()
