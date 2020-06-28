from minio import Minio

from src.utils.logger import Logger
from src.server.application_context import MinioConfigurations

class MinioClient:
    __CLIENT = None

    @classmethod
    def init(cls, minio_configs: MinioConfigurations):
        """ Create Minio client."""
        cls.get_logger().info('Creating minio client...')
        if not cls.__CLIENT:
            cls.__CLIENT = Minio(minio_configs.host,
                    access_key=minio_configs.access_key,
                    secret_key=minio_configs.secret_key,
                    secure=False)

    @classmethod
    def get_client(cls) -> Minio:
        if not cls.__CLIENT:
            cls.get_logger().error('Minio client not found')
        return cls.__CLIENT

    @classmethod
    def get_logger(cls):
        return Logger(cls.__name__)
