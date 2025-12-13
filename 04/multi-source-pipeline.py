#!/usr/bin/env python3

import pandas as pd
import os
import requests
import json


def ingest_csv(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        print("Ingesting CSV file: ", file_path)
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print(f"Error ingesting CSV file: {e}")
        return None


def ingest_json(file_path):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")
        print("Ingesting JSON file: ", file_path)
        with open(file_path, "r") as fh:
            data = json.load(fh)

        if isinstance(data, dict):
            df = pd.DataFrame.from_dict(data)
        elif isinstance(data, list):
            df = pd.DataFrame(data)
        else:
            raise ValueError("JSON data is not a dictionary or list")
        return df

    except Exception as e:
        print(f"Error ingesting JSON file: {e}")
        return None


def ingest_api(url):
    try:
        if url == "":
            raise ValueError("URL is empty")
        print("Ingesting API: ", url)
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        if "hourly" not in data:
            raise KeyError("Missing 'hourly' key in API response")
        hourly_data = pd.DataFrame(data["hourly"])
        return hourly_data

    except Exception as e:
        print(f"Error ingesting API: {e}")
        return None


def run_pipeline():
    api_url = "https://api.open-meteo.com/v1/forecast?latitude=40.7&longitude=-74.0&hourly=temperature_2m"
    csv_file_path = "data/input.csv"
    json_file_path = "data/input.json"

    csv_df = ingest_csv(csv_file_path)
    if csv_df is not None:
        print(f"CSV data shape: {csv_df.shape}")

    json_df = ingest_json(json_file_path)
    if json_df is not None:
        print(f"JSON data shape: {json_df.shape}")

    api_df = ingest_api(api_url)
    if api_df is not None:
        print(f"API data shape: {api_df.shape}")


if __name__ == "__main__":
    run_pipeline()
