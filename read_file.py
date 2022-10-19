

# Imports the Google Cloud client library
from google.cloud import storage
import os
import io
from io import BytesIO
import pandas as pd

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\kings\Documents\projects\cloud_storage\serviceKeyGoogle.json"

def write_read(bucket_name, blob_name):
    """Write and read a blob from GCS using file-like IO"""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your new GCS object
    # blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Mode can be specified as wb/rb for bytes mode.
    # See: https://docs.python.org/3/library/io.html
    # with blob.open("w") as f:
    #     f.write("Hello world")

    with blob.open("r") as f:
        print(f.read())

write_read("my-ebay-laptop-prices", "laptops.csv")