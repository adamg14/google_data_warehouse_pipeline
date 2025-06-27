from google.cloud import storage
from google.cloud import bigquery

parent_dir = str(Path(__file__).resolve().parent.parent)
sys.path.append(parent_dir)

from utils.constants import PARQUET_URL, FILE_NAME, BUCKET_NAME, DATASET_ID, TABLE_ID


def gcp_bucket_load(source_file_name):
    """This function takes the extracted data from the data source and uploads it to a google cloud bucket"""
    storage_client = storage.Client.from_service_account_json('./gcp_credentials.json')
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(BLOB_NAME)

    generation_match_precondition = 0
    blob.upload_from_filename(
        source_file_name,
        if_generation_match=generation_match_precondition
    )

    print(f"Extracted and processed data uploaded to gs://{bucket_name}/{blob_name}")


def gcp_bq_load(source_file_name):
    """This function takes the data from the Google Cloud Storage bucket uploaded using the function above and loads it to Google BigQuery"""
    client = bigquery.Client.from_service_account_json('./gcp_credentials.json')

    dataset = client.dataset(DATASET_ID)
    table = dataset.table(TABLE_ID)

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )

    with open(source_file, "rb") as source_file:
        job = client.load_table_from_file(
            source_file,
            table,
            job_config=job_config
        )
    
    print(f"Loaded {job.output_rows} rows to Google Big Query Table: {TABLE_ID}")


def main():
    gcp_bucket_load()
    gcp_bq_load()