from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
def getCoins(n):
    coins = cg.get_coins_markets(vs_currency="usd")
    result = sorted(coins, key = lambda coin: coin['current_price'], reverse = True)
    for i in range(n):
        print(result[i]["id"], result[i]["current_price"])
print("Please, input your number")
n = int(input())
getCoins(n)
