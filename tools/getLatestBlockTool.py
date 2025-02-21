from ..tools.web3commonutils import getWeb3Provider

def getLatestBlockTool(network):
    try:
        print(f"Chain Provided as input is {network}")
        response = getWeb3Provider(network)
        web3Provider = response[0]
        chainId = response[1]
        networkName = response[2]
        blockNumber = web3Provider.eth.block_number
        stringResp = f"The Current Block number for {networkName} ({chainId}) is {blockNumber}"
        return stringResp
    except:
        print("Some unexpected error in getting chain")
        return "Some unexpected error in getting chain"
