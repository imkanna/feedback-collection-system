from .base_request_handler import BaseRequestHandler
from src.model.feedback import Feedback
from src.service.feedbackService import FeedbackService
from src.model.errors.error import Error 
from src.utils.request_mapper_utils import RequestMapper

class FeedbackRequestHandler(BaseRequestHandler):
    """ Handler for CRUD operations for feedback. """

    SUPPORTED_METHODS = ['GET', 'POST']

    async def post(self):
        try:
            resource = RequestMapper.formatFeedback(self._parse_body())
            await FeedbackService.add_feedback(resource)

            self.make_response(status_code=201)
        except Error as e:
            self.make_error_response(e.status, e.message)
        except RuntimeError:
            self.make_error_response(500, self.INTERNAL_ERROR_MESSAGE)

    async def get(self):
        try:
            result = await FeedbackService.get_all_feedback('a')

            self.make_response(response_body=result, status_code=200)
        except Error as e:
            self.make_error_response(e.status, e.message)
        except RuntimeError:
            self.make_error_response(500, self.INTERNAL_ERROR_MESSAGE)