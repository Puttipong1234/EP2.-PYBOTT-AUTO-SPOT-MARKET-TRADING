import threading
import time

from DB.Firebasedb import GetInitialValue , WriteInitialValue
from BinanceTrade.Trade import client

def rebalanceAsset(symbols):
    InitValue = GetInitialValue(symbols) #15

    # เงินต้นเราเท่าไหร่ ? ในครั้งก่อน
    # รู้ว่าเราถือ เท่าไหร่ และ ราคาปัจจุบันเท่าไหร่?

    holding = client.get_asset_balance(asset=symbols)
    CurrentPrice = client.get_avg_price(symbol=symbols + "USDT")
    HoldingUSDT = float(holding["free"]) * float(CurrentPrice["price"])
    
    rebalanceValue = HoldingUSDT - float(InitValue)
    rebalanceSize = float(rebalanceValue/float(CurrentPrice["price"]))
    
    if rebalanceSize > 0:
        print("SELL : " , rebalanceSize)
    
    elif rebalanceSize < 0:
        print("BUY : " , rebalanceSize)
    #function BUY SELL import BinanceTrade

    #CurrentValue = holding*CurrentPrice
    

class RebalanceBot(threading.Thread):

    def __init__(self,interval,coins_list = []):
        self.need_to_break = False
        self.kill_bot = False
        self.coins_list = coins_list
        self.interval = interval
    
    def job(self):

        print("START MORNITORING AND REBALANCING ASSET")

        for coin in self.coins_list:
            # func Rebalance!
            rebalanceAsset(symbols=coin)
            print("REBALANCE {}".format(coin))
    

    def run(self):
        while True:
            if not self.need_to_break and not self.kill_bot:
                print("====START====")
                self.job()
                time.sleep(self.interval)
                print("=============")
            
            elif self.need_to_break and not self.kill_bot:
                print("BOT IS PAUSED NOW")
    
            elif self.kill_bot:
                print("BOT KILLED")
                break
    
    def pause(self):
        self.need_to_break = True
    
    def resume(self):
        self.need_to_break = False
    
    def kill(self):
        self.kill_bot = True
    
    # def addmoresymbols

    # def deletesymbol
