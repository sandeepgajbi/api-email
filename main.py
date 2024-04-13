import requests
from send_email import send_email
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define the API URL and key
url = "https://newsapi.org/v2/top-headlines"
api_key = "bfdf1e2b220c4abc92c40d5b21325482"

# Define email parameters
recipient_email = "sandeepgajbi@gmail.com"
subject = "TechCrunch Top Headlines"

try:
    # Make API request
    params = {"sources": "techcrunch", "apiKey": api_key}
    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise exception for HTTP errors
    content = response.json()

    # Extract news articles
    news = ""
    for article in content["articles"]:
        title = article["title"].split("|")[0]
        description = article["description"]
        news += f"Title: {title}\nDescription: {description}\n\n"

    # Send email
    send_email(recipient_email, subject, news)
    logging.info("Email sent successfully")

except Exception as e:
    logging.error(f"An error occurred: {e}")
