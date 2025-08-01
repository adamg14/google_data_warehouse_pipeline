import os
import requests
import pandas as pd
from google.cloud import storage
from google.cloud import bigquery
from datetime import datetime
from pathlib import Path
import sys

parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

from utils.constants import PARQUET_URL, FILE_NAME, BUCKET_NAME

FILE_ENDINGS = [
    "2024-01.parquet",
    "2024-02.parquet",
    "2024-03.parquet",
    "2024-04.parquet",
    "2024-05.parquet",
    "2024-06.parquet"
    ]

# need to reuse this functions for all the different files that need to be downloaded
def download_csv(PARQUET_URL):
    print("Downloading required PARQUET file...")

    combined_data = pd.DataFrame()

    for endings in FILE_ENDINGS:
        url = f"{PARQUET_URL}{endings}"

        try:
            response = requests.get(url)
            response.raise_for_status()

            temp_data_store = pd.read_parquet(url)
            print(temp_data_store)

            combined_data = pd.concat([combined_data, temp_data_store], ignore_index=True)

        except Exception as e:
            print(f"An error occured while downloading the file")
            print(e)
            break
        
    
    combined_data.to_csv(f"./data/{FILE_NAME}")
    print("Data successfully extracted")
    return combined_data


# function for processing the data using pandas



def main():
    download_csv(PARQUET_URL)


if __name__ == "__main__":
    main()

