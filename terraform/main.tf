locals{
    project_id = var.project_id
    region = var.region
    bucket_suffix = replace(lower(var.project_id), "/[^a-z0-9]/", "-") 
}

# Google Cloud Storage Bucket
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

