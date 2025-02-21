import os
from web3 import Web3

def getWeb3Provider(network:str):
    try:
        print(f"Chain Provided as input is {network}")
        lowerCaseNetwork = network.lower()
        if not lowerCaseNetwork:
            httpProvider =  os.getenv('PROVIDER_ETH_MAINNET_URL')
            web3Provider = Web3(Web3.HTTPProvider(httpProvider))
            return [web3Provider,"0x1","Ethereum Mainnet"]
        elif lowerCaseNetwork=="ethereum mainnet" or lowerCaseNetwork=="eth" or lowerCaseNetwork=="eth-mainnet" or lowerCaseNetwork=="eth chain" or network=="ETH Mainnet":
            httpProvider =  os.getenv('PROVIDER_ETH_MAINNET_URL')
            web3Provider = Web3(Web3.HTTPProvider(httpProvider))
            return [web3Provider,"0x1","Ethereum Mainnet"]
        elif lowerCaseNetwork=="polygon mainnet" or lowerCaseNetwork=="polygon" or lowerCaseNetwork=="poly-mainnet" or lowerCaseNetwork=="matic chain" or lowerCaseNetwork=="polygon matic" or lowerCaseNetwork=="polygon-matic":
            httpProvider =  os.getenv('PROVIDER_POLYGON_POS_MAINNET_URL')
            web3Provider = Web3(Web3.HTTPProvider(httpProvider))
            return [web3Provider,"0x89","Polygon Mainnet"]
        elif lowerCaseNetwork=="arbitrum mainnet" or lowerCaseNetwork=="arbitrum" or lowerCaseNetwork=="arb-mainnet" or lowerCaseNetwork=="arbitrum chain" or lowerCaseNetwork=="arb" or lowerCaseNetwork=="arbitrum-mainnet" or lowerCaseNetwork=="arbitrum-one" or lowerCaseNetwork=="arb-one" or lowerCaseNetwork=="arbitrum one":
            httpProvider =  os.getenv('PROVIDER_ARBITRUM_MAINNET_URL')
            web3Provider = Web3(Web3.HTTPProvider(httpProvider))
            return [web3Provider,"0xa4b1","Arbitrum One"]
        elif lowerCaseNetwork=="zksync" or lowerCaseNetwork=="zksync mainnet" or lowerCaseNetwork=="zksync-mainnet" or lowerCaseNetwork=="zksync rollup" or lowerCaseNetwork=="zksync" or lowerCaseNetwork=="zk sync":
            httpProvider =  os.getenv('PROVIDER_ZKSYNC_MAINNET_URL')
            web3Provider = Web3(Web3.HTTPProvider(httpProvider))
            return [web3Provider,"0x144","zkSync Mainnet"]
        elif lowerCaseNetwork=="optimism" or lowerCaseNetwork=="optimism mainnet" or lowerCaseNetwork=="op mainnet" or lowerCaseNetwork=="op-main" or lowerCaseNetwork=="op" :
            httpProvider =  os.getenv('PROVIDER_OPTIMISM_MAINNET_URL')
            web3Provider = Web3(Web3.HTTPProvider(httpProvider))
            return [web3Provider,"0xa","Optimism Mainnet"]
        elif lowerCaseNetwork=="fantom" or lowerCaseNetwork=="fantom-opera" or lowerCaseNetwork=="fantom opera mainnet" or lowerCaseNetwork=="fantom mainnet" or lowerCaseNetwork=="fantom opera" :
            httpProvider =  os.getenv('PROVIDER_FANTOM_OPERA_MAINNET_URL')
            web3Provider = Web3(Web3.HTTPProvider(httpProvider))
            return [web3Provider,"0xfa","Fantom Opera Mainnet"]
        elif lowerCaseNetwork=="mantle" or lowerCaseNetwork=="mantle-mainnet" or lowerCaseNetwork=="mantle mainnet" or lowerCaseNetwork=="mnt" or lowerCaseNetwork=="mnt mainnet" or lowerCaseNetwork=="mnt-mainnet":
            httpProvider =  os.getenv('PROVIDER_MANTLE_MAINNET_URL')
            web3Provider = Web3(Web3.HTTPProvider(httpProvider))
            return [web3Provider,"0x1388","Mantle Mainnet"]
        elif lowerCaseNetwork=="base" or lowerCaseNetwork=="base-mainnet" or lowerCaseNetwork=="base mainnet":
            httpProvider =  os.getenv('PROVIDER_BASE_MAINNET_URL')
            web3Provider = Web3(Web3.HTTPProvider(httpProvider))
            return [web3Provider,"0x2105","Base Mainnet"]
        else:
            httpProvider =  os.getenv('PROVIDER_ETH_MAINNET_URL')
            web3Provider = Web3(Web3.HTTPProvider(httpProvider))
            return [web3Provider,"0x1","Ethereum Mainnet"]
    except:
        print("Some unexpected error in fetching provider")
        return "Some unexpected error in fetching provider"