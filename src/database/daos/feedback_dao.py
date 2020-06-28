from typing import List

from src.model.feedback import Feedback
from src.database.mongo import Mongo
from src.utils.logger import Logger
from src.model.errors.error import Error

class FeedbackDao:
    @classmethod
    async def insert_feedback(cls, data: Feedback):
        logger = Logger(cls.__name__)
        logger.info(f'Creating feedback - id: {data.id}, reference: {data.reference}, name: {data.name}')
        
        await Mongo.get().feedback.insert_one(cls.__to_document(data))
        

    @classmethod
    async def get_all_feedback(cls, reference: str) -> List[Feedback]:
        Logger(cls.__name__).info(f'Getting all feedbacks - reference: {reference}')
        
        cursor = Mongo.get().feedback.find({'reference': reference}).sort([('reference', 1)])
        result = []
        while await cursor.fetch_next:
            result.append(cls.__to_object(cursor.next_object()))
        return result

    @classmethod
    def __to_document(cls, data: Feedback) -> dict:
        document = dict()
        document['id'] = data.id
        if data.reference: document['reference'] = data.reference
        if data.name: document['name'] = data.name
        if data.message: document['message'] = data.message
        if data.created: document['created'] = data.created

        return document

    @classmethod
    def __to_object(cls, data: dict) -> Feedback:
        return Feedback(
            id=data['id'],
            reference=data['reference'],
            name=data['name'],
            message=data['message'],
            created=data['created']
        )