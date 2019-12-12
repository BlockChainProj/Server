# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.finace_bill import FinaceBill  # noqa: E501
from swagger_server.models.issue_bill import IssueBill  # noqa: E501
from swagger_server.models.settle_bill import SettleBill  # noqa: E501
from swagger_server.models.state import State  # noqa: E501
from swagger_server.models.transfer_bill import TransferBill  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTransactionController(BaseTestCase):
    """TransactionController integration test stubs"""

    def test_finace_post(self):
        """Test case for finace_post

        Finace a bill
        """
        finaceBill = FinaceBill()
        response = self.client.open(
            '/finace',
            method='POST',
            data=json.dumps(finaceBill),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_issue_post(self):
        """Test case for issue_post

        Issue a transaction
        """
        issueBill = IssueBill()
        response = self.client.open(
            '/issue',
            method='POST',
            data=json.dumps(issueBill),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_settle_post(self):
        """Test case for settle_post

        settle a bill
        """
        settleBill = SettleBill()
        response = self.client.open(
            '/settle',
            method='POST',
            data=json.dumps(settleBill),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_transfer_post(self):
        """Test case for transfer_post

        Transfer a bill
        """
        transferBill = TransferBill()
        response = self.client.open(
            '/transfer',
            method='POST',
            data=json.dumps(transferBill),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
