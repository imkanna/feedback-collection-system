from dataclasses import dataclass

@dataclass
class LoggerConfiguration:
    log_level: str

@dataclass
class DatabaseConfiguration:
    host: str
    port: int
    name: str
    user: str
    password: str

@dataclass
class ApplicationContext:
    port: int
    process: int
    logger_configs: LoggerConfiguration
    db_configs: DatabaseConfiguration