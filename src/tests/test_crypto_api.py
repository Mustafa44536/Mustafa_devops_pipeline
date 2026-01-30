import os
import pytest

pytestmark = pytest.mark.skipif(
    not os.getenv("COINMARKETCAP_API_KEY"),
    reason="COINMARKETCAP_API_KEY not set in CI"
)


from webapp.crypto_api import transform, get_response


def test_transform():
    test_fake_data = {
   
        "data": {
            "BTC": [
                    {
                        "id": 1,
                        "name": "Bitcoin",
                        "symbol": "BTC",
                            "quote": {
                            "USD": {
                                    "price": 103929.32609335119,
                                
                                }
                        }
                    },
            ]
        }
    }
    result = transform(test_fake_data)
    #assertions 
    assert result["symbol"] == "BTC"
    assert result["price"] == 103929.32609335119

    
def test_response():
    response = get_response()

    assert response.status_code == 200
