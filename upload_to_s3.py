import os
from datetime import datetime

from src.utils.aws_helper import upload_file_to_s3

RAW_DATA_DIR = "data/raw"


def get_latest_raw_file() -> str:
    """
    Return the most recently created file from the raw data folder.
    """
    if not os.path.exists(RAW_DATA_DIR):
        raise FileNotFoundError(f"Raw data directory not found: {RAW_DATA_DIR}")

    files = [
        os.path.join(RAW_DATA_DIR, file_name)
        for file_name in os.listdir(RAW_DATA_DIR)
        if os.path.isfile(os.path.join(RAW_DATA_DIR, file_name))
    ]

    if not files:
        raise FileNotFoundError("No raw files found in data/raw")

    latest_file = max(files, key=os.path.getctime)
    return latest_file


def build_s3_key(local_file_path: str) -> str:
    """
    Build a partition-style S3 path using today's date.
    """
    now = datetime.now()
    file_name = os.path.basename(local_file_path)

    return (
        f"raw/bus_arrival/"
        f"{now.year}/"
        f"{now.month:02d}/"
        f"{now.day:02d}/"
        f"{file_name}"
    )


def main() -> None:
    try:
        latest_file = get_latest_raw_file()
        print(f"Latest raw file found: {latest_file}")

        s3_key = build_s3_key(latest_file)
        print(f"S3 destination key: {s3_key}")

        upload_file_to_s3(latest_file, s3_key)

    except Exception as error:
        print(f"Upload failed: {error}")


if __name__ == "__main__":
    main()