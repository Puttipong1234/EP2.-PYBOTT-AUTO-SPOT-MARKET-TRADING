from BinanceTrade.Trade import client

#info = client.get_account()
#USDT_balance = client.get_asset_balance("USDT")
#print(USDT_balance)

def BUY(symbol,position_size):
    USDT_balance = client.get_asset_balance("USDT")
    if float(USDT_balance['free']) > 10:
        order = client.order_market_buy(
            symbol=symbol,
            quantity=position_size
        )

        return order

    return "เกิดข้อผิดพลาด"

def SELL(symbol):
    sym = symbol.split("USDT")[0] #BTCUSDT --> BTC
    Interger = client.get_asset_balance(sym)['free'].split(".")[0]
    decimal = client.get_asset_balance(sym)['free'].split(".")[-1]
    dec_count = -1

    while True:
        position_size = Interger + "." + decimal[:dec_count]
        if float(position_size) > 0:
            try:
                order = client.order_market_sell(
                    symbol=symbol,
                    quantity=position_size
                )

                return order
            
            except Exception as e:
                if e.code == -1013:
                    dec_count = dec_count - 1

                else :
                    print(e.args)
                    return "เกิดข้อผิดพลาด"

if __name__ == "__main__":
    #order = BUY(symbol="BTCUSDT",position_size=0.00025)
    order = SELL(symbol="BTCUSDT")
    print(order)