from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
s = cg.get_coins_markets(vs_currency='usd')
n = int(input())
for i in range(n):
    print(s[i]['market_cap'])

