# getCryptoPrices
Get the latest Cryptocurrency prices from CoinGecko and define the number of days to go back, to fetch top-performing 100 cryptocurrencies.

## How this script works?
- Define the number of days to search for the top-performing cryptocurrencies.
- The script uses the [CoinGecko](https://api.coingecko.com/api/v3/coins/markets) website, to access the latest prices.
- The results will be displayed using a pretty table and the resulting fields will be: Name, Symbol, Public Key, Hash and Price (USD).

## Preparation
- Install the following libraries:
```bash
pip3 install requests, hashlib, datetime, timedelta, prettytable
```

- Change the number of days you wish to use to go back t fetch top-performing 100 cryptocurrencies (eg. days_back = 30)


## Permissions

Ensure you give the script permissions to execute. Do the following from the terminal:
```bash
sudo chmod +x getCryptoPrices.py
```

## Usage
```bash
sudo python3 getCryptoPrices.py
```

## Typical response
```
+--------------------+--------+--------------------+------------------------------------------------------------------+--------------+
|        Name        | Symbol |     Public Key     |                               Hash                               | Price (USD)  |
+--------------------+--------+--------------------+------------------------------------------------------------------+--------------+
|      Bitcoin       |  BTC   |      bitcoin       | 6b88c087247aa2f07ee1c5956b8e1a9f4c7f892a70e324f1bb3d161e05ca107b |    $27313    |
|      Ethereum      |  ETH   |      ethereum      | b60d7bdd334cd3768d43f14a05c7fe7e886ba5bcb77e1064530052fed1a3f145 |   $1776.08   |
|       Tether       |  USDT  |       tether       | 3dc7089d175e3fa1640f29917f3ae503c7f6919a9a0f80aac383eb2fcbd40daf |    $1.001    |
|        BNB         |  BNB   |    binancecoin     | b3b83d263a9e9898cf719285fb5acd74984c30cbc09799359987c2532b5cf231 |   $313.51    |
|      USD Coin      |  USDC  |      usd-coin      | 230ff45bb8b702d203d98bf1b5a6ef6b645749eb5708810edaac7e2d33c7ce10 |    $1.001    |
|        XRP         |  XRP   |       ripple       | 591b66b11758731f2d661ed864bab0ee82ad13ec6bb99c9abc9444bc91f647d6 |  $0.520894   |
|      Cardano       |  ADA   |      cardano       | 56549e77eb4bb62fe378c57674ff16251b7b5eb2ed4537a7ba0be67cb18da1cd |  $0.369561   |
| Lido Staked Ether  | STETH  |    staked-ether    | c3c6c49b3300c5fc913d85183f8e346deacccb21393306009326bddd5f91566d |   $1772.22   |
|      Dogecoin      |  DOGE  |      dogecoin      | 8b47e3b9448f0b72d9f12aa41ee5ca5754fe05f21cc8c521b5f6bdf6a507b36f |  $0.074107   |
|      Polygon       | MATIC  |   matic-network    | af489dfd066751d74fe2a27886b61c870e8951d768f78ee7103570a0d2eaef9f |    $1.089    |
|       Solana       |  SOL   |       solana       | 615666dae9d3625adaef933e4c1ed0158f657a22c2f570edcd1f7caa68e16413 |    $20.51    |
|    Binance USD     |  BUSD  |    binance-usd     | b275af9a445790165443549d0d78a6f77502663146f4fcb69c32630d882eb52f |    $1.001    |
|      Polkadot      |  DOT   |      polkadot      | bfeb3d7f31acf7a43be1ea47546cf3095c643e6f73680612f872659b3f107895 |    $6.07     |
|      Litecoin      |  LTC   |      litecoin      | 6ce9fe4549f0f60d6fcc7697681ec2e6ed2eade066c3f6829628a59ce5cfc64b |    $89.36    |
|     Shiba Inu      |  SHIB  |     shiba-inu      | 31eadc22d26e36169b96b30cbcf9c40b8d8616e3c3d81e79dea316ce54fdd3ea |  $1.048e-05  |
|        TRON        |  TRX   |        tron        | 3ecf001753640fa58a06d5515fa610388a4f1722647d5f9f8abe76e4ed8a61f9 |  $0.064298   |
|     Avalanche      |  AVAX  |    avalanche-2     | c30db6e86cd3d7f55b4baabe5915f75a47035b4df3881c37454856550e16b56c |    $16.75    |
|        Dai         |  DAI   |        dai         | 4de6bb4e4a6c2058981c96726e7142bc487588eadf7f315b1d7dc56e30cc51aa |     $1.0     |
|      Uniswap       |  UNI   |      uniswap       | 0cb888d14a26697c116689ec90a252163136239564639c051971d681a7d80dac |    $5.84     |
|  Wrapped Bitcoin   |  WBTC  |  wrapped-bitcoin   | a64aeaae38158b7a05e184266abda2a00c6be2daaaee8d650fc1b3b2dd40312b |    $27326    |
|     Chainlink      |  LINK  |     chainlink      | b4bfe090fdd6cdf453b0c961c5cde06a23a5e401e90028225860d0c8b5578c4c |    $6.97     |
|     Cosmos Hub     |  ATOM  |       cosmos       | 4cbe19716b1aa73a67dc4b28c34391879b503259fc76852082b4dafcf0de85b2 |    $11.25    |
|     LEO Token      |  LEO   |     leo-token      | 9dd75629e9b73349b4921c589e0927bce36a62e10f2eea72999b0634e422e26f |    $3.41     |
|      Toncoin       |  TON   |  the-open-network  | 68655b987763a359e8b6a734514cffc729dd9a460a88713305c657717db7b414 |    $2.11     |
|  Ethereum Classic  |  ETC   |  ethereum-classic  | f80cc5c027cf58b8d2dd5f8253d23693210de7bf6db758cc1dae49770552d12a |    $20.21    |
|       Monero       |  XMR   |       monero       | 4469412a3887c4b146059ec7f86cd06d0da86bfa5748df1256e463164a0797f7 |   $154.06    |
|      Stellar       |  XLM   |      stellar       | 232ed6f9fabf14e3bb55392b18cfe3d0febc94d20cc6327c38a1d075d6ea118c |   $0.09828   |
|        OKB         |  OKB   |        okb         | 83f0df418546f5a402c4b0b7cd92de59f5493bf9fa0fec3bcef337e1292d82e9 |    $42.9     |
|    Bitcoin Cash    |  BCH   |    bitcoin-cash    | b792ab9c8670666155bc7dba740440c24e488d9e86a7c3ddf52e4a2d73248b3b |   $121.15    |
|      Filecoin      |  FIL   |      filecoin      | 5457f5097e288148400af5e26af86a9dfedf96fecd41479401e40445890856e4 |    $5.57     |
|      TrueUSD       |  TUSD  |      true-usd      | f459d01d242d35d4e421c74014a981aadfc25b064c588c0a8c091eba2c0b8350 |    $1.001    |
|       Aptos        |  APT   |       aptos        | 83ca6d000a92893befe216e3bbc268d9df623fb3d822c6e72f5111e95e15f942 |    $11.27    |
|      Lido DAO      |  LDO   |      lido-dao      | daf2bc7e694dc896e47a88c464141b30c48b8c806e5fd9a829e84060fb5d0ee7 |    $2.33     |
|       Hedera       |  HBAR  |  hedera-hashgraph  | 889709f06d06d083f1709f49eac6c78bc48482087efe6aa933e8de5ea07921dc |  $0.059781   |
|       Quant        |  QNT   |   quant-network    | 71818d0a9bf4211a7da1cb8c339638dd3b16f9244939fd8a73f216b9766c7597 |   $121.35    |
|       Cronos       |  CRO   |  crypto-com-chain  | bc9e381330222bf8e8a804649764e476f6ef0d2510662360103f364d827e477f |  $0.067353   |
|   NEAR Protocol    |  NEAR  |        near        | 46ba34770bccfde756708d47d83fb7c8257fe8a4b3a35f25d385a8284021f476 |    $1.89     |
|      VeChain       |  VET   |      vechain       | 4921fb4bbc1c4360efdbbdd69cf55b463703b50cb32d0dbb8a463721a6e4af20 |  $0.0225075  |
|      Arbitrum      |  ARB   |      arbitrum      | 143b9b70edf76467d576ad45e2efa5cfbacb2c63bf0f3ed9bcb8c9f17adcb89e |    $1.22     |
|      ApeCoin       |  APE   |      apecoin       | 0c09a24f67546248b2340585f298c34e2bbd5e0535e52032055e8690ce1ed422 |    $4.09     |
|      Algorand      |  ALGO  |      algorand      | df8e966c94469b23598aafaee6c14463ad40dc6286babad3096cb413979a8116 |  $0.203572   |
| Internet Computer  |  ICP   | internet-computer  | 18d4edafb9dffd185810161c9361c3bc5d63c12f60ea0652feae95b816bd8d94 |    $4.85     |
|       Stacks       |  STX   |     blockstack     | 355e3c7fe5067ff07c04739f892085bd3ff235f4d5a67762a0d3c468536f0c10 |   $0.9472    |
|     The Graph      |  GRT   |     the-graph      | 7d06ae394b3061470b4f9be56045a62c40a8def47b00995fa465f7ac7e660f8b |  $0.140463   |
|        EOS         |  EOS   |        eos         | 16149626b0365e04a9a52d02e17ca8aeb63680b9f5ee2ba334b0b1a38a833cfe |    $1.12     |
|       Fantom       |  FTM   |       fantom       | 684603a7e7eae5bac769334a169067ece3d969d108b5a2b3bfa78b0bb3461ef6 |   $0.42283   |
|    The Sandbox     |  SAND  |    the-sandbox     | b5127f74421e669a5edb404bcb2a3f8cd0df1c84d4d2fd47ec51bb293a3eeab2 |  $0.617252   |
|     MultiversX     |  EGLD  |    elrond-erd-2    | de75c84e31b08a5289587933308c2f6b4ff9e882e449da5600ffa4ed64258a6a |    $42.23    |
|    Decentraland    |  MANA  |    decentraland    | e4c81f0b9fe9cab127657f6246445de2a7a0268c2d59e42216ab232782053fdd |   $0.57768   |
|        Frax        |  FRAX  |        frax        | 50779838c1d45a29013eb9a206ff36975ed0a019557ddcf091e1c28c9c0a63e9 |    $1.001    |
|        Aave        |  AAVE  |        aave        | 1a11bddc4396ca460d2996b1a1bc6ee02477089fe30b514532bb72dad42789e2 |    $70.73    |
|       Tezos        |  XTZ   |       tezos        | afefb91b38561ce4c5ed9f03d31ba2e93d8d878f6d2817a2851641fbdd290343 |    $1.095    |
|        Flow        |  FLOW  |        flow        | 3b21278178ed3463f3bde3a35f088caf6d99ff1b2f647d9a0c2b8de599ec3dc6 |  $0.939379   |
|   Theta Network    | THETA  |    theta-token     | 36b2d14669ae82e29e7d50a6321dba895cccb1c479d565a3bf4013de6eb60e4b |   $0.97627   |
|     ImmutableX     |  IMX   |    immutable-x     | c764a760f04a5229db26359097bc418ded5e668abcda741f91b84adaea69ff92 |    $1.065    |
|   Axie Infinity    |  AXS   |   axie-infinity    | 0571d17b8b35ee278f72082e3d0ff1bd026d22606db2a2786304fd730d4d4879 |    $8.26     |
|        NEO         |  NEO   |        neo         | 73ef176d9f12809e64363b2b5f4553abecca7aae157327f190323cfa0e42c815 |    $12.66    |
|    Rocket Pool     |  RPL   |    rocket-pool     | 8c234699fb33ed73f276b2f66dd92f29ebef6828d7f8852bd033eac114a9b121 |    $45.81    |
|       KuCoin       |  KCS   |   kucoin-shares    | 1798a0a2c5a2ab5372b83acf045bd2597397093b96a3fd6d657faf97ccc71f89 |    $8.32     |
|     Pax Dollar     |  USDP  |   paxos-standard   | ced75b3f3b6375033a13efa99d8703c9802f4c34e6d3221c5e82c94faeb2b353 |     $1.0     |
| Synthetix Network  |  SNX   |       havven       | be2479085d4e691cf61cfd8402c722a812011a6008a93cc95e01d9c15c50a0b6 |    $2.39     |
|       BitDAO       |  BIT   |       bitdao       | 6b91300551f305600fcb4c90472a8c8a5528bb425bdc117445cd2d638c41c449 |  $0.521373   |
|      Conflux       |  CFX   |   conflux-token    | 900d62f38001c17b58992240c99fe6e3e54c6ab845ad89e73f29e64e48bc3077 |  $0.352822   |
|   WhiteBIT Token   |  WBT   |      whitebit      | a5847b472f6f6a0723f789c59f88fbb839cf63ff6c5fb06813c6e74f7c0ff544 |    $5.06     |
| Terra Luna Classic |  LUNC  |     terra-luna     | d2c593a7e940a8477a381a3c56e6ebb051ea7e57ccdc98b35406a0d373070cf1 | $0.00012195  |
|        USDD        |  USDD  |        usdd        | 167936b6e1723df4f7a4f72024955730cbfd317495fd498cc661a7bc0d9f6cac |  $0.989742   |
|     Curve DAO      |  CRV   |  curve-dao-token   | 07e4a6904f7a1855a473c08092420d480e2a1ef6aa9acf705bdc3e48d2923384 |  $0.922325   |
|       Klaytn       |  KLAY  |     klay-token     | e548a82372072d34fabd680bcad2d5d5a210de70b4ccd917fb1bc2eb88c61dfb |  $0.228526   |
|        Gate        |   GT   |  gatechain-token   | 9174768797d7012fa34767baf9ab930d5d90632699835a67bead498beecd3589 |    $4.98     |
|      Optimism      |   OP   |      optimism      | c9c3722d768c33938b0a250c9e252ae33021f52d40e5e95ac3edd1355501274e |     $2.2     |
|     Bitcoin SV     |  BSV   |  bitcoin-cash-sv   | 7c3d3e554f2eae2d37a1bf21645f46600f2e3077756b722e0a02c11d3795c3db |    $35.42    |
|        GMX         |  GMX   |        gmx         | 600637a5a091c1aea3dcf5949332fc2ab8b95315d67ce5b557e89590beab3292 |    $78.39    |
|    PancakeSwap     |  CAKE  | pancakeswap-token  | c217d2d0d3f10e09b558cd6faf2836e816c2bfcc1998265b44fd2f1cc1d1ce19 |    $3.63     |
|   Mina Protocol    |  MINA  |   mina-protocol    | 347f2936e40ba817496a61e37d04199842fdecffb101a06db41f2d5ccee43c46 |  $0.752019   |
|        Dash        |  DASH  |        dash        | af9d2c92ddc38ca77b3cd29e944c9b61928032808d3a3cb6c3a3c8965067291e |    $56.76    |
|       Chiliz       |  CHZ   |       chiliz       | 8800378d9667780bdaf980f366a38fb9af564144bf006f206b5ca07c751a04f1 |  $0.115301   |
|       Maker        |  MKR   |       maker        | 878c240fd717f39d8cec9f7a5cf936873ffcc0757beef703ad2c5f9ed1890344 |   $674.41    |
|       Huobi        |   HT   |    huobi-token     | 54ffc9bfbac5f2d3decef45348201ee344b5757cd4680407a21379774eb38ee3 |    $3.62     |
|     BitTorrent     |  BTT   |     bittorrent     | 5b2ceea968caeccf29f1eb627775c7c2afcbedc4131b5450df9fab5bd87867d1 | $6.14348e-07 |
|       eCash        |  XEC   |       ecash        | 7a19351163e74265dc96db0ef6a0ae8a2ff1775fb707dd94979f113f5badc479 |  $3.005e-05  |
|     Frax Share     |  FXS   |     frax-share     | 2752aacf94971698bb4af3db8ffe8c7b1cb6017067379be552eb3085917c6a16 |    $8.06     |
|        IOTA        | MIOTA  |        iota        | 9604832cb6e918585fe94b71b9aadb332f43e28a0fca596fbd262c8943f5f754 |  $0.204804   |
|    XDC Network     |  XDC   |  xdce-crowd-sale   | d4ec13a9cb4c4b5838f4c3056f0cb571858d749306ea1f38caa64ec44d895fec | $0.04050283  |
|    Bitget Token    |  BGB   |    bitget-token    | 8c8fff93432839ba85d37b67664981d80cfe90221b0562ea743b4acb382fa080 |  $0.392427   |
|        cETH        |  CETH  |   compound-ether   | a9755775b7e27b700cde4781a67f25c248eeb7dc6f5c2f284f046a7bd1cd2b7c |    $35.67    |
|      Edgecoin      |  EDGT  |     edgecoin-2     | 488abb7032956b0b32407f547fdb5ae29b826c7c794bfd67be7d9af8accdcfd8 |    $1.001    |
|       Flare        |  FLR   |   flare-networks   | 8b01b8528c42dd66db9fe1f3f2dfe9bca88c6c9958c3cb3467e4827c3e47eba8 |  $0.0418046  |
|      PAX Gold      |  PAXG  |      pax-gold      | cb392729e3a7d784c5a78d50d30b26750f150f0d2baf328743b89dabde90aa12 |   $1985.21   |
|   SingularityNET   |  AGIX  |   singularitynet   | b149514c4fe7af449de0c1a333ccde4016fd80c493dd12d6c25b1d04d3e2930b |  $0.419054   |
|    Mask Network    |  MASK  |    mask-network    | 1d586beb2e3febca06134f50cd3bf96c2efb1b3fe0ae25bb9b6d97e73e09aef8 |    $6.63     |
|  Tokenize Xchange  |  TKX   |  tokenize-xchange  | e41ca53d53db9d7fc53b52b38c99513e6ca4c36b8dbb141697c4034ef7408e19 |    $6.29     |
|    Tether Gold     |  XAUT  |    tether-gold     | 7afa32b0153a157932e7e2d5acd39670d704f2478008151356f8c17fd8753b0c |   $1979.55   |
|    Trust Wallet    |  TWT   | trust-wallet-token | fc37fa0d035f2863f4ae275b0af9eff084b09f047f19a82af41082a030d71f49 |    $1.13     |
|       cUSDC        | CUSDC  | compound-usd-coin  | dfdb2c84553907a9fb4544d5e8e82114e5064b35a5d32ce125d2c3d3e94129f1 | $0.02282195  |
|      Zilliqa       |  ZIL   |      zilliqa       | 7b5b858fae45e43d3b9004a2bd8736f040fafe1f83043dbe738eb81c4996e88f | $0.02751202  |
|      Osmosis       |  OSMO  |      osmosis       | a08ebfb6519e8d814f1b8aee62da9a4e173f7e6898d60d962042421d18dbe4ef |  $0.802122   |
|      Loopring      |  LRC   |      loopring      | ff7514688fb75ceeff5a142e648e0b1871e98ad78e075594e624bc73bd051eb9 |  $0.349937   |
|       Render       |  RNDR  |    render-token    | 50dbacb51329cf4b04603d621aa21a073fae89045520874aa25042ffa633abed |    $1.18     |
|       1inch        | 1INCH  |       1inch        | e679fb124222495c115219233a55d638c5557995daf3cced10b5cff8ff60a731 |  $0.499302   |
|       Radix        |  XRD   |       radix        | da7f85eaf3d0452479031da124d28778aaf15cc756a6c909d7dc708fade343f0 | $0.04069562  |
+--------------------+--------+--------------------+------------------------------------------------------------------+--------------+
```

## Sample script
```python
import requests
import hashlib
from datetime import datetime, timedelta
from prettytable import PrettyTable

# Define the number of days to go back to fetch top-performing cryptocurrencies
days_back = 30

# Calculate the date for the start of the period to fetch data for
start_date = (datetime.now() - timedelta(days=days_back)).strftime('%d-%m-%Y')

# Define the API endpoint and parameters for fetching top-performing cryptocurrencies
top_url = 'https://api.coingecko.com/api/v3/coins/markets'
top_params = {'vs_currency': 'usd', 'order': 'market_cap_desc', 'per_page': 100, 'page': 1, 'sparkline': 'false', 'date': start_date}

# Fetch the top-performing cryptocurrency data from the API
response = requests.get(top_url, params=top_params)
top_data = response.json()

# Build a list of the top-performing cryptocurrency ids
crypto_list = [crypto['id'] for crypto in top_data]

# Define the API endpoint and parameters for fetching cryptocurrency data
data_url = 'https://api.coingecko.com/api/v3/coins/markets'
data_params = {'vs_currency': 'usd', 'ids': ','.join(crypto_list), 'order': 'market_cap_desc', 'per_page': 100, 'page': 1, 'sparkline': 'false'}

# Define the API endpoint and parameters for fetching public key data
key_url = 'https://api.coingecko.com/api/v3/coins/list'
key_params = {'include_platform': 'false'}

# Fetch the cryptocurrency data from the API
response = requests.get(data_url, params=data_params)
crypto_data = response.json()

# Fetch the public key data from the API
response = requests.get(key_url, params=key_params)
key_data = response.json()

# Build a dictionary of public key hashes for each cryptocurrency
hashes = {}
for key in key_data:
    if key['id'] in crypto_list:
        public_key = key['id']
        public_key_hash = hashlib.sha256(public_key.encode()).hexdigest()
        hashes[public_key] = public_key_hash

# Create a table to display the cryptocurrency data
table = PrettyTable()
table.field_names = ["Name", "Symbol", "Public Key", "Hash", "Price (USD)"]

# Add the cryptocurrency data to the table
for crypto in crypto_data:
    public_key = crypto['id']
    public_key_hash = hashes[public_key]
    table.add_row([crypto['name'], crypto['symbol'].upper(), public_key, public_key_hash, f"${crypto['current_price']}"])

# Print the table
print(table)
```

## License Information

This library is released under the [Creative Commons ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/). You are welcome to use this library for commercial purposes. For attribution, we ask that when you begin to use our code, you email us with a link to the product being created and/or sold. We want bragging rights that we helped (in a very small part) to create your 9th world wonder. We would like the opportunity to feature your work on our homepage.

