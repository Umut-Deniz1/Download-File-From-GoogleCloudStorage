
# pip install --upgrade google-cloud-storage

# download certain file
from google.cloud import storage
import os
from pathlib import Path
import nltk
nltk.download('punkt')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your credential"
storage_client = storage.Client("[project name]")
bucket = storage_client.get_bucket('bucketname')
blob = bucket.blob("path/to/file")
blob.download_to_filename("filename")


# Download directory
bucket = storage.Bucket(storage_client, "bucketname", user_project="project")
all_blobs = list(storage_client.list_blobs(bucket))

for blob in all_blobs:
    if blob.name.endswith("/"):
        continue
    if blob.name.startswith("path/to/file"):
        file_split = blob.name.split("/")
        directory = "/".join(file_split[0:-1])
        Path(directory).mkdir(parents=True, exist_ok=True)
        blob.download_to_filename(blob.name)
        print(blob.name)
