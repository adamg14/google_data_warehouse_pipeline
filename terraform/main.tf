locals{
    project_id = var.project_id
    region = var.region
    bucket_suffix = replace(lower(var.project_id), "/[^a-z0-9]/", "-") 
}

# Google Cloud Platform Storage Bucket
resource "google_storage_bucket" "nyc_taxi_data" {
    name = "nyc-taxi-data-8888"
    location = upper(var.region)
    storage_class = "STANDARD"
    uniform_bucket_level_access = true
    force_destroy =  true

    versioning {
      enabled = true
    }

    lifecycle_rule {
      condition {
        age = 30
      }
      
      action {
        type = "Delete"
      }
    }

    labels = {
      environment = "dev"
      terraformed = "true"
    }
}

# Google Cloud Platform BigQuery Dataset
resource "google_bigquery_dataset" "dataset" {
    dataset_id = var.dataset_id
    friendly_name = "NYC Yello Taxi Data"
    description = "Dataset contains NYC taxi trip data for the first half of 2024"
    location = var.region
    delete_contents_on_destroy = true

    labels = {
      env = "dev"
    }
}

# Google Cloud Platform BigQuery Table
resource "google_bigquery_table" "table" {
  dataset_id = var.dataset_id
  table_id = var.table_id

  deletion_protection = false

  labels = {
    env = "dev"
  }
}

resource "google_bigquery_job" "load_raw_data" {

  job_id = "load_raw_data_${formatdate("YYYYMMDDhhmmss", timestamp())}"

  load {
    source_uris = [ "gs://"${var.bucket_name}/{var.blob_name} ]

    destination_table {
      project_id = var.project_id
      dataset_id = var.dataset_id
      table_id = var.table_id
    }

    skip_leading_rows = 1
    source_format = "CSV"
    autodetect = true
  }


}