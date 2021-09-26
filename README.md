# py1assignment
# CoinGecko API wrapper
![Build Status](https://github.com/kagesaburo27/py1assignment/workflows/python-app/badge.svg)

Python3 wrapper around the [CoinGecko](https://www.coingecko.com/) API (V3)

### Installation
PyPI
```bash
pip install pycoingecko
```
or from source
```bash
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```

### Usage

```python
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```

**/coins/markets** (List all supported coins price, market cap, volume, and market related data)
    ```python 
    cg.get_coins_markets()
    ```
 ### Examples
The required parameters for each endpoint are defined as required (mandatory) parameters for the corresponding functions.\
**Any optional parameters** can be passed using same names, as defined in CoinGecko API doc (https://www.coingecko.com/api/docs/v3)

Usage examples:
```python
>>> coins = cg.get_coins_markets(vs_currency="usd", order="market_cap_desc", per_page=2, page=1, sparkline="falset"
[
  {
    "id": "bitcoin",
    "symbol": "btc",
    "name": "Bitcoin",
    "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1547033579",
    "current_price": 43330,
    "market_cap": 815770652999,
    "market_cap_rank": 1,
    "fully_diluted_valuation": 909936661682,
    "total_volume": 32048101812,
    "high_24h": 44229,
    "low_24h": 40890,
    "price_change_24h": 864.75,
    "price_change_percentage_24h": 2.03635,
    "market_cap_change_24h": 12495173806,
    "market_cap_change_percentage_24h": 1.55553,
    "circulating_supply": 18826787.0,
    "total_supply": 21000000.0,
    "max_supply": 21000000.0,
    "ath": 64805,
    "ath_change_percentage": -33.11964,
    "ath_date": "2021-04-14T11:54:46.763Z",
    "atl": 67.81,
    "atl_change_percentage": 63817.22095,
    "atl_date": "2013-07-06T00:00:00.000Z",
    "roi": null,
    "last_updated": "2021-09-26T14:41:38.943Z"
  },
  {
    "id": "ethereum",
    "symbol": "eth",
    "name": "Ethereum",
    "image": "https://assets.coingecko.com/coins/images/279/large/ethereum.png?1595348880",
    "current_price": 3008.18,
    "market_cap": 353771617562,
    "market_cap_rank": 2,
    "fully_diluted_valuation": null,
    "total_volume": 26136001241,
    "high_24h": 3056.55,
    "low_24h": 2745.41,
    "price_change_24h": 112.82,
    "price_change_percentage_24h": 3.8966,
    "market_cap_change_24h": 11545612363,
    "market_cap_change_percentage_24h": 3.37368,
    "circulating_supply": 117682957.499,
    "total_supply": null,
    "max_supply": null,
    "ath": 4356.99,
    "ath_change_percentage": -30.8408,
    "ath_date": "2021-05-12T14:41:48.623Z",
    "atl": 0.432979,
    "atl_change_percentage": 695836.90408,
    "atl_date": "2015-10-20T00:00:00.000Z",
    "roi": {
      "times": 91.75570956889368,
      "currency": "btc",
      "percentage": 9175.570956889369
    },
    "last_updated": "2021-09-26T14:42:12.436Z"
  }
]
```
