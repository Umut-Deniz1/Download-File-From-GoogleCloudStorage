
#pip install --upgrade google-cloud-storage
from google.cloud import storage
import os
from pathlib import Path
import nltk
nltk.download('punkt')
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "betatests-bad323259eb9.json"
storage_client = storage.Client("[BetaTests]")
bucket = storage_client.get_bucket('betatests.appspot.com')
blob = bucket.blob("chatbot/chatbotmodel.h5")
blob.download_to_filename("chatbotmodel.h5")


#Download dir
bucket = storage.Bucket(storage_client, "betatests.appspot.com", user_project="BetaTests")
all_blobs = list(storage_client.list_blobs(bucket))

for blob in all_blobs:
    if blob.name.endswith("/"):
        continue
    if blob.name.startswith("chatbot/nltk_data/"):
        file_split = blob.name.split("/")
        directory = "/".join(file_split[0:-1])
        Path(directory).mkdir(parents=True, exist_ok=True)
        blob.download_to_filename(blob.name)
        print(blob.name)
