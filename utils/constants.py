import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

PARQUET_URL = parser.get("project_variables", "PARQUET_URL")
FILE_NAME = parser.get("project_variables", "FILE_NAME")

GCP_PROJECT = parser.get("google_cloud_platform", "PARQUET_URL")
BUCKET_NAME = parser.get("google_cloud_platform", "BUCKET_NAME")
BLOB_NAME = parser.get("google_cloud_platform", "BLOB_NAME")

DATASET_ID = parser.get("google_cloud_platform", "DATASET_ID")
TABLE_ID = parser.get("google_cloud_platform", "TABLE_ID")