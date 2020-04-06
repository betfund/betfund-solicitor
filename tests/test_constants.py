"""Unit tests for `betfund_solicitor.constants` module."""
import json
import pytest

from unittest import TestCase

from betfund_solicitor.constants import AWS_REGIONS


def rjson(filepath):
    return json.loads(open(filepath).read())


class TestConstants(TestCase):
    """Tests for `betund_solicitor.constants.AWS_REGIONS`."""

    def setUp(self) -> None:

        # initialize AWS Regions set
        self.aws_regions = AWS_REGIONS

        # load AWS constants JSON
        self.aws_regions_json = rjson("tests/constants/aws_region_constants.json")

    def test_aws_regions_constant(self):
        """Unit test for to ensure AWS Regions are properly constant."""
        assert self.aws_regions == set(self.aws_regions_json)
