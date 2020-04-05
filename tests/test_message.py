"""Unit tests for `betfund_solicitor.Message` modules."""
import json
import pytest

from jsonschema import validate
from unittest import TestCase

from betfund_solicitor import Message


def rjson(filepath):
    return json.loads(open(filepath).read())


class TestBasicMessage(TestCase):
    """Tests for `betund_solicitor.message.Message`."""

    def setUp(self) -> None:

        # instantiate `betfund_solicitor.message.Message` object
        self.message = Message(
            reason="test",
            sender="mitchbregs@gmail.com",
            to="leonkozlowski@gmail.com",
            subject="SubjectTest",
            body_html="TextTest",
        )

        ## Amazon SES
        # register basic payload
        self.ses_send_email_payload = rjson(
            "tests/payloads/ses_send_email_payload_basic.json"
        )
        # register basic jsonschema
        self.ses_send_email_schema = rjson(
            "tests/schemas/ses_send_email_schema_basic.json"
        )

        ## SendGrid
        # register basic payload
        self.sendgrid_send_payload = rjson(
            "tests/payloads/sendgrid_send_payload_basic.json"
        )
        # register basic jsonschema
        self.sendgrid_send_schema = rjson(
            "tests/schemas/sendgrid_send_schema_basic.json"
        )

    def test_constructor(self):
        """Unit test for `Message.__init__(...)` success."""
        assert self.message.reason == "test"
        assert self.message.sender == "mitchbregs@gmail.com"
        assert self.message.to == ["leonkozlowski@gmail.com"]
        assert self.message.subject == "SubjectTest"
        assert self.message.body_html == "TextTest"

    def test_repr(self):
        """Test the object string representation."""
        assert self.message.__repr__() == "<Message `test`>"

    def test_ses_send_email_json_schema(self):
        """Use `jsonschema.validate` to ensure that payload has proper typing"""
        validate(
            instance=self.message.ses_send_email_payload,
            schema=self.ses_send_email_schema,
        )

    def test_ses_send_email_payload(self):
        """Unit test for `Message.ses_send_email_payload` success."""
        assert self.ses_send_email_payload == self.message.ses_send_email_payload

    def test_sendgrid_send_json_schema(self):
        """Use `jsonschema.validate` to ensure that payload has proper typing"""
        validate(
            instance=self.message.sendgrid_send_payload,
            schema=self.sendgrid_send_schema,
        )

    def test_sendgrid_send_payload(self):
        """Unit test for `Message.sendgrid_send_payload` success."""
        assert self.sendgrid_send_payload == self.message.sendgrid_send_payload
