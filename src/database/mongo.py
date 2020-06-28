from motor.motor_tornado import MotorClient

from src.server.application_context import DatabaseConfiguration
from src.utils.logger import Logger


class Mongo:
    """ MongoDB access point. """

    __CLIENT = None
    DB = None

    @classmethod
    def init(cls, db_data: DatabaseConfiguration):
        """ Create database with asynchronous connector."""
        cls.get_logger().info('Establishing database connection...')
        uri = cls.__create_uri(db_data.host, db_data.port, db_data.user, db_data.password, db_data.name)
        # Create db client
        cls.__CLIENT = MotorClient(uri)
        cls.DB = cls.__CLIENT.get_default_database()

    @classmethod
    def set(cls, db):
        cls.DB = db

    @classmethod
    def get(cls):
        return cls.DB

    @classmethod
    def __create_uri(cls, host, port, user, password, db_name):
        """ Generates database URI"""
        # Create auth string from parameters
        auth = f'{user}:{password}@' if user and password else ''
        # Create database URI
        return f'mongodb://{auth}{host}:{port}/{db_name}?retryWrites=false'

    @classmethod
    def get_logger(cls):
        return Logger(cls.__name__)
