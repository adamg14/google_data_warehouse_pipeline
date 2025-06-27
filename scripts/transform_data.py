import pandas as pd

taxi_data = pd.read_csv("./data/raw_data.csv", low_memory=False)
print(taxi_data)

def clean_data(csv_file):
    # define the data types of the columns of the CSV file
    data_types = {
        "VendorID": "Int64",
        "passenger_count": "Int64",
        "trip_distance": "float64",
        "RateCodeID": "float64",
        "store_and_fwd_flag": "str",
        "PULocationID": "Int64",
        "DOLocationID": "Int64",
        "payment_type": "Int64",
        "fare_amount": "float64",
        "extra": "float64",
        "mta_tax": "float64",
        "tip_amount": "float64",
        "tolls_amount": "float64",
        "improvement_surcharge": "float64",
        "total_amount": "float64",
        "congestion_surcharge": "float64",
        "Airport_fee": "float64"
    }

    taxi_data = pd.read(csv_file, dtype=data_types)
    taxi_data["tpep_pickup_datetime"] = pd.to_datetime(taxi_data["tpep_pickup_datetime"])
    taxi_data["tpep_dropoff_datetime"] = pd.to_datetime(taxi_ata["tpep_dropoff_datetime"])

    # insert first column
    taxi_data.insert(0, 'trip_id', range(1, len(taxi_data + 1)))

    # calculation of trip duration=
    taxi_data['trip_duration_min'] = (taxi_data['tpep_dropoff_datetime'] - taxi_data['tpep_pickup_datetime']).dt.total_seconds / 60

    clean_taxi_data = taxi_data.copy()

    clean_columns = final_columns = [
        'trip_id',
        'VendorID',
        'tpep_pickup_datetime', 'tpep_dropoff_datetime',
        'trip_duration_min',
        'passenger_count',
        'trip_distance',
        'speed_mph',
        'RatecodeID',
        'is_store_and_fwd',
        'PULocationID',
        'DOLocationID',
        'payment_type',
        'fare_amount',
        'extra',
        'mta_tax',
        'tip_amount',
        'tolls_amount',
        'improvement_surcharge',
        'total_amount',
        'congestion_surcharge',
        'Airport_fee'
    ]

    clean_taxi_data = clean_taxi_data[clean_columns]

    clean_taxi_data.to_csv(csv_file, index=False)

    print(f"Cleaned records saved to CSV file: {csv_file}")
    return clean_taxi_data


transform_data("./data/raw_data.csv")