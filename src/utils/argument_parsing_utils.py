from argparse import ArgumentParser

from src.server.application_context import ApplicationContext, LoggerConfiguration, DatabaseConfiguration, MinioConfigurations
import src.configs.config as config

class ArgumentParsingUtils:

    @classmethod
    def parse_arguments(cls) -> ApplicationContext:
        """ Get environment from program argument_parsing. """
        parser = ArgumentParser()
        # Set up argument values
        parser.add_argument('--port', default=config.application["port"], type=int, help='Port where application will listen')
        parser.add_argument('--process', default=config.application["process"], type=int, help='Number of processes')
        parser.add_argument('--log_level', default=config.application["log_level"], type=str, help='Log level')
        parser.add_argument('--log_upload_interval', default=config.application["log_upload_interval"], type=str, help='Log upload interval in hours')
        parser.add_argument('--db_host', default=config.application["db_host"], type=str, help='DB host')
        parser.add_argument('--db_port', default=config.application["db_port"], type=int, help='DB port')
        parser.add_argument('--db_name', default=config.application["db_name"], type=str, help='DB name')
        parser.add_argument('--db_user', default=config.application["db_user"], type=str, help='DB user')
        parser.add_argument('--db_password', default=config.application["db_password"], type=str, help='DB password')
        parser.add_argument('--minio_host', default=config.application["minio_host"], type=str, help='Minio host')
        parser.add_argument('--minio_access_key', default=config.application["minio_access_key"], type=str, help='Minio access_key')
        parser.add_argument('--minio_secret_key', default=config.application["minio_secret_key"], type=str, help='Minio secret_key')
        
        # Get program argument_parsing
        args = parser.parse_args()

        # logger parameters
        logger_configs = LoggerConfiguration(
            log_level=args.log_level,
            log_upload_interval=args.log_upload_interval
        )

        # db parameters
        db_configs = DatabaseConfiguration(
            host=args.db_host,
            port=args.db_port,
            name=args.db_name,
            user=args.db_user,
            password=args.db_password
        )

        minio_configs = MinioConfigurations(
            host=args.minio_host,
            access_key=args.minio_access_key,
            secret_key=args.minio_secret_key
        )

        # Build application context
        return ApplicationContext(
            port=args.port,
            process=args.process,
            logger_configs = logger_configs,
            db_configs=db_configs,
            minio_configs=minio_configs
        )
