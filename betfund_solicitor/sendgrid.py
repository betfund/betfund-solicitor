"""SendGrid V3 API wrapper class."""

from python_http_client.exceptions import BadRequestsError
from sendgrid import SendGridAPIClient

from betfund_solicitor import Message


class SendGrid:
    """Class for handling SendGrid email operations.

    See: https://github.com/sendgrid/sendgrid-python

    Attributes
    ----------
    client : `sendgrid.SendGridAPIClient`
        Client to connect to SendGrid API.
    message : `betfund_solicitor.Message`
        Message object handling encapsulation for desired email.
    """

    def __init__(self, message: Message, sendgrid_api_key: str):
        """SendGrid initialization.

        Params
        ------
        message : `betfund_solicitor.Message`
            Message object handling encapsulation for desired email.
        sendgrid_api_key : str
            Credentials to connect to SendGrid API.
        """
        self.client = SendGridAPIClient(api_key=sendgrid_api_key)
        self.message = message

    def __repr__(self):
        return f"<SendGrid ({self.message})>"

    def send(self):
        """Sends email using `sendgrid.SendGridAPIClient.mail.send.post`.

        Returns
        -------
        dict
            JSON response from `sendgrid.SendGridAPIClient.mail.send.post`
            representing successful email send or notifying payload errors.

        Raises
        ------
        `python_http_client.exceptions.BedRequestsError`
            Raised if invalid connection arguments to SendGrid API or
            upon passing incomplete parameters to email send request.
        """

        # get sendgrid payload for request
        payload = self.message.sendgrid_send_payload

        try:
            # request to send the email
            response = self.client.client.mail.send.post(request_body=payload)
        except BadRequestsError as error:
            # raise exception on failure
            raise error

        return response
