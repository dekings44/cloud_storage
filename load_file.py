from google.cloud import storage
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\kings\Documents\projects\cloud_storage\serviceKeyGoogle.json"

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )

source_file_name = "../ebay_prices/ebay_laptops.csv"
bucket_name = "my-ebay-laptop-prices"
destination_blob_name = "my_ebay_laptops.csv"

upload_blob(bucket_name, source_file_name, destination_blob_name)