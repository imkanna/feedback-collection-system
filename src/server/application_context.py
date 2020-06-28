from dataclasses import dataclass

@dataclass
class LoggerConfiguration:
    log_level: str
    log_upload_interval: int

@dataclass
class DatabaseConfiguration:
    host: str
    port: int
    name: str
    user: str
    password: str

@dataclass
class MinioConfigurations:
    host: str
    access_key: str
    secret_key: str
    
@dataclass
class ApplicationContext:
    port: int
    process: int
    logger_configs: LoggerConfiguration
    db_configs: DatabaseConfiguration
    minio_configs: MinioConfigurations