import pandas as pd
from elasticsearch.helpers import bulk
from .client import create_elastic_client  # client.py dosyasından import ettik

class CSVIndexer:
    def __init__(self, indexname="kadir"):
        self.indexname = indexname
        self.client = create_elastic_client()

    def index_csv(self, csv_path):
        df = pd.read_csv(csv_path)

        if "product_name" not in df.columns or "prices" not in df.columns:
            raise ValueError("HATA: CSV'de eksik sütunlar var!")

        products = [
            {
                "_index": self.indexname,
                "_source": {
                    "product_name": str(row["product_name"]),
                    "prices": float(row["prices"]),
                    "rating_count": str(row.get("rating_count", "N/A")),  
                    "attributes": {}
                }
            }
            for _, row in df.iterrows()
        ]

        bulk(self.client, products)
        print(f"{len(products)} veri başarıyla indekslendi.")

