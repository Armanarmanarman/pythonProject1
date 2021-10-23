from pycoingecko import CoinGeckoAPI

CoinGeckoAPI = CoinGeckoAPI()
s = CoinGeckoAPI.get_coins_markets(vs_currency='usd')
filterRange = int(input())
for i in range(filterRange):
    print(s[i]['market_cap'])
