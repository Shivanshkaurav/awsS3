from storages.backends.s3boto3 import S3Boto3Storage
import os

class StaticStorage(S3Boto3Storage):
    location = 'static'
    file_overwrite = False
    # custom_domain = os.getenv("AWS_S3_CUSTOM_DOMAIN")

class MediaStorage(S3Boto3Storage):
    location = 'media'
    default_acl = 'public-read'
    file_overwrite = False
    # custom_domain = os.getenv("AWS_S3_CUSTOM_DOMAIN")