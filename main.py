import os
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\kings\Documents\projects\cloud_storage\serviceKeyGoogle.json"

# storage_client = storage.Client()

# my_bucket = "my-ebay-laptop-prices"

# bucket = storage_client.create_bucket(my_bucket)

# msg = f"Bucket with name {bucket.name} has been created"

# print(msg)

def create_bucket_class_location(bucket_name):
    """
    Create a new bucket in the US region with the coldline storage
    class
    """
    # bucket_name = "your-new-bucket-name"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "COLDLINE"
    new_bucket = storage_client.create_bucket(bucket, location="us")

    print(
        "Created bucket {} in {} with storage class {}".format(
            new_bucket.name, new_bucket.location, new_bucket.storage_class
        )
    )
    return new_bucket

create_bucket_class_location('ebay-products-prices')
