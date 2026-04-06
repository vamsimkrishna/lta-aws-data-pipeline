import os
from datetime import datetime

from src.utils.aws_helper import upload_file_to_s3

PROCESSED_DATA_DIR = "data/processed"


def get_latest_processed_file() -> str:
    """
    Return the most recently created processed file.
    """
    if not os.path.exists(PROCESSED_DATA_DIR):
        raise FileNotFoundError(f"Processed data directory not found: {PROCESSED_DATA_DIR}")

    files = [
        os.path.join(PROCESSED_DATA_DIR, file_name)
        for file_name in os.listdir(PROCESSED_DATA_DIR)
        if os.path.isfile(os.path.join(PROCESSED_DATA_DIR, file_name))
    ]

    if not files:
        raise FileNotFoundError("No processed files found in data/processed")

    latest_file = max(files, key=os.path.getctime)
    return latest_file


def build_s3_key(local_file_path: str) -> str:
    """
    Build the S3 key for processed files using today's date.
    """
    now = datetime.now()
    file_name = os.path.basename(local_file_path)

    return (
        f"processed/bus_arrival/"
        f"{now.year}/"
        f"{now.month:02d}/"
        f"{now.day:02d}/"
        f"{file_name}"
    )


def main() -> None:
    try:
        latest_file = get_latest_processed_file()
        print(f"Latest processed file found: {latest_file}")

        s3_key = build_s3_key(latest_file)
        print(f"S3 destination key: {s3_key}")

        upload_file_to_s3(latest_file, s3_key)

    except Exception as error:
        print(f"Processed upload failed: {error}")


if __name__ == "__main__":
    main()