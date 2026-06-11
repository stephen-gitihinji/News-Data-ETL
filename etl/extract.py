#extracting data from the news api site and 
import requests as req
from config import NEWS_API_KEY

def extract_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={NEWS_API_KEY}"

    response = req.get(url)
    response.raise_for_status

    data = response.json()
    articles = data.get("articles", [])
    return articles

#print(type(extract_news()))
