#transforming and cleaning the news data
from datetime import datetime
# from extract import extract_news

# my_articles = extract_news()

def transform_news(articles):
    cleaned_data = []

    for article in articles:
        cleaned_data.append(
            {
                "source" : article.get("source", {}).get('name'),
                "author": article.get("author"),
                "title": article.get("title"),
                "published_at": article.get("publishedAt"),
                "inserted _at": datetime.now()

            }
        )
    return cleaned_data
# print(my_articles)
