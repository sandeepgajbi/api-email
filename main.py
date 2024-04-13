import requests
from send_email import send_email

url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=bfdf1e2b220c4abc92c40d5b21325482"

api_key = "bfdf1e2b220c4abc92c40d5b21325482"

request = requests.get(url)
content = request.json()
news = ""

for article in content["articles"]:
    news = f"Title : {article["title"].split("|")[0]} \nDescription : {article["description"]}" + "\n" + "\n" + news

# send news to email
send_email(news)
