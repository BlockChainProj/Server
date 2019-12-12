import connexion
import six

from swagger_server.models.bill_list import BillList  # noqa: E501
from swagger_server import util


def bills_get(accountAddress):  # noqa: E501
    """Get the list of Bills of the current account

     # noqa: E501

    :param accountAddress: the corresponding account&#39;s address
    :type accountAddress: str

    :rtype: BillList
    """
    return 'do some magic!'
