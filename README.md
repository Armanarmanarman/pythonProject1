# pythonProject1
This project pulls the date from coingeco.com 
And filters out top N cryptocurrencies by market 
capitalisation
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install pycoingecko
```

## Usage

```python
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
s = cg.get_coins_markets(vs_currency='usd')
n = int(input())
for i in range(n):
    print(s[i]['market_cap'])
```
## Example
Give integer n input in rane 1-100
and it will print out top n cryptocurrencies market capitalisation
