#creating a dataframe from the data obtained and storing it to a database
import pandas as pd
from sqlalchemy import create_engine
from config import DB_HOST, DB_PORT, DB_NAME, DB_PASSWORD, DB_USER

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
   # connect_args= {"options" : "-c search_path=news_schema"} #modifying the search path sqlalchemy
    )

def load_news(data):
    df = pd.DataFrame(data)
    try:
        df.to_sql(name="news", con=engine, if_exists='replace', index=False)
        print("Data loaded successfully!")
    except Exception as e:
        print("There was a problem with loading the data!", e)
