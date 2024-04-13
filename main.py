import requests

url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=bfdf1e2b220c4abc92c40d5b21325482"

api_key = "bfdf1e2b220c4abc92c40d5b21325482"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(f"Title : {article["title"].split("|")[0]}")
    print(f"Description : {article["description"]}")
    print("\n")
