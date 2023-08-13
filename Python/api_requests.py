import requests

base_url = 'https://api.coingecko.com/api/v3'

def get_cryptocurrency_details(coin_id):
    try:
        response = requests.get(f'{base_url}/coins/{coin_id}')
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as req_err:
        print(f"Error fetching cryptocurrency details: {req_err}")
        return None

def get_price_data(coin_ids, vs_currencies, currency):
    try:
        response = requests.get(f'{base_url}/simple/price', params={'ids': ','.join(coin_ids), 'vs_currencies': vs_currencies})
        response.raise_for_status()
        price_data = response.json()

        converted_prices = {}
        for coin_id, coin_prices in price_data.items():
            converted_prices[coin_id] = coin_prices[currency]

        return converted_prices
    except requests.exceptions.RequestException as req_err:
        print(f"Error fetching price data: {req_err}")
        return None

def get_coin_id_by_symbol(symbol):
    try:
        response = requests.get(f'{base_url}/coins/list')
        response.raise_for_status()
        coin_list = response.json()
        for coin_info in coin_list:
            if coin_info['symbol'].lower() == symbol.lower():
                return coin_info['id']
        return None
    except requests.exceptions.RequestException as req_err:
        print(f"Error fetching coin list: {req_err}")
        return None

def get_historical_data(coin_id, days):
    try:
        response = requests.get(f'{base_url}/coins/{coin_id}/market_chart', params={'vs_currency': 'usd', 'days': days})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as req_err:
        print(f"Error fetching historical data: {req_err}")
        return None
