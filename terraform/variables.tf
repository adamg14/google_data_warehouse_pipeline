variable "project_id" {
    description = "The Google Cloud Project ID where resources will be created"
    type = string
    default = "taxi-data-pipeline-463918"
}

variable "region" {
  description = "The Google Cloud region where the resources will be deployed"
  type = string
  default = "us-central1"
}

variable "dataset_id" {
    description = "BigQuery Dataset ID"
    type = string
    default = "nyc_yellow_taxi_data"
}

variable "table_id" {
    description = "BigQuery Table ID"
    type = string
    default = "taxi_trips"
}

variable "bucket_name"{
    description = "Google Cloud Storage Bucket Name"
    type = string
    default = "nyc-taxi-data-8888"
}

variable "blob_name" {
    description = "Google Cloud Storage BLOB Name"
    type = string
    default = "extracted_data.csv"
}
