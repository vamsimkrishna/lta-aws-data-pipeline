import os
import boto3
from dotenv import load_dotenv

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION")
S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")


def get_s3_client():
    """
    Create and return an S3 client using credentials from the .env file.
    """
    return boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION
    )


def upload_file_to_s3(local_file_path: str, s3_key: str) -> None:
    """
    Upload a local file to the configured S3 bucket.
    """
    s3_client = get_s3_client()

    s3_client.upload_file(
        Filename=local_file_path,
        Bucket=S3_BUCKET_NAME,
        Key=s3_key
    )

    print(f"Upload successful: s3://{S3_BUCKET_NAME}/{s3_key}")