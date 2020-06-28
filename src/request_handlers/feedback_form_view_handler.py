from tornado.web import RequestHandler
from tornado.template import Loader

class FeedbackFormViewHandler(RequestHandler):
    def get(self):
        loader = Loader(self.get_template_path())
        self.write(loader.load('feedback.html').generate(static_url=self.static_url))