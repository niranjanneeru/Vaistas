import requests

r = requests.get("https://makeatonapi.herokuapp.com/").json()
for c in r:
    for k in c:
        print(k, c[k])
