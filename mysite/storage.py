from django.core.files.storage import Storage
from boto3.session import Session


class S3Storage(Storage):
    def __init__(self, *args, **kwargs):
        self.session = Session(
            aws_access_key_id=kwargs.get("access_key"),
            aws_secret_access_key=kwargs.get("secret_key"),
        )
        self.s3 = self.session.resource("s3")
        self.bucket_name = kwargs.get("bucket_name")

    def _open(self, name, mode="rb"):
        obj = self.s3.Object(self.bucket_name, name)
        return obj.get()["Body"]

    def _save(self, name, content):
        obj = self.s3.Object(self.bucket_name, name)
        obj.put(Body=content)
        return name

    def exists(self, name):
        obj = self.s3.Object(self.bucket_name, name)
        return obj.exists()

    def url(self, name):
        return f"https://{self.bucket_name}.s3.amazonaws.com/{name}"
