import client.bcosclient as bcos

client = bcos.BcosClient()
# 调用查节点版本接口
res = client.getNodeVersion()
print("getClientVersion",res)


res = client.getSealerList()
print('getConsensusStatus',res)
# 调用查节点块高接口
try:
    res = client.getBlockNumber()
    print("getBlockNumber",res)
except BcosError as e:
    print("bcos client error,",e.info())
