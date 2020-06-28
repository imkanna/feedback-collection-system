from os.path import abspath, join, dirname
from tornado.ioloop import IOLoop
from tornado.web import Application
from tornado.httpserver import HTTPServer

from src.server.router import Router
from src.server.application_context import ApplicationContext
from src.utils.argument_parsing_utils import ArgumentParsingUtils
from src.utils.logger import Logger
from src.database.mongo import Mongo

class Server:

    @classmethod
    def start(cls):
        # Read command line arguments
        context: ApplicationContext = ArgumentParsingUtils.parse_arguments()

        #initiate application logging
        Logger.initiate_logger(context.logger_configs)
        
        #getting logger
        logger = Logger(cls.__name__)
        logger.info('Initializing the application...')
        logger.debug(f'Configurations: {context}')

        settings = {
            'template_path': abspath(join(dirname(__file__), '../../views/templates')),
            'static_path': abspath(join(dirname(__file__), '../../views/static'))
        }
        # Create application by assigning routes and the location of view files
        app = Application(Router.routes(), **settings)
        
        # Server creation
        server = HTTPServer(app)
        server.bind(context.port)
        server.start(context.process)
        
        # Connect to MongoDB server
        Mongo.init(context.db_configs)
        # This is done so that every incoming request has a pointer to the database connection
        app.settings['db'] = Mongo.get()

        logger.info(f'Listining on port {context.port}')
        IOLoop.current().start()
