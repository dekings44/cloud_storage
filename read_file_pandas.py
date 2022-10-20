from google.cloud import storage
import os
import io
from io import BytesIO
import pandas as pd
from fsspec.registry import known_implementations

#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\kings\Documents\projects\cloud_storage\serviceKeyGoogle.json"


file_path = "gcs://my-ebay-laptop-prices/laptops.csv"
df = pd.read_csv(file_path,
                 sep=",",
                 storage_options={"token": "serviceKeyGoogle.json"})


print(df.head())
print(df.info())