"""Message encapsulation."""

from typing import Dict, List, Union


class Message:
    """Class to encapsulate all email message related elements.

    Attributes
    ----------
    sender : str
        The email address that is sending the email.
    to : list
        The destination for this email.
    subject : str
        The subject of the message.
    reply_to : list
        If the recipient replies to the message, each reply-to address will
        receive the reply.
    body_text : str
        The message body in plaintext.
    body_html : str
        The message body in HTML.
    attachments : list
        List of absolute filepaths to attach.
    cc : list
        The recipients to place on the CC.
    bcc : list
        The recipients to place on the BCC.
    charset : str
        The character set of the content.
    tags : list
        Tags correspond to characteristics of the email that you define.
    """
    def __init__(
        self,
        sender: str,
        to: Union[str, List[str]],
        subject: str,
        reply_to: Union[str, List[str]],
        body_text: str = '',
        body_html: str = '',
        attachments: Union[str, List[str]] = [],
        cc: Union[str, List[str]] = [],
        bcc: Union[str, List[str]] = [],
        charset: str = "UTF-8",
        tags: List[Dict[str, str]] = []
    ):
        self.sender = sender
        self.to = to if isinstance(to, list) else [to]
        self.subject = subject
        self.reply_to = reply_to if isinstance(reply_to, list) else [reply_to]
        self.body_text = body_text
        self.body_html = body_html
        self.attachments = attachments if isinstance(attachments, list) else [attachments]
        self.cc = cc if isinstance(cc, list) else [cc]
        self.bcc = bcc if isinstance(bcc, list) else [bcc]
        self.charset = charset
        self.tags = tags

    @property
    def ses_send_email_payload(self):
        """Property converting attributes to AWS SES configuration."""

        # Payload kwargs for `boto3.client.send_email` method
        # See: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ses.html#SES.Client.send_email
        payload = {
            "Source": self.sender,
            "Destination": {
                "ToAddresses": self.to,
                "CcAddresses": self.cc,
                "BccAddresses": self.bcc
            },
            "Message": {
                "Subject": {
                    "Data": self.subject,
                    "Charset": self.charset
                },
                "Body": {
                    "Text": {
                        "Data": self.body_text,
                        "Charset": self.charset
                    },
                    "Html": {
                        "Data": self.body_html,
                        "Charset": self.charset
                    }
                }
            },
            "ReplyToAddresses": self.reply_to,
            "Tags": self.tags
        }

        return payload

    @property
    def ses_send_raw_email_payload(self):
        pass

