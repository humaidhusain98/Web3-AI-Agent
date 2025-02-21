from ..tools.web3commonutils import getWeb3Provider

def getWalletBalance(*args):
    try:
        print(args)
        argsSplit = args[0].split(",")
        print(argsSplit)
        network = argsSplit[0].strip()
        address = argsSplit[1].strip()
        print(f"Chain Provided as input is {network}")
        response = getWeb3Provider(network)
        web3Provider = response[0]
        chainId = response[1]
        networkName = response[2]
        balance = web3Provider.eth.get_balance(address)
        balanceInEth = web3Provider.from_wei(balance,'ether')
        stringResp = f"The Balance of {address} for {networkName} ({chainId}) is {balanceInEth} Ether"
        print(stringResp)
        return stringResp
    except:
        print("Some unexpected error in getting chain")
        return "Some unexpected error in getting chain"
