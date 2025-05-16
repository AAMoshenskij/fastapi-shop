# apps/analytics/etl/products_etl.py
import pandas as pd
from sqlalchemy import create_engine
from config.settings import DATABASES

def load_products_from_csv():
    df = pd.read_csv('products.csv')
    
    # Преобразование данных под вашу модель
    df_clean = df.rename(columns={
        'name': 'product_name',
        'link': 'external_link',
        'image': 'external_image_url',
        'ratings': 'external_ratings',
        'no_of_ratings': 'external_ratings_count',
        'actual_price': 'external_price',
        'discount_price': 'external_discount_price'
    })
    
    # Очистка числовых полей (например, "30,227" -> 30227)
    df_clean['external_ratings_count'] = df_clean['external_ratings_count'].str.replace(',', '').astype(int)
    
    # Загрузка в PostgreSQL
    engine = create_engine(DATABASES["url"])
    df_clean.to_sql('products', engine, if_exists='append', index=False)
