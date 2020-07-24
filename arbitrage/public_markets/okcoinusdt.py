from arbitrage.public_markets._okcoin import OKCoin


class OKCoinUSDT(OKCoin):
    def __init__(self):
        super().__init__("USD", "btc_usdt")
