import requests
import json
apiKey="2e41bca3-12dd-4059-b522-280767a21908"
url="https://eventregistry.org/api/v1/article/getArticles"
params={"apiKey":apiKey,"keyword":"technology","articleCount": 5,"dataType": "news"}
r=requests.get(url,params=params)
data=r.json() #json bhi python dictionry ki tarah hota hai lekin python dictionary nhi hoti just text hota hai toh json.load usko python dict me convert kar deta hai 
for article in data["articles"]["results"]:
    print(article["title"])
    print(article["body"])
    print("-------------")
#data =r.json()
#print(json.dumps(data,indent=2))
input("")