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