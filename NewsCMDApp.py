import requests
import json
type=input("Type of news you want to watch - ")
a=requests.get(f"https://newsapi.org/v2/everything?q={type}&apiKey=b6ab3529cb5f417b90ca694ae98f6fff")
jsonn=json.loads(a.text)
i=0
for article in jsonn["articles"]:
    i=i+1
    print(str(i)+ " "+ article["title"])
    print("\n")
    print(article["description"])
    print("\n")
    print("**************************************")
    print("\n")
