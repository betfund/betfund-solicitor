# See: https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-using-sdk-python.html

from boto3 import client
from botocore.exceptions import ClientError

from betfund_solicitor import Message

AWS_REGIONS = {
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2",
    "ap-east-1",
    "ap-south-1",
    "ap-northeast-3",
    "ap-northeast-2",
    "ap-southeast-1",
    "ap-southeast-2",
    "ap-northeast-1",
    "ca-central-1",
    "cn-north-1",
    "cn-northwest-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "eu-north-1",
    "me-south-1",
    "sa-east-1",
    "us-gov-east-1",
    "us-gov-west-1"
}


class SimpleEmailService:
    """Class for handling Amazon SES operations.

    See: https://boto3.amazonaws.com/v1/documentation/

    Attributes
    ----------
    message : `betfund_solicitor.Message`
        Message object encapsulating all relevant configuration for the
        email to be sent.
    aws_access_key : str
        AWS Access Key ID from AWS management console.
    aws_secret_key : str
        AWS Secret Access Key from AWS management console.
    aws_region : str:
        AWS Region used for Amazon SES.
    """
    def __init__(
        self,
        message: Message,
        aws_access_key: str,
        aws_secret_key: str,
        aws_region: str = "us-east-1"
    ):
        assert aws_region in AWS_REGIONS, 'not a valid `aws_region`'
        self.client = client(
            'ses',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=aws_region
        )
        self.message = message

    def __repr__(self):
        return f"<SimpleEmailService ({self.message})>"

    def send_email(self):
        """Sends email using AWS `boto3.client.send_email` for SES."""

        payload = self.message.ses_send_email_payload

        try:
            # try to send the email
            response = self.client.send_email(**payload)
        except ClientError as e:
            # raise error on connectivity or payload failure
            raise e

        return response