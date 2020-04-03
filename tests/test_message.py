"""Unit tests for `lines.snapshot` modules."""
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
            body_text="TextTest",
            body_html="",
        )

        # register basic payload
        self.ses_send_email_payload = rjson(
            "tests/payloads/ses_send_email_payload_basic.json"
        )

        # register basic jsonschema
        self.ses_send_email_schema = rjson(
            "tests/schemas/ses_send_email_schema_basic.json"
        )

    def test_constructor(self):
        """Unit test for `Message.__init__(...)` success."""
        assert self.message.reason == "test"
        assert self.message.sender == "mitchbregs@gmail.com"
        assert self.message.to == ["leonkozlowski@gmail.com"]
        assert self.message.subject == "SubjectTest"
        assert self.message.body_text == "TextTest"
        assert self.message.body_html == ""

    def test_ses_send_email_payload(self):
        """Unit test for `Message.__init__(...)` success."""
        pass

    def test_ses_send_email_jsonschema(self):
        """Unit test for `Message.ses_send_email_payload` success."""

        # use `jsonschema.validate` to assert that payload has proper typing
        validate(
            instance=self.message.ses_send_email_payload,
            schema=self.ses_send_email_schema,
        )
