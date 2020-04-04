"""
Amazon Simple Email Service (SES) wrapper class.

Example:
https://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-using-sdk-python.html
"""

from boto3 import client
from botocore.exceptions import ClientError

from betfund_solicitor import Message
from betfund_solicitor.constants import AWS_REGIONS


class SimpleEmailService:
    """Class for handling Amazon SES operations.

    See: https://boto3.amazonaws.com/v1/documentation/

    Attributes
    ----------
    client : `boto3.client`
        Client to connect to Amazon Web Services.
    message : `betfund_solicitor.Message`
        Message object handling encapsulation for desired email.
    """

    def __init__(
        self,
        message: Message,
        aws_access_key: str,
        aws_secret_key: str,
        aws_region: str = "us-east-1",
    ):
        """SimpleEmailService initialization.

        Params
        ------
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
        if not aws_region in AWS_REGIONS:
            raise ValueError(f"`{aws_region}` not a valid region")
        self.client = client(
            "ses",
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=aws_region,
        )
        self.message = message

    def __repr__(self):
        return f"<SimpleEmailService ({self.message})>"

    def send_email(self):
        """Sends email using AWS `boto3.client.send_email` for SES.

        Returns
        -------
        dict
            JSON response from `boto3.client.send_email` representing
            successful email send or notifying payload errors.
        """

        payload = self.message.ses_send_email_payload

        try:
            # try to send the email
            response = self.client.send_email(**payload)
        except ClientError as error:
            # raise error on client connectivity failure
            raise error

        return response
