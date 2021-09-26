from pycoingecko import CoinGeckoAPI
import json
cg = CoinGeckoAPI()
def getCoins(n):
    coins = cg.get_coins_markets(vs_currency="usd", order="market_cap_desc", per_page=n, page=1, sparkline="falset")
    return coins
def getCoinsDesc(n):
    coins = cg.get_coins_markets(vs_currency="usd", per_page=n, page=1, sparkline="falset")
    result = sorted(coins, key=lambda coin: coin['current_price'], reverse = True)
    return result  
print("Please, input your number")
n = int(input())
print("-------------------List using Coingecko sorting---------------------")
print(json.dumps(getCoins(n), indent=2))
print("-------------------List using python sorting------------------------")
print(json.dumps(getCoinsDesc(n), indent=2))
