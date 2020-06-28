from typing import List

from src.model.feedback import Feedback
from src.utils.logger import Logger
from src.database.daos.feedback_dao import FeedbackDao
from src.jobs.upload_logs_job import UploadLogsToMinio

class FeedbackService:

    @classmethod
    async def add_feedback(cls, feedback: Feedback):
        logger = Logger(cls.__name__)
        logger.info(f'Feedback received- {{reference: {feedback.reference}, name: {feedback.name}}}')
        logger.debug(f'Feedback received- {feedback}')
        UploadLogsToMinio.upload_files_to_minio()
        await FeedbackDao.insert_feedback(feedback)

    @classmethod
    async def get_all_feedback(cls, reference: str) -> List[Feedback]:
        logger = Logger(cls.__name__)
        logger.info(f'Get all feedback - reference: {reference}')
        
        return await FeedbackDao.get_all_feedback(reference)
