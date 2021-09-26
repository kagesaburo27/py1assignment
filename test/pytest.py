import pytest
import requests.exceptions
import responses
import unittest
import unittest.mock as mock

from pycoingecko import CoinGeckoAPI
from requests.exceptions import HTTPError

class TestWrapper(unittest.TestCase):
 #---------- /price/coins/markets ----------#
    @responses.activate
    def test_failed_get_coins_markets(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coins_markets('usd')

    @responses.activate
    def test_get_coins_markets(self):
        # Arrange
        markets_json_sample = [ { "id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1510040391", "current_price": 7015.11823787848, "market_cap": 120934444800.105, "market_cap_rank": 1, "total_volume": 6121170828.21792, "high_24h": 7054.21193531031, "low_24h": 6668.29100755648, "price_change_24h": "299.72373285508", "price_change_percentage_24h": "4.46323343521924", "market_cap_change_24h": "5197755386.983", "market_cap_change_percentage_24h": "4.4910178555649", "circulating_supply": "17236100.0", "ath": 19665.3949272416, "ath_change_percentage": -64.2200698307594, "ath_date": "2017-12-16T00:00:00.000Z", "roi": 0, "last_updated": "2018-08-28T12:12:53.390Z" } ]

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd',
                          json = markets_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_coins_markets('usd')

        ## Assert
        assert response == markets_json_sample