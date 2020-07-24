from arbitrage.public_markets._huobipro import Huobipro


class HuobiproUSDT(Huobipro):
    def __init__(self):
        super().__init__("USD", "btc_usdt")
