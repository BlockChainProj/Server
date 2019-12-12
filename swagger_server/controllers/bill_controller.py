import connexion
import six

from swagger_server.models.bill_list import BillList  # noqa: E501
from swagger_server import util

from client import bcosclient as bcos
import json
from client.datatype_parser import DatatypeParser
from client.common import transaction_common



# #找到abi文件
# def default_abi_file(contractname):
#     abi_file = contractname
#     if not abi_file.endswith(".abi"):  # default from contracts/xxxx.abi,if only input a name
#         abi_file = contracts_dir + "/" + contractname + ".abi"
#     return abi_file


# def get_functions_by_contract(contract_name):
#     """
#     get functions according to contract_name
#     """
#     data_parser = DatatypeParser(default_abi_file(contract_name))
#     #return [*data_parser.func_abi_map_by_name.keys()]
#     return [*data_parser.func_abi_map_by_name.keys()]


def bills_get(accountAddress):  # noqa: E501
    """Get the list of Bills of the current account

     # noqa: E501

    :param accountAddress: the corresponding account&#39;s address
    :type accountAddress: str

    :rtype: BillList
    """
    contract_address = "0xc0dcd5c4efe2c832781c9c0f8cb073cada16ef72" #合约地址
    contract_dir = "contracts" #合约目录
    contract_name = "Supply" #合约名字
    accountAddress = "a599d3672309bd85c66aaa67a0ab5dfff4ba4d88"
    tx_client = transaction_common.TransactionCommon(
                contract_address, contract_dir, contract_name)
    res_length = tx_client.call_and_decode("getReceiptLength", [accountAddress])
    length = res_length[0]
    receipt = []
    for i in range(length):
        receipt.append(tx_client.call_and_decode("getReceipt", [accountAddress,str(i)]))
    return receipt
    # myClient = bcos.BcosClient()
    
    # contract_abi_path = contract_dir + "/" + contract_name + ".abi"

    # load_f = open(contract_abi_path, 'r')
    # contract_abi = json.load(load_f)
    # load_f.close()

    # res = myClient.call(contract_address, contract_abi, "getReceipt", ["a599d3672309bd85c66aaa67a0ab5dfff4ba4d88","0"])
    return res
