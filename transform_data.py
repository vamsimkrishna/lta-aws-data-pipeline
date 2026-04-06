import os
import json
import pandas as pd
from datetime import datetime

RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"


def get_latest_raw_file():
    files = [
        os.path.join(RAW_DATA_DIR, f)
        for f in os.listdir(RAW_DATA_DIR)
    ]
    return max(files, key=os.path.getctime)


def extract_records(json_data):
    records = []

    bus_stop = json_data.get("BusStopCode")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for service in json_data.get("Services", []):
        service_no = service.get("ServiceNo")

        next_bus = service.get("NextBus", {})

        record = {
            "bus_stop": bus_stop,
            "service_no": service_no,
            "arrival_time": next_bus.get("EstimatedArrival"),
            "load": next_bus.get("Load"),
            "origin_code": next_bus.get("OriginCode"),
            "destination_code": next_bus.get("DestinationCode"),
            "record_timestamp": timestamp
        }

        records.append(record)

    return records


def main():
    latest_file = get_latest_raw_file()
    print(f"Processing file: {latest_file}")

    with open(latest_file, "r") as f:
        data = json.load(f)

    records = extract_records(data)

    df = pd.DataFrame(records)

    os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{PROCESSED_DATA_DIR}/processed_bus_arrival_{timestamp}.csv"

    df.to_csv(output_file, index=False)

    print("Transformation complete")
    print(f"Processed file saved at: {output_file}")
    print(df.head())


if __name__ == "__main__":
    main()