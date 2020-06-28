from src.request_handlers.feedback_form_view_handler import FeedbackFormViewHandler
from src.request_handlers.feedback_list_view_handler import FeedbackListViewHandler
from src.request_handlers.feedback_request_handler import FeedbackRequestHandler
from src.utils.logger import Logger

class Router:

    # Dictionary to map routes to Tornado RequestHandler subclasses
    ROUTES = {
        '/': FeedbackFormViewHandler,
        '/feedback': FeedbackRequestHandler,
        '/feedback/list': FeedbackListViewHandler
    }

    @classmethod 
    def routes(cls):
        """ Get routes with their respective handlers"""
        Logger(cls.__name__).debug(f'routes added: {[(k) for k, v in cls.ROUTES.items()]}')
        return [(k, v) for k, v in cls.ROUTES.items()]
