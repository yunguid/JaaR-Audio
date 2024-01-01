# Handles uploading and downloading from GCS

from google.cloud import storage


def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}")

if __name__ == "__main__":
    bucket_name = input("Please enter the bucket name: ")
    source_file_name = input("Please eneter the source file name: ")
    destination_blob_name = input("Please enter the destiniation blob name: ")
    upload_blob(bucket_name, source_file_name, destination_blob_name)


