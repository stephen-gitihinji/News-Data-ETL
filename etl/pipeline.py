#running the pipeline by integrating the modules
from etl.extract import extract_news
from etl.transform import transform_news
from etl.load import load_news

def run_pipeline():
    try:
        articles = extract_news()
        if not articles:
            print("There are no Articles!")
        transformed_data = transform_news(articles)
        if not transformed_data:
            print("No data has been transformed")
        load_news(transformed_data)
    except Exception as e:
        print(f"Pipeline has failed {e}")
