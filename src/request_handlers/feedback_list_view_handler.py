from tornado.web import RequestHandler
from tornado.template import Loader
from src.service.feedbackService import FeedbackService
from src.model.errors.error import Error

class FeedbackListViewHandler(RequestHandler):
    async def get(self):
        reference = self.get_argument('reference', None)
        #if not reference: send error page
        feedbacks = await FeedbackService.get_all_feedback(reference)
        loader = Loader(self.get_template_path())
        self.write(loader.load('feedback_table.html').generate(feedbacks=feedbacks, reference=reference))