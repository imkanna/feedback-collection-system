from tornado.web import RequestHandler
import ast
from gzip import compress
from json import dumps, loads

from src.database.mongo import Mongo
from src.model.errors.error import Error
from src.utils.logger import Logger

class BaseRequestHandler(RequestHandler):

    INTERNAL_ERROR_MESSAGE = 'Internal Server Error.'

    def prepare(self):
        # This is needed so that every request can access globally to the database
        Mongo.set(self.settings['db'])

    def _parse_body(self):
        try:
            return ast.literal_eval(self.request.body.decode('utf-8').replace('\t', '').replace('\n', ''))
        except RuntimeError:
            raise Error(f'Invalid request body {self.request.body}', 400)

    def make_error_response(self, status_code, message):
        """ Create a common error response. """
        self._get_logger().error(f'{status_code} | {message}')
        self.set_status(status_code)
        response = {'status': status_code, 'message': message}
        self.write(response)

    def make_response(self, response_body=None, status_code=200):
        """ Create a common success response. """
        self.set_status(status_code)
        # Set default JSON content header
        self.set_header('Content-Type', 'application/json')
        # Null response is also accepted
        if response_body is not None:
            # This is in case of gzip encoding
            if 'Accept-Encoding' in self.request.headers and 'gzip' in self.request.headers['Accept-Encoding']:
                self.set_header('Content-Encoding', 'gzip')
                self.write(compress(bytes(str(response_body), 'utf-8')))
            else:
                # The following is done to accept List responses.
                json_response = response_body if not isinstance(response_body, str) else loads(response_body)
                self.write(dumps(json_response))

    def _get_logger(self):
        return Logger(self.__class__.__name__)