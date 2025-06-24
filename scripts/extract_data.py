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

from utils.constants import PARQUET_URL, FILE_NAME


# need to reuse this functions for all the different files that need to be downloaded
def download_csv(PARQUET_URL):
    print("Downloading PARQUET file...")
    response = requests.get(PARQUET_URL) 
    response.raise_for_status()

    with open(f"./data/{FILE_NAME}", "wb") as f:
        f.write(response.content)
    print(f"PARQUET file saved")


# function for processing the data using pandas
# function to upload the processed data to a google cloud bucket
# function to load the data into big query
# 
def main():
    download_csv(PARQUET_URL)


if __name__ == "__main__":
    main()

