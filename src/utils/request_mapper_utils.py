from src.model.feedback import Feedback
from src.model.errors.error import Error
import uuid
import time

class RequestMapper:
    
    @staticmethod
    def formatFeedback(request_body: dict) -> Feedback:
        if not request_body: raise Error('Feedback not found', 400)
        if not 'reference' in request_body.keys(): raise Error('reference not found', 400)
        if not 'name' in request_body.keys(): raise Error('reference not found', 400)
        if not 'message' in request_body.keys(): raise Error('reference not found', 400)

        return Feedback(
            id = uuid.uuid1(),
            reference = request_body['reference'],
            name=request_body['name'],
            message=request_body['message'],
            created=time.time()
        )
