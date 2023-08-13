import api_requests
import chart_utils

def main():
    print("Welcome to the Crypto Information Portal!")
    coin_input = input("Enter the cryptocurrency symbol or name (e.g., BTC, Ethereum): ").strip()

    coin_id = api_requests.get_coin_id_by_symbol(coin_input)
    if coin_id:
        try:
            coin_details = api_requests.get_cryptocurrency_details(coin_id)
            coin_name = coin_details['name']

            print("\nChoose a currency to display prices in:")
            available_currencies = ['usd', 'eur', 'gbp', 'jpy']
            for idx, currency in enumerate(available_currencies, start=1):
                print(f"{idx}. {currency.upper()}")
            
            currency_choice = int(input("Enter the number of your choice: ")) - 1
            selected_currency = available_currencies[currency_choice]

            # Fetch current price
            price_data = api_requests.get_price_data([coin_id], selected_currency)
            coin_price = price_data[coin_id][selected_currency]
            print(f"Current price: {coin_price} {selected_currency.upper()}")

            # Fetch and display historical data
            historical_data = api_requests.get_historical_data(coin_id, 30)
            chart_utils.display_historical_chart(historical_data, coin_name)
            
        except KeyError:
            print("Data not available for the selected cryptocurrency.")
    else:
        print("Cryptocurrency not found.")

if __name__ == '__main__':
    main()
