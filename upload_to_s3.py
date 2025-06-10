import os
import boto3
from botocore.exceptions import ClientError

BUCKET_NAME = "szebi-s3-cloudfront"
LOCAL_FOLDER = "./dist"

def upload_files_to_s3():
    s3_client = boto3.client("s3")
    for root, dirs, files in os.walk(LOCAL_FOLDER):
        for file in files:
            local_path = os.path.join(root, file)
            relative_path = os.path.relpath(local_path, LOCAL_FOLDER)
            s3_key = relative_path.replace("\\", "/")
            s3_client.upload_file(
                local_path,
                BUCKET_NAME,
                s3_key,
                ExtraArgs={"ContentType": get_content_type(file)}
            )
            print(f"Uploaded {s3_key} successfully")

def get_content_type(filename):
    extension = os.path.splitext(filename)[1].lower()
    mime_types = {
        ".html": "text/html",
        ".css": "text/css",
        ".js": "application/javascript",
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif"
    }
    return mime_types.get(extension, "application/octet-stream")

if __name__ == "__main__":
    upload_files_to_s3()