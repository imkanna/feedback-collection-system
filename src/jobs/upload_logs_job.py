import glob
import zipfile
from os.path import abspath, join, dirname, split
from os import remove
from datetime import datetime

from src.utils.minio_client import MinioClient
from src.utils.logger import Logger

class UploadLogsToMinio:

    __BUCKET_NAME = "feedback-collector-logs"

    @classmethod
    def upload_files_to_minio(cls):
        cls.get_logger().info('Uploading log files to minio')
        try:
            cls.__generate_zip_file()
            client = MinioClient.get_client()
            bucket_exists = client.bucket_exists(cls.__BUCKET_NAME)

            # create bucket if bucket not available
            if not bucket_exists:
                  cls.get_logger().info(f'Bucket not found, creating new bucket with name {cls.__BUCKET_NAME}')
                  client.make_bucket(cls.__BUCKET_NAME)

            # upload zip files to minio
            log_file_path = f'{abspath(join(dirname(__file__), "../.."))}/logs'
            ziped_files = glob.glob(f'{log_file_path}/*.zip')
            for file in ziped_files:
                file_name = split(file)[1]
                
                cls.get_logger().info(f'Uploading file {file_name}')
                client.fput_object(cls.__BUCKET_NAME, file_name, file)
                cls.get_logger().info(f'Successfully uploaded {file_name}')

                # delete uploaded file
                remove(file)

        except Exception:
            cls.get_logger().error(f'Logfile upload failed')
            pass


    @classmethod
    def __generate_zip_file(cls):
        # check for log files availability
        log_file_path = f'{abspath(join(dirname(__file__), "../.."))}/logs'
        log_files = glob.glob(f'{log_file_path}/*.log.[0-9]')

        # create logfiles.zip
        if log_files:
            with zipfile.ZipFile(f'{log_file_path}/{datetime.now().strftime("%d-%M-%Y_%H:%M:%S")}_logs.zip', 'w') as zip:
                for file in log_files:
                    zip.write(file, split(file)[1])
        
        #remove the rotated log files
        ziped_files = glob.glob(f'{log_file_path}/*.zip')
        if ziped_files:
            for file in log_files:
                remove(file)
    
    @classmethod
    def get_logger(cls):
        return Logger(cls.__name__)