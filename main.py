from pycoingecko import CoinGeckoAPI

CoinGeckoAPI = CoinGeckoAPI()
s = CoinGeckoAPI.get_coins_markets(vs_currency='usd')
filterRange = int(input())
i =0
while i < filterRange:
    print(s[i]['market_cap_rank'])
    print(s[i]['name'])
    print(s[i]['market_cap'])
    i = i+1