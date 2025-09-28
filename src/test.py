from google.cloud import storage

client = storage.Client()
bucket = client.bucket("mlops_project_2_anime_rec")
blob = bucket.blob("animelist.csv")
blob.download_to_filename("animelist.csv")



