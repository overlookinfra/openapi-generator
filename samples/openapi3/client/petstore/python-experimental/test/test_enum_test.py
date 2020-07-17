# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import
import sys
import unittest

import petstore_api
try:
    from petstore_api.model import integer_enum
except ImportError:
    integer_enum = sys.modules[
        'petstore_api.model.integer_enum']
try:
    from petstore_api.model import integer_enum_one_value
except ImportError:
    integer_enum_one_value = sys.modules[
        'petstore_api.model.integer_enum_one_value']
try:
    from petstore_api.model import integer_enum_with_default_value
except ImportError:
    integer_enum_with_default_value = sys.modules[
        'petstore_api.model.integer_enum_with_default_value']
try:
    from petstore_api.model import string_enum
except ImportError:
    string_enum = sys.modules[
        'petstore_api.model.string_enum']
try:
    from petstore_api.model import string_enum_with_default_value
except ImportError:
    string_enum_with_default_value = sys.modules[
        'petstore_api.model.string_enum_with_default_value']
from petstore_api.model.enum_test import EnumTest


class TestEnumTest(unittest.TestCase):
    """EnumTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEnumTest(self):
        """Test EnumTest"""
        # FIXME: construct object with mandatory attributes with example values
        # model = EnumTest()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()