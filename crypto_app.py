import api_requests
import chart_utils

def main():
    print("Welcome to the Crypto Information Portal!")
    coin_input = input("Enter the cryptocurrency symbol or name (e.g., BTC, Ethereum): ").strip()

    coin_id = get_coin_id_by_symbol(coin_input)
    if coin_id:
        try:
            coin_details = get_cryptocurrency_details(coin_id)
            coin_name = coin_details['name']
            coin_symbol = coin_details['symbol']
            coin_description = coin_details['description']['en']

            print("\nCryptocurrency Information:")
            print(f"Name: {coin_name}")
            print(f"Symbol: {coin_symbol}")
            print(f"Description: {coin_description}\n")

            currency_options = {
                1: 'USD',
                2: 'EUR',
                3: 'GBP',
                4: 'JPY'
            }

            print("Choose a currency to display prices in:")
            for num, currency in currency_options.items():
                print(f"{num}. {currency}")

            currency_choice = input("Enter the number of your choice: ")
            chosen_currency = currency_options.get(int(currency_choice), 'USD')

            # Count API calls
            global api_call_count
            api_call_count += 1

            if api_call_count > MAX_API_CALLS:
                print("Maximum number of API calls reached. Further data not available.")
            else:
                # Fetch current price
                price_data = get_price_data([coin_id], chosen_currency)
                coin_price = price_data[coin_id]
                print(f"Current price: {coin_price} {chosen_currency}")

        except requests.exceptions.HTTPError as http_err:
            print(f"Error fetching data: {http_err}")
    else:
        print("Cryptocurrency not found.")

if __name__ == '__main__':
    main()
