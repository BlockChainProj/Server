# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.bill_list import BillList  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBillController(BaseTestCase):
    """BillController integration test stubs"""

    def test_bills_get(self):
        """Test case for bills_get

        Get the list of Bills of the current account
        """
        query_string = [('accountAddress', 'accountAddress_example')]
        response = self.client.open(
            '/bills',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
