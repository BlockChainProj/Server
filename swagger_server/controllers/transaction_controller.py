import connexion
import six

from swagger_server.models.finace_bill import FinaceBill  # noqa: E501
from swagger_server.models.issue_bill import IssueBill  # noqa: E501
from swagger_server.models.settle_bill import SettleBill  # noqa: E501
from swagger_server.models.state import State  # noqa: E501
from swagger_server.models.transfer_bill import TransferBill  # noqa: E501
from swagger_server import util


def finace_post(finaceBill=None):  # noqa: E501
    """Finace a bill

     # noqa: E501

    :param finaceBill: 
    :type finaceBill: dict | bytes

    :rtype: State
    """
    if connexion.request.is_json:
        finaceBill = FinaceBill.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def issue_post(issueBill=None):  # noqa: E501
    """Issue a transaction

     # noqa: E501

    :param issueBill: 
    :type issueBill: dict | bytes

    :rtype: State
    """
    if connexion.request.is_json:
        issueBill = IssueBill.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def settle_post(settleBill=None):  # noqa: E501
    """settle a bill

     # noqa: E501

    :param settleBill: 
    :type settleBill: dict | bytes

    :rtype: State
    """
    if connexion.request.is_json:
        settleBill = SettleBill.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def transfer_post(transferBill=None):  # noqa: E501
    """Transfer a bill

     # noqa: E501

    :param transferBill: 
    :type transferBill: dict | bytes

    :rtype: State
    """
    if connexion.request.is_json:
        transferBill = TransferBill.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
