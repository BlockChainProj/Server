import connexion
import six

from swagger_server.models.finace_bill import FinaceBill  # noqa: E501
from swagger_server.models.issue_bill import IssueBill  # noqa: E501
from swagger_server.models.settle_bill import SettleBill  # noqa: E501
from swagger_server.models.state import State  # noqa: E501
from swagger_server.models.transfer_bill import TransferBill  # noqa: E501
from swagger_server import util

from client.common import transaction_common
from client.datatype_parser import DatatypeParser

contract_address = "0xc0dcd5c4efe2c832781c9c0f8cb073cada16ef72" #合约地址
contract_dir = "contracts" #合约目录
contract_name = "Supply" #合约名字

accountAddress = "a599d3672309bd85c66aaa67a0ab5dfff4ba4d88"
tx_client = transaction_common.TransactionCommon(
                contract_address, contract_dir, contract_name)

def print_parse_transaction(tx, contractname, parser=None):
    if parser is None:
        parser = DatatypeParser(default_abi_file(contractname))
    inputdata = tx["input"]
    inputdetail = parser.parse_transaction_input(inputdata)
    print("INFO >> transaction hash : ", tx["hash"])
    print("tx input data detail:\n {}".format(inputdetail))
    return (inputdetail)

def default_abi_file(contractname):
    abi_file = contractname
    if not abi_file.endswith(".abi"):  # default from contracts/xxxx.abi,if only input a name
        abi_file = contract_dir + "/" + contractname + ".abi"
    return abi_file

def print_receipt_logs_and_txoutput(client, receipt, contractname, parser=None):
    print("\nINFO >>  receipt logs : ")
    # 解析receipt里的log
    if parser is None and len(contractname) > 0:
        parser = DatatypeParser(default_abi_file(contractname))
    logresult = parser.parse_event_logs(receipt["logs"])
    i = 0
    for log in logresult:
        if 'eventname' in log:
            i = i + 1
            print("{}): log name: {} , data: {}".format(i, log['eventname'], log['eventdata']))
    txhash = receipt["transactionHash"]
    txresponse = client.getTransactionByHash(txhash)
    inputdetail = print_parse_transaction(txresponse, "", parser)
    # 解析该交易在receipt里输出的output,即交易调用的方法的return值
    outputresult = parser.parse_receipt_output(inputdetail['name'], receipt['output'])
    print("receipt output :", outputresult)
    

def finace_post(finaceBill=None):  # noqa: E501
    """Finace a bill

     # noqa: E501

    :param finaceBill: 
    :type finaceBill: dict | bytes

    :rtype: State
    """
    if connexion.request.is_json:
        try:
            finaceBill = FinaceBill.from_dict(connexion.request.get_json())  # noqa: E501
            tx_client = transaction_common.TransactionCommon(
                    contract_address, contract_dir, contract_name)
            fn_args = []
            fn_args.append(int(finaceBill.money))
            fn_args.append(finaceBill.bill_index)
            receipt = tx_client.send_transaction_getReceipt("borrowMoney", fn_args)[0]
            data_parser = DatatypeParser(default_abi_file(contract_name))
            # 解析receipt里的log 和 相关的tx ,output
            print_receipt_logs_and_txoutput(tx_client, receipt, "", data_parser)
        except:
            return False
        else:
            return True


def issue_post(issueBill=None):  # noqa: E501
    """Issue a transaction

     # noqa: E501

    :param issueBill: 
    :type issueBill: dict | bytes

    :rtype: State
    """
    if connexion.request.is_json:
        try:
            issueBill = IssueBill.from_dict(connexion.request.get_json())  # noqa: E501
            tx_client = transaction_common.TransactionCommon(
                    contract_address, contract_dir, contract_name)
            fn_args = []
            fn_args.append(issueBill.lender_key)
            fn_args.append(issueBill.money)
            fn_args.append(issueBill.info)
            receipt = tx_client.send_transaction_getReceipt("buyAndCheck", fn_args)[0]
            data_parser = DatatypeParser(default_abi_file(contract_name))
            # 解析receipt里的log 和 相关的tx ,output
            print_receipt_logs_and_txoutput(tx_client, receipt, "", data_parser)
        except:
            return False
        else:
            return True


def settle_post(settleBill=None):  # noqa: E501
    """settle a bill

     # noqa: E501

    :param settleBill: 
    :type settleBill: dict | bytes

    :rtype: State
    """
    if connexion.request.is_json:
        try:
            settleBill = SettleBill.from_dict(connexion.request.get_json())  # noqa: E501
            tx_client = transaction_common.TransactionCommon(
                    contract_address, contract_dir, contract_name)
            fn_args = []
            fn_args.append(settleBill.bill_index)
            receipt = tx_client.send_transaction_getReceipt("settleCheck", fn_args)[0]
            data_parser = DatatypeParser(default_abi_file(contract_name))
            # 解析receipt里的log 和 相关的tx ,output
            print_receipt_logs_and_txoutput(tx_client, receipt, "", data_parser)
        except:
            return False
        else:
            return True
    


def transfer_post(transferBill=None):  # noqa: E501
    """Transfer a bill

     # noqa: E501

    :param transferBill: 
    :type transferBill: dict | bytes

    :rtype: State
    """
    if connexion.request.is_json:
        try:
            transferBill = TransferBill.from_dict(connexion.request.get_json())  # noqa: E501
            tx_client = transaction_common.TransactionCommon(
                    contract_address, contract_dir, contract_name)
            fn_args = []
            fn_args.append(transferBill.borrower_key)
            fn_args.append(transferBill.new_lender_key)
            fn_args.append(transferBill.money)
            fn_args.append(transferBill.info)
            receipt = tx_client.send_transaction_getReceipt("transferCheck", fn_args)[0]
            data_parser = DatatypeParser(default_abi_file(contract_name))
            # 解析receipt里的log 和 相关的tx ,output
            print_receipt_logs_and_txoutput(tx_client, receipt, "", data_parser)
        except:
            return False
        else:
            return True
