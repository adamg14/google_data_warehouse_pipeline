terraform {
  required_version = ">= 1.0.0"

  required_providers {
    google = {
        source = "hashicorp/google"
        version = "~> 4.51.0"
    }
  }
}

provider "google" {
    project = var.project_id
    region = var.region
    credentials = file("../gcp_credentials.json")
}