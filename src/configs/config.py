application = {
    "port": 8080,
    "process": 0, #defining 0 to create number of processes equal to the available processors.'
    "log_level": "INFO",
    "log_upload_interval": 1, # hours
    "db_host": "localhost",
    "db_port": 27017,
    "db_name": "feedback_db",
    "db_user": None,
    "db_password": None,
    "minio_host": "localhost:9000",
    "minio_access_key": "minioadmin",
    "minio_secret_key": "minioadmin"
}