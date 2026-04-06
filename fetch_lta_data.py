import os
import json
import requests
from datetime import datetime

from config.config import BASE_URL, HEADERS, RAW_DATA_DIR


def ensure_directory_exists(directory: str) -> None:
    """Create directory if it does not already exist."""
    os.makedirs(directory, exist_ok=True)


def fetch_bus_arrival_data(bus_stop_code: str) -> dict:
    """
    Fetch bus arrival data from LTA DataMall Bus Arrival v3 API.
    """
    params = {"BusStopCode": bus_stop_code}

    response = requests.get(
        BASE_URL,
        headers=HEADERS,
        params=params,
        timeout=30
    )
    response.raise_for_status()
    return response.json()


def save_raw_json(data: dict, bus_stop_code: str) -> str:
    """
    Save raw API response as a timestamped JSON file.
    """
    ensure_directory_exists(RAW_DATA_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"bus_arrival_{bus_stop_code}_{timestamp}.json"
    file_path = os.path.join(RAW_DATA_DIR, file_name)

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return file_path


def main() -> None:
    bus_stop_code = "22009"

    try:
        print(f"Fetching bus arrival data from LTA v3 for bus stop: {bus_stop_code}")
        data = fetch_bus_arrival_data(bus_stop_code)

        saved_file = save_raw_json(data, bus_stop_code)

        print("Data fetched successfully.")
        print(f"Raw JSON saved at: {saved_file}")
        print(f"Services returned: {len(data.get('Services', []))}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        if http_err.response is not None:
            print("Response text:", http_err.response.text)

    except requests.exceptions.RequestException as req_err:
        print(f"Request failed: {req_err}")

    except Exception as err:
        print(f"Unexpected error: {err}")


if __name__ == "__main__":
    main()