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

def SELL(symbol,position_size=0,sell_all=True):
    POS_SIZE = str(position_size)
    if sell_all:
        POS_SIZE = client.get_asset_balance(sym)['free']
    sym = symbol.split("USDT")[0] #BTCUSDT --> BTC
    # 0.00223445 --> [0 , 00223445]
    Interger = POS_SIZE.split(".")[0]
    decimal = POS_SIZE.split(".")[1]
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

def ReceiveSignals(signal_data_dict):
    if signal_data_dict["SIGNALS"] == "buy":
        BUY(symbol=signal_data_dict["SYMBOL"],position_size=signal_data_dict["POSITION_SIZE"])
        return "BUY {} SUCCESS! \nSIZE : {}".format(signal_data_dict["SYMBOL"],signal_data_dict["POSITION_SIZE"])
    
    elif signal_data_dict["SIGNALS"] == "sell":
        SELL(symbol=signal_data_dict["SYMBOL"])
        return "SELL {} SUCCESS".format(signal_data_dict["SYMBOL"])

if __name__ == "__main__":

    data = {'STRATEGY': 'STOCH-RSI', 
    'SYMBOL': 'BTCUSDT', 
    'TIME': '2021-05-01T05:48:43Z', 
    'SIGNALS': 'sell', 
    'POSITION_SIZE': 0.000279}

    msg = ReceiveSignals(signal_data_dict=data)



    # if data["SIGNALS"] == "sell":
    #     print(data["SYMBOL"])
    #     print(data["POSITION_SIZE"])
    #     print("\n" + "SELL NOW")
    
    # else:
    #     print(data["SYMBOL"])
    #     print(data["POSITION_SIZE"])
    #     print("\n" + "BUY NOW")

    #order = BUY(symbol="BTCUSDT",position_size=0.0003)
    # order = SELL(symbol="BTCUSDT")
    # print(order)