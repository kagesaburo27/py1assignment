# py1assignment
# CoinGecko API wrapper


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
### API documentation
https://www.coingecko.com/api/docs/v3

- **/coins/markets** (List all supported coins price, market cap, volume, and market related data)
    ```python 
    cg.get_coins_markets()
    ```
    
 ### Test

Run unit tests with:

```
# after installing pytest using pip3
pytest tests
```
